#!/usr/bin/env node
/**
 * fetch-meta-dashboard.mjs — régénère site-2026/dashboard-data.json
 * pour le DERNIER MOIS COMPLET, par campagne (portée, impressions, coûts).
 *
 * Utilise la même stack que notre CLI `meta` :
 *   • jeton system-user : ~/.config/meta-ads/.token   (ou TOKEN_FILE du .env)
 *   • compte : AD_ACCOUNT_ID dans PROBACLAC/Probaclac/.env
 *   • même endpoint Graph que `meta ads insights get` (v23.0, level=campaign)
 *
 * Usage :
 *   node site-2026/tools/fetch-meta-dashboard.mjs            # mois précédent complet
 *   node site-2026/tools/fetch-meta-dashboard.mjs 2026-06    # un mois précis
 *
 * Puis : git add site-2026/dashboard-data.json && git commit && git push
 * (ce que l'agent fait quand tu écris « rafraîchi le dashboard pour le mois passé »).
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { homedir } from 'node:os';
import { resolve, dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const API = 'https://graph.facebook.com/v23.0';
const __dir = dirname(fileURLToPath(import.meta.url));
const SITE = resolve(__dir, '..');                 // site-2026/
const PROJECT = resolve(SITE, '..');               // PROBACLAC/Probaclac/
const OUT = join(SITE, 'dashboard-data.json');

const MONTHS = ['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre'];
const MONTHS_EN = ['January','February','March','April','May','June','July','August','September','October','November','December'];

function readEnv(file){
  const env = {};
  try {
    for (const line of readFileSync(file,'utf8').split('\n')){
      const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$/);
      if (m) env[m[1]] = m[2].replace(/^["']|["']$/g,'');
    }
  } catch {}
  return env;
}
function expand(p){ return p.startsWith('~') ? join(homedir(), p.slice(1)) : p; }

// ── Config from .env + token file (same resolution as the meta CLI bridge) ──
const env = readEnv(join(PROJECT, '.env'));
const ACCOUNT = env.AD_ACCOUNT_ID;
if (!ACCOUNT) { console.error('✖ AD_ACCOUNT_ID introuvable dans', join(PROJECT,'.env')); process.exit(1); }
const tokenFile = expand(env.TOKEN_FILE || join(homedir(), '.config/meta-ads/.token'));
let TOKEN;
try { TOKEN = readFileSync(tokenFile,'utf8').trim(); }
catch { console.error('✖ Jeton introuvable :', tokenFile); process.exit(1); }

// ── Date range : previous complete month (or the YYYY-MM arg) ──
const arg = process.argv[2];
let y, m; // m = 0-indexed
if (arg && /^\d{4}-\d{2}$/.test(arg)) { const [yy,mm]=arg.split('-').map(Number); y=yy; m=mm-1; }
else { const now=new Date(); y=now.getFullYear(); m=now.getMonth()-1; if(m<0){m=11;y--;} }
const pad = n => String(n).padStart(2,'0');
const since = `${y}-${pad(m+1)}-01`;
const until = `${y}-${pad(m+1)}-${pad(new Date(y, m+1, 0).getDate())}`;

async function graph(path, params){
  const u = new URL(`${API}/${path}`);
  for (const [k,v] of Object.entries(params)) u.searchParams.set(k, v);
  u.searchParams.set('access_token', TOKEN);
  const r = await fetch(u);
  const j = await r.json();
  if (j.error) throw new Error(`${j.error.message} (code ${j.error.code})`);
  return j;
}

const OBJ_LABELS = {
  OUTCOME_AWARENESS:'Notoriété', OUTCOME_TRAFFIC:'Trafic', OUTCOME_ENGAGEMENT:'Engagement',
  OUTCOME_LEADS:'Prospects', OUTCOME_SALES:'Ventes', OUTCOME_APP_PROMOTION:'Promotion appli',
  BRAND_AWARENESS:'Notoriété', REACH:'Portée', LINK_CLICKS:'Clics', POST_ENGAGEMENT:'Engagement',
  VIDEO_VIEWS:'Vues vidéo', MESSAGES:'Messages'
};
const num = v => v==null ? 0 : Number(v);

// ── Previous month (for comparison chips) ──
let pm = m-1, py = y; if (pm<0){ pm=11; py--; }
const pSince = `${py}-${pad(pm+1)}-01`;
const pUntil = `${py}-${pad(pm+1)}-${pad(new Date(py, pm+1, 0).getDate())}`;

(async () => {
  const fields = 'campaign_name,campaign_id,objective,spend,impressions,reach,clicks,ctr,cpc,cpm,frequency';
  const acctFields = 'spend,impressions,reach,clicks,ctr,cpc,cpm,frequency';
  const [perCamp, acct, daily, prevAcct] = await Promise.all([
    graph(`${ACCOUNT}/insights`, { level:'campaign', time_range:JSON.stringify({since,until}), fields, limit:'500' }),
    graph(`${ACCOUNT}/insights`, { time_range:JSON.stringify({since,until}), fields:acctFields }),
    graph(`${ACCOUNT}/insights`, { level:'campaign', time_range:JSON.stringify({since,until}), time_increment:'1', fields:'campaign_name,campaign_id,impressions,reach', limit:'500' }),
    graph(`${ACCOUNT}/insights`, { time_range:JSON.stringify({since:pSince,until:pUntil}), fields:acctFields }).catch(()=>({data:[]}))
  ]);

  const campaigns = (perCamp.data||[])
    .filter(c => num(c.impressions) > 0)
    .map(c => ({
      id:c.campaign_id, name:c.campaign_name, objective:c.objective,
      objective_label: OBJ_LABELS[c.objective] || c.objective || '—',
      spend:num(c.spend), impressions:num(c.impressions), reach:num(c.reach),
      clicks:num(c.clicks), ctr:num(c.ctr)/100, cpc:num(c.cpc), cpm:num(c.cpm), frequency:num(c.frequency)
    }))
    .sort((a,b)=>b.impressions-a.impressions);

  const a = (acct.data||[])[0] || {};
  const totals = {
    spend:num(a.spend), impressions:num(a.impressions), reach:num(a.reach), clicks:num(a.clicks),
    ctr:num(a.ctr)/100, cpm:num(a.cpm), cpc:num(a.cpc), frequency:num(a.frequency)
  };

  // ── Previous month block ──
  const p = (prevAcct.data||[])[0];
  const previous = p ? {
    label: `${MONTHS[pm][0].toUpperCase()+MONTHS[pm].slice(1)} ${py}`,
    since:pSince, until:pUntil,
    spend:num(p.spend), impressions:num(p.impressions), reach:num(p.reach), clicks:num(p.clicks),
    ctr:num(p.ctr)/100, cpm:num(p.cpm), cpc:num(p.cpc), frequency:num(p.frequency)
  } : null;

  // ── Daily stacked series (all days of the month, zeros filled) ──
  const nDays = new Date(y, m+1, 0).getDate();
  const dates = Array.from({length:nDays}, (_,i)=>`${y}-${pad(m+1)}-${pad(i+1)}`);
  const dayIdx = Object.fromEntries(dates.map((d,i)=>[d,i]));
  const byCamp = new Map();
  for (const row of (daily.data||[])){
    if (!byCamp.has(row.campaign_id))
      byCamp.set(row.campaign_id, { id:row.campaign_id, name:row.campaign_name,
        impressions:Array(nDays).fill(0), reach:Array(nDays).fill(0) });
    const s = byCamp.get(row.campaign_id), i = dayIdx[row.date_start];
    if (i!=null){ s.impressions[i]+=num(row.impressions); s.reach[i]+=num(row.reach); }
  }
  const dailyOut = { dates, series:[...byCamp.values()].filter(s=>s.impressions.some(v=>v>0)) };

  const now = new Date();
  const out = {
    generated_at: `${now.getFullYear()}-${pad(now.getMonth()+1)}-${pad(now.getDate())}`,
    account_id: ACCOUNT,
    account_label: 'Probaclac (Nicar Canada)',
    period: {
      label: `${MONTHS[m][0].toUpperCase()+MONTHS[m].slice(1)} ${y}`,
      label_en: `${MONTHS_EN[m]} ${y}`, since, until
    },
    totals, previous, campaigns, daily: dailyOut
  };
  writeFileSync(OUT, JSON.stringify(out, null, 2) + '\n');

  // ── Snapshot intégré dans dashboard.html (fallback si fetch échoue : file://, hors-ligne) ──
  const HTML = join(SITE, 'dashboard.html');
  try {
    const html = readFileSync(HTML, 'utf8');
    const tag = /(<script type="application\/json" id="dashData">)[\s\S]*?(<\/script>)/;
    if (tag.test(html)) {
      writeFileSync(HTML, html.replace(tag, (_, a, b) => `${a}\n${JSON.stringify(out)}\n${b}`));
      console.log('✔ snapshot intégré dans dashboard.html');
    }
  } catch (e) { console.warn('⚠ dashboard.html non mis à jour :', e.message); }

  console.log(`✔ ${OUT}`);
  console.log(`  Période : ${out.period.label} (${since} → ${until})`);
  console.log(`  Campagnes avec diffusion : ${campaigns.length}`);
  console.log(`  Portée ${totals.reach.toLocaleString('fr-CA')} · Impressions ${totals.impressions.toLocaleString('fr-CA')} · Dépense ${totals.spend} $`);
})().catch(e => { console.error('✖', e.message); process.exit(1); });

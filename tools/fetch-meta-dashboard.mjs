#!/usr/bin/env node
/**
 * fetch-meta-dashboard.mjs — régénère site-2026/dashboard-data.json
 * pour le DERNIER MOIS COMPLET, par campagne (portée, impressions, coûts).
 *
 * Utilise la même stack que notre CLI `meta` :
 *   • jeton system-user : ~/.config/meta-ads/.token   (ou TOKEN_FILE du .env)
 *   • compte : AD_ACCOUNT_ID dans PROBACLAC/Probaclac/.env
 *   • mot de passe du rapport : DASHBOARD_PASSWORD dans le même .env
 *     (dashboard-data.json et le snapshot de dashboard.html sont chiffrés avec)
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
import { webcrypto as crypto } from 'node:crypto';
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

// ── Chiffrement : le site et le dépôt sont publics, les données n'y vont que chiffrées ──
// AES-256-GCM, clé dérivée du mot de passe (PBKDF2-SHA256). Le dashboard déchiffre dans le navigateur.
const PASSWORD = env.DASHBOARD_PASSWORD;
if (!PASSWORD || PASSWORD.length < 12) { console.error('✖ DASHBOARD_PASSWORD (12 caractères min.) introuvable dans', join(PROJECT,'.env')); process.exit(1); }
const KDF_ITER = 600000;
const b64 = u8 => Buffer.from(u8).toString('base64');
async function encrypt(obj){
  const salt = crypto.getRandomValues(new Uint8Array(16)), iv = crypto.getRandomValues(new Uint8Array(12));
  const base = await crypto.subtle.importKey('raw', new TextEncoder().encode(PASSWORD), 'PBKDF2', false, ['deriveKey']);
  const key = await crypto.subtle.deriveKey({name:'PBKDF2', salt, iterations:KDF_ITER, hash:'SHA-256'}, base, {name:'AES-GCM', length:256}, false, ['encrypt']);
  const ct = await crypto.subtle.encrypt({name:'AES-GCM', iv}, key, new TextEncoder().encode(JSON.stringify(obj)));
  return { v:1, alg:'AES-256-GCM', kdf:'PBKDF2-SHA256', iter:KDF_ITER, salt:b64(salt), iv:b64(iv), ct:b64(new Uint8Array(ct)) };
}

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

// ── Historique : les HISTORY_MONTHS derniers mois complets, jusqu'au mois du rapport ──
const HISTORY_MONTHS = 6;
let hm = m-(HISTORY_MONTHS-1), hy = y; while (hm<0){ hm+=12; hy--; }
const hSince = `${hy}-${pad(hm+1)}-01`;

(async () => {
  const fields = 'campaign_name,campaign_id,objective,spend,impressions,reach,clicks,ctr,cpc,cpm,frequency';
  const acctFields = 'spend,impressions,reach,clicks,ctr,cpc,cpm,frequency';
  const [perCamp, acct, daily, prevAcct, hist] = await Promise.all([
    graph(`${ACCOUNT}/insights`, { level:'campaign', time_range:JSON.stringify({since,until}), fields, limit:'500' }),
    graph(`${ACCOUNT}/insights`, { time_range:JSON.stringify({since,until}), fields:acctFields }),
    graph(`${ACCOUNT}/insights`, { level:'campaign', time_range:JSON.stringify({since,until}), time_increment:'1', fields:'campaign_name,campaign_id,impressions,reach', limit:'500' }),
    graph(`${ACCOUNT}/insights`, { time_range:JSON.stringify({since:pSince,until:pUntil}), fields:acctFields }).catch(()=>({data:[]})),
    graph(`${ACCOUNT}/insights`, { time_range:JSON.stringify({since:hSince,until}), time_increment:'monthly', fields:acctFields, limit:'50' }).catch(()=>({data:[]}))
  ]);

  // ── Historique mensuel (mois sans diffusion = zéros, pour garder la série continue) ──
  const histRows = Object.fromEntries((hist.data||[]).map(r=>[r.date_start.slice(0,7), r]));
  const history = Array.from({length:HISTORY_MONTHS}, (_,i)=>{
    let mm = hm+i, yy = hy; while (mm>11){ mm-=12; yy++; }
    const key = `${yy}-${pad(mm+1)}`, r = histRows[key] || {};
    return {
      month:key, label:`${MONTHS[mm][0].toUpperCase()+MONTHS[mm].slice(1)} ${yy}`,
      spend:num(r.spend), impressions:num(r.impressions), reach:num(r.reach), clicks:num(r.clicks),
      ctr:num(r.ctr)/100, cpm:num(r.cpm), cpc:num(r.cpc), frequency:num(r.frequency)
    };
  });

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
    totals, previous, history, campaigns, daily: dailyOut
  };
  const sealed = await encrypt(out);
  writeFileSync(OUT, JSON.stringify(sealed) + '\n');

  // ── Snapshot chiffré intégré dans dashboard.html (fallback si fetch échoue : file://, hors-ligne) ──
  const HTML = join(SITE, 'dashboard.html');
  try {
    const html = readFileSync(HTML, 'utf8');
    const tag = /(<script type="application\/json" id="dashData">)[\s\S]*?(<\/script>)/;
    if (tag.test(html)) {
      writeFileSync(HTML, html.replace(tag, (_, a, b) => `${a}\n${JSON.stringify(sealed)}\n${b}`));
      console.log('✔ snapshot intégré dans dashboard.html');
    }
  } catch (e) { console.warn('⚠ dashboard.html non mis à jour :', e.message); }

  console.log(`✔ ${OUT} (chiffré, AES-256-GCM)`);
  console.log(`  Période : ${out.period.label} (${since} → ${until})`);
  console.log(`  Campagnes avec diffusion : ${campaigns.length}`);
  console.log(`  Portée ${totals.reach.toLocaleString('fr-CA')} · Impressions ${totals.impressions.toLocaleString('fr-CA')} · Dépense ${totals.spend} $`);
})().catch(e => { console.error('✖', e.message); process.exit(1); });

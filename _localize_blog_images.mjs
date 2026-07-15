// Télécharge les images Wix (static.wixstatic.com) dans assets/blog/ et repointe
// toutes les références HTML vers le local (chemin ajusté selon la profondeur).
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const ROOT = path.resolve('.');
const IMGDIR = path.join(ROOT, 'assets/blog');
fs.mkdirSync(IMGDIR, { recursive: true });

// Liste tous les .html hors backup / node_modules
function walk(dir, acc = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.name === '_html_backup' || e.name === 'node_modules' || e.name === '.git') continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, acc);
    else if (e.name.endsWith('.html')) acc.push(p);
  }
  return acc;
}
const files = walk(ROOT);

const URL_RE = /https:\/\/static\.wixstatic\.com\/media\/[^"'()\s]+/g;

// url -> {local: "<id>.<ext>", canon: "url de téléchargement (sans /v1/…)"}
function parse(url) {
  const rest = url.replace('https://static.wixstatic.com/media/', '');
  const beforeV1 = rest.split('/v1/')[0];               // <id>~mv2.<ext>  ou  <id>.<ext>
  const m = beforeV1.match(/^(.+?)(~mv2)?\.([a-zA-Z0-9]+)$/);
  if (!m) return null;
  const local = `${m[1]}.${m[3].toLowerCase()}`;
  const canon = 'https://static.wixstatic.com/media/' + beforeV1;
  return { local, canon };
}

// 1) Collecte des URL uniques
const urlSet = new Set();
for (const f of files) {
  const html = fs.readFileSync(f, 'utf8');
  const ms = html.match(URL_RE);
  if (ms) ms.forEach(u => urlSet.add(u));
}

// 2) Téléchargement (un original par nom local)
const downloaded = new Set();
let dlOk = 0, dlFail = [];
for (const u of urlSet) {
  const p = parse(u);
  if (!p) { dlFail.push(u); continue; }
  const dest = path.join(IMGDIR, p.local);
  if (downloaded.has(p.local) || fs.existsSync(dest)) { downloaded.add(p.local); continue; }
  try {
    execFileSync('curl', ['-sfL', '-A', 'Mozilla/5.0', p.canon, '-o', dest], { stdio: 'ignore' });
    if (fs.existsSync(dest) && fs.statSync(dest).size > 0) { downloaded.add(p.local); dlOk++; }
    else dlFail.push(p.canon);
  } catch (e) { dlFail.push(p.canon); }
}

// 3) Réécriture des références (profondeur -> préfixe)
let filesChanged = 0, refsChanged = 0;
for (const f of files) {
  const rel = path.relative(ROOT, f);
  const depth = rel.split(path.sep).length - 1;         // 0 = racine, 1 = blogue/en, 2 = en/blogue
  const prefix = '../'.repeat(depth) + 'assets/blog/';
  let html = fs.readFileSync(f, 'utf8'), n = 0;
  html = html.replace(URL_RE, (u) => {
    const p = parse(u);
    if (!p || !downloaded.has(p.local)) return u;        // laisse tel quel si non téléchargé
    n++;
    return prefix + p.local;
  });
  if (n) { fs.writeFileSync(f, html); filesChanged++; refsChanged += n; }
}

console.log(`Images uniques: ${urlSet.size} | téléchargées: ${dlOk} | échecs: ${dlFail.length}`);
if (dlFail.length) console.log('ÉCHECS:\n' + dlFail.slice(0, 20).join('\n'));
console.log(`Fichiers modifiés: ${filesChanged} | références repointées: ${refsChanged}`);

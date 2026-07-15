// Génère les pages d'articles EN dans en/blogue/<slug>.html
// Chrome = en/blogue.html (head+nav+footer, anglais) avec chemins ajustés pour la profondeur 2.
// Contenu = métadonnées des cartes de en/blogue.html + texte source en/blogue/_src/<slug>.txt
import fs from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve('.');
const idxPath = path.join(ROOT, 'en/blogue.html');
const idx = fs.readFileSync(idxPath, 'utf8');

// --- 1. Découpe le chrome ---
const navEnd = idx.indexOf('</nav>') + '</nav>'.length;
const headNav = idx.slice(0, navEnd);                       // <head>…</head><body><nav>…</nav>
const footStart = idx.indexOf('<footer');
const footEnd = idx.indexOf('</footer>') + '</footer>'.length;
const footer = idx.slice(footStart, footEnd);
const scripts = idx.slice(footEnd); // inclut le <script> + </body></html>

// Ajoute un ../ à chaque chemin relatif d'attribut HTML (profondeur 1 -> 2)
const deepen = s => s.replace(/(href|src)="(?!https?:|#|mailto:|tel:|\/\/|data:)([^"]+)"/g,
  (_, a, p) => `${a}="../${p}"`);
// Idem pour les chemins dans le JS (assets + url:"…​.html" du CATALOGUE)
const deepenJS = s => s
  .replace(/(['"])\.\.\/assets\//g, '$1../../assets/')
  .replace(/url:"(?!https?:|\.\.\/)([^"]+\.html)"/g, 'url:"../$1"');

const headNavDeep = deepen(headNav);
const footerDeep = deepen(footer);
const scriptsDeep = deepenJS(deepen(scripts));

// --- 2. Extrait les cartes ---
const cardRe = /<a class="blogcard r" href="https:\/\/www\.probaclac\.ca\/en\/post\/([^"]+)"[^>]*>\s*<div class="blogcard__img"><img src="([^"]+)" alt="([^"]*)"[^>]*><\/div>\s*<div class="blogcard__body">\s*<span class="blogcard__date">([^<]*)<\/span>\s*<h2 class="blogcard__title">([^<]*)<\/h2>/g;
const asciiSlug = s => s.normalize('NFD').replace(/[̀-ͯ]/g, '');
const cards = {};
let m;
while ((m = cardRe.exec(idx))) {
  cards[m[1]] = { slug: m[1], file: asciiSlug(m[1]), img: m[2], alt: m[3], date: m[4], title: m[5] };
}
const allTitles = new Set(Object.values(cards).map(c => c.title.trim()));

// --- 3. Texte -> paragraphes ---
const esc = s => s.replace(/&(?!#?\w+;)/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
function bodyHtml(txt) {
  let blocks = txt.replace(/\r/g, '').split(/\n\s*\n+/).map(b => b.trim()).filter(Boolean);
  // retire les blocs de fin qui sont en fait des titres d'autres articles (posts reliés)
  while (blocks.length && allTitles.has(blocks[blocks.length - 1])) blocks.pop();
  return blocks.map(b => `      <p>${esc(b).replace(/\n/g, ' ')}</p>`).join('\n');
}

// --- 4. Assemble ---
const srcDir = path.join(ROOT, 'en/blogue/_src');
const outDir = path.join(ROOT, 'en/blogue');
let built = [], missing = [];
for (const slug of Object.keys(cards)) {
  const c = cards[slug];
  const srcFile = path.join(srcDir, c.file + '.txt');
  if (!fs.existsSync(srcFile)) { missing.push(slug); continue; }
  const body = bodyHtml(fs.readFileSync(srcFile, 'utf8'));
  const main = `
<main class="post">
  <div class="wrap">
    <a class="post__back" href="../blogue.html"><span>←</span> All articles</a>
    <header class="post__head r">
      <div class="post__eyebrow">Blog · Probaclac</div>
      <h1 class="post__title">${c.title}</h1>
      <div class="post__meta"><span>${c.date}</span><span>By Probaclac</span></div>
    </header>
    <figure class="post__cover r"><img src="${c.img}" alt="${c.alt}" loading="eager"></figure>
    <div class="post__body r">
${body}
    </div>
    <div class="post__cta">
      <a class="btn btn--solid" href="../blogue.html">See all articles<span class="arr">→</span></a>
      <a class="btn btn--ghost" href="https://www.monprobiotique.ca">See the range<span class="arr">→</span></a>
    </div>
  </div>
</main>
`;
  const page = headNavDeep + '\n' + main + '\n' + footerDeep + '\n' + scriptsDeep;
  fs.writeFileSync(path.join(outDir, c.file + '.html'), page);
  built.push(c.file);
}
console.log('Construits (' + built.length + '):', built.join(', ') || '—');
console.log('Sans source .txt (' + missing.length + '):', missing.join(', ') || '—');

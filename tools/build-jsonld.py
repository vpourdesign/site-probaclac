# -*- coding: utf-8 -*-
"""
Génère le JSON-LD schema.org de toutes les pages de site-2026/.
Ne touche ni au contenu visible ni aux URL : tout est dérivé de ce que la page contient déjà.
Idempotent — relancer remplace le bloc existant.
"""
import re, json, glob, os, html as H

# Usage : python3 tools/build-jsonld.py   (depuis la racine du dépôt ou n'importe où)
ROOT   = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ORIGIN = 'https://probaclac.ca'
ORG    = f'{ORIGIN}/#organization'
SITE   = f'{ORIGIN}/#website'
MARK   = 'data-pbl-schema'

# Nœuds trop riches pour être régénérés (études cliniques, conditions traitées).
# Récupérés depuis les blocs existants et réinjectés à chaque passe.
try:
    PRESERVED = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                            'jsonld-preserved.json'), encoding='utf-8'))
except FileNotFoundError:
    PRESERVED = {}

# conditions traitées par chaque page — dérivées du sujet déjà présent sur la page
ABOUT = {
 'probiotique-vaginal.html':          ['Vaginose bactérienne'],
 'probiotique-infection-a-levure.html':['Candidose vulvovaginale'],
 'probiotique-infection-urinaire.html':['Infection urinaire'],
 'probiotique-colon-irritable.html':  ["Syndrome de l'intestin irritable"],
 'probiotique-antibiotique.html':     ['Diarrhée associée aux antibiotiques'],
 'probiotique-gastro-intestinal.html':['Diarrhée associée aux antibiotiques', 'Déséquilibre de la flore intestinale'],
 'probiotique-voyage.html':           ['Diarrhée du voyageur'],
 'diarrhee-du-voyageur.html':         ['Diarrhée du voyageur'],
 'microbiote.html':                   ['Déséquilibre de la flore intestinale'],
 'meilleur-probiotique.html':         ['Déséquilibre de la flore intestinale', 'Diarrhée associée aux antibiotiques',
                                       "Syndrome de l'intestin irritable", 'Vaginose bactérienne'],
 'best-probiotic.html':               ['Gut flora imbalance', 'Antibiotic-associated diarrhea',
                                       'Irritable bowel syndrome', 'Bacterial vaginosis'],
}
# seules dates réellement connues — on n'en invente aucune
DATE_MOD = {'meilleur-probiotique.html': '2026-09-10'}

MOIS = {'janvier':1,'février':2,'mars':3,'avril':4,'mai':5,'juin':6,'juillet':7,
        'août':8,'septembre':9,'octobre':10,'novembre':11,'décembre':12,
        'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,
        'august':8,'september':9,'october':10,'november':11,'december':12}

def txt(s):
    s = re.sub(r'(?s)<(script|style).*?</\1>', '', s or '')
    return re.sub(r'\s+', ' ', H.unescape(re.sub('<[^>]*>', ' ', s))).strip()

def url_for(path):
    p = path.replace(os.sep, '/')
    if p == 'index.html':      return ORIGIN + '/'
    if p == 'en/index.html':   return ORIGIN + '/en/'
    return f'{ORIGIN}/{p[:-5]}'

EN_AT_ROOT = {'studies.html'}   # pages anglaises hors du dossier en/

def lang_of(rel):
    return 'en' if rel.startswith('en/') or rel in EN_AT_ROOT else 'fr'

def set_lang(h, rel):
    return re.sub(r'<html\s+lang="[^"]*"', f'<html lang="{lang_of(rel)}-CA"', h, count=1)

def set_hreflang(h, rel, twin):
    """Retire les hreflang existants, puis pose fr-CA / en-CA / x-default (FR) sous le canonical si la page a une traduction sûre."""
    h = re.sub(r'\n?<link\s+rel="alternate"\s+hreflang="[^"]*"[^>]*>', '', h)
    if not twin:
        return h
    fr, en = (rel, twin) if lang_of(rel) == 'fr' else (twin, rel)
    links = (f'\n<link rel="alternate" hreflang="fr-CA" href="{url_for(fr)}">'
             f'\n<link rel="alternate" hreflang="en-CA" href="{url_for(en)}">'
             f'\n<link rel="alternate" hreflang="x-default" href="{url_for(fr)}">')
    tag = f'<link rel="canonical" href="{url_for(rel)}">'
    return h.replace(tag, tag + links, 1)

def meta(h, name):
    m = re.search(rf'<meta\s+name="{name}"\s+content="([^"]*)"', h) \
        or re.search(rf'<meta\s+content="([^"]*)"\s+name="{name}"', h)
    return H.unescape(m.group(1)).strip() if m else None

def title_of(h):
    m = re.search(r'(?s)<title>(.*?)</title>', h)
    return txt(m.group(1)) if m else None

def h1_of(h):
    m = re.search(r'(?s)<h1[^>]*>(.*?)</h1>', re.sub(r'(?s)<(script|style).*?</\1>', '', h))
    return txt(m.group(1)) if m else None

def date_of(h):
    m = re.search(r'(?s)<div class="post__meta">(.*?)</div>', h)
    seg = txt(m.group(1)) if m else txt(h)
    d = re.search(r'\b(\d{1,2})\s+([A-Za-zÀ-ÿ]+)\s+(20\d{2})\b', seg)
    if d and d.group(2).lower() in MOIS:
        return f'{d.group(3)}-{MOIS[d.group(2).lower()]:02d}-{int(d.group(1)):02d}'
    return None

def catalogue(h):
    m = re.search(r'(?s)const CATALOGUE = \[(.*?)\];', h)
    if not m: return {}
    out = {}
    for row in re.findall(r'\{(.*?)\}', m.group(1)):
        f = dict(re.findall(r'(\w+)\s*:\s*"([^"]*)"', row))
        if 'url' in f: out[f['url']] = f
    return out

def strip_old(h):
    return re.sub(rf'(?s)\n?<script type="application/ld\+json" {MARK}>.*?</script>', '', h)

def set_canonical(h, url):
    """Un seul canonical par page, sur l'apex, sans .html. Remplace l'existant, sinon le pose après <title>."""
    tag = f'<link rel="canonical" href="{url}">'
    pat = r'<link\s+rel="canonical"[^>]*>'
    if re.search(pat, h):
        h = re.sub(pat, lambda m: tag, h, count=1)
        first = h.index(tag) + len(tag)
        return h[:first] + re.sub(r'\n?' + pat, '', h[first:])   # doublons éventuels
    if '</title>' in h:
        return h.replace('</title>', '</title>\n' + tag, 1)
    return h.replace('</head>', tag + '\n</head>', 1)

# ── nœuds partagés ────────────────────────────────────────────────────────────
def org_node():
    return {
        "@type": "Organization", "@id": ORG,
        "name": "Probaclac", "url": ORIGIN + '/',
        "logo": {"@type": "ImageObject", "@id": f"{ORIGIN}/#logo",
                 "url": f"{ORIGIN}/assets/logo.png", "caption": "Probaclac"},
        "image": {"@id": f"{ORIGIN}/#logo"},
        "description": "Probiotiques de grade pharmaceutique formulés au Québec. "
                       "Chaque formule est homologuée par Santé Canada et porte son propre "
                       "numéro de produit naturel (NPN).",
        "telephone": "+1-800-567-9683",
        "address": {"@type": "PostalAddress", "streetAddress": "31 rue Gaston-Dumoulin, suite 103",
                    "addressLocality": "Blainville", "addressRegion": "QC",
                    "postalCode": "J7C 6B4", "addressCountry": "CA"},
        "areaServed": {"@type": "Country", "name": "Canada"},
        "parentOrganization": {"@type": "Organization", "name": "Laboratoires Nicar"},
        "sameAs": ["https://www.facebook.com/Probaclac", "https://www.instagram.com/probaclac.ca"],
    }

def site_node():
    return {"@type": "WebSite", "@id": SITE, "url": ORIGIN + '/', "name": "Probaclac",
            "publisher": {"@id": ORG}, "inLanguage": ["fr-CA", "en-CA"]}

def crumbs(url, trail):
    return {"@type": "BreadcrumbList", "@id": url + "#breadcrumb",
            "itemListElement": [{"@type": "ListItem", "position": i, "name": n,
                                 **({"item": u} if u else {})}
                                for i, (n, u) in enumerate(trail, 1)]}

def product_node(url, entry, lang):
    npn = entry['npn'].replace('NPN', '').strip()
    props = [{"@type": "PropertyValue",
              "name": "Numéro de produit naturel (NPN)" if lang == 'fr' else "Natural Product Number (NPN)",
              "value": npn},
             {"@type": "PropertyValue",
              "name": "Composition" if lang == 'fr' else "Composition",
              "value": entry['meta']}]
    return {"@type": ["Product", "DietarySupplement"], "@id": url + "#product",
            "name": f"Probaclac {entry['name']}", "url": url,
            "brand": {"@id": ORG}, "manufacturer": {"@id": ORG},
            "category": entry.get('catLabel'),
            "identifier": {"@type": "PropertyValue", "propertyID": "NPN", "value": npn},
            "additionalProperty": props,
            "countryOfOrigin": {"@type": "Country", "name": "Canada"},
            "safetyConsideration": ("Consultez un professionnel de la santé si les symptômes persistent."
                                    if lang == 'fr' else
                                    "Consult a health care practitioner if symptoms persist."),
            "isProprietary": False}

def faq_node(url, h, lang):
    pairs = re.findall(
        r'(?s)<button class="faq__q"[^>]*>\s*<span>(.*?)</span>.*?<p class="faq__a">(.*?)</p>', h)
    if not pairs: return None
    return {"@type": "FAQPage", "@id": url + "#faq", "inLanguage": lang + "-CA",
            "isPartOf": {"@id": url + "#webpage"},
            "mainEntity": [{"@type": "Question", "name": txt(q),
                            "acceptedAnswer": {"@type": "Answer", "text": txt(a)}}
                           for q, a in pairs]}

# ── construction par page ─────────────────────────────────────────────────────
def build(path, h, pairs):
    p    = path.replace(os.sep, '/')
    rel  = p[3:] if p.startswith('en/') else p
    lang = lang_of(p)
    url  = url_for(p)
    base = os.path.basename(p)
    home = ORIGIN + ('/en/' if lang == 'en' else '/')
    ttl  = title_of(h) or h1_of(h) or 'Probaclac'
    desc = meta(h, 'description')
    cat  = catalogue(h)
    g    = [org_node(), site_node()]

    page = {"@id": url + "#webpage", "url": url, "name": ttl, "inLanguage": lang + "-CA",
            "isPartOf": {"@id": SITE}, "publisher": {"@id": ORG},
            "breadcrumb": {"@id": url + "#breadcrumb"}}
    if desc: page["description"] = desc
    if h1_of(h): page["headline"] = h1_of(h)

    # lien de traduction, sans jamais créer d'URL : uniquement si les deux fichiers existent
    twin = pairs.get(p)
    if twin:
        key = "workTranslation" if lang == 'fr' else "translationOfWork"
        page[key] = {"@id": url_for(twin) + "#webpage"}

    trail = [("Accueil" if lang == 'fr' else "Home", home)]

    # ── accueil
    if base == 'index.html' and rel == 'index.html':
        page["@type"] = ["WebPage", "CollectionPage"]
        trail = [("Accueil" if lang == 'fr' else "Home", None)]
        if cat:
            g.append({"@type": "ItemList", "@id": url + "#formules",
                      "name": "Les formules Probaclac" if lang == 'fr' else "Probaclac formulas",
                      "numberOfItems": len(cat),
                      "itemListOrder": "https://schema.org/ItemListUnordered",
                      "itemListElement": [
                          {"@type": "ListItem", "position": i,
                           "url": f"{home}{u[:-5]}", "name": f"Probaclac {e['name']}"}
                          for i, (u, e) in enumerate(cat.items(), 1)]})
    # ── pages produit
    elif rel.startswith('probiotique-'):
        page["@type"] = ["MedicalWebPage", "WebPage"]
        page["specialty"] = {"@type": "MedicalSpecialty", "name": "Gastroenterology"}
        entry = cat.get(base)
        if entry:
            prod = product_node(url, entry, lang)
            g.append(prod)
            page["mainEntity"] = {"@id": prod["@id"]}
            trail += [("Nos produits" if lang == 'fr' else "Products", None),
                      (f"Probaclac {entry['name']}", None)]
        else:
            trail += [(ttl, None)]
    # ── guides comparatifs
    elif rel in ('meilleur-probiotique.html', 'best-probiotic.html'):
        page["@type"] = ["MedicalWebPage", "WebPage"]
        page["specialty"] = {"@type": "MedicalSpecialty", "name": "Gastroenterology"}
        trail += [(h1_of(h) or ttl, None)]
        if cat:
            g.append({"@type": "ItemList", "@id": url + "#formules",
                      "numberOfItems": len(cat),
                      "itemListElement": [
                          {"@type": "ListItem", "position": i,
                           "url": f"{home}{u[:-5]}", "name": f"Probaclac {e['name']}"}
                          for i, (u, e) in enumerate(cat.items(), 1)]})
    # ── FAQ
    elif rel == 'foire-aux-questions.html':
        page["@type"] = ["FAQPage", "WebPage"]
        trail += [(h1_of(h) or ttl, None)]
        f = faq_node(url, h, lang)
        if f:
            page["mainEntity"] = f["mainEntity"]
    # ── index du blogue
    elif rel == 'blogue.html':
        page["@type"] = ["Blog", "CollectionPage"]
        trail += [("Blogue" if lang == 'fr' else "Blog", None)]
        links = sorted(set(re.findall(r'href="((?:\.\./)?blogue/[^"#]+)\.html"', h)))
        if links:
            g.append({"@type": "ItemList", "@id": url + "#articles",
                      "numberOfItems": len(links),
                      "itemListElement": [
                          {"@type": "ListItem", "position": i,
                           "url": f"{home}blogue/{l.split('/')[-1]}"}
                          for i, l in enumerate(links, 1)]})
    # ── articles
    elif '/blogue/' in rel or rel.startswith('blogue/'):
        page["@type"] = ["BlogPosting", "WebPage"]
        page["author"] = {"@id": ORG}
        page["mainEntityOfPage"] = {"@id": url + "#webpage"}
        d = date_of(h)
        if d:
            page["datePublished"] = d
            page["dateModified"]  = d
        trail += [("Blogue" if lang == 'fr' else "Blog", f"{home}blogue"),
                  (h1_of(h) or ttl, None)]
    # ── pages éditoriales santé
    elif rel in ('microbiote.html', 'diarrhee-du-voyageur.html', 'etudes.html', 'studies.html'):
        page["@type"] = ["MedicalWebPage", "WebPage"]
        page["specialty"] = {"@type": "MedicalSpecialty", "name": "Gastroenterology"}
        trail += [(h1_of(h) or ttl, None)]
    elif rel == 'histoire.html':
        page["@type"] = ["AboutPage", "WebPage"]
        page["mainEntity"] = {"@id": ORG}
        trail += [(h1_of(h) or ttl, None)]
    else:
        page["@type"] = "WebPage"
        trail += [(h1_of(h) or ttl, None)]

    # enrichissements dérivés du sujet de la page
    if 'MedicalWebPage' in (page["@type"] if isinstance(page["@type"], list) else [page["@type"]]):
        page.setdefault("author", {"@id": ORG})
        page.setdefault("reviewedBy", {"@id": ORG})
        page.setdefault("audience", {"@type": "PeopleAudience",
                                     "geographicArea": {"@type": "Country", "name": "Canada"}})
    conds = ABOUT.get(rel)
    if conds:
        page["about"] = [{"@type": "MedicalCondition", "name": c} for c in conds]
    if rel in DATE_MOD:
        page["dateModified"] = DATE_MOD[rel]

    # réinjection des nœuds préservés (études cliniques d'/etudes et /studies)
    keep = PRESERVED.get(rel)
    if keep:
        if keep.get('about'):
            page["about"] = keep['about']
        il = keep.get('itemList')
        if il:
            node = {"@type": "ItemList", "@id": url + "#etudes",
                    "name": il['name'], "numberOfItems": len(il['itemListElement']),
                    "itemListElement": il['itemListElement']}
            g.append(node)
            page["mainEntity"] = {"@id": node["@id"]}

    g.append(page)
    g.append(crumbs(url, trail))
    fq = faq_node(url, h, lang)
    if fq and rel != 'foire-aux-questions.html':
        g.append(fq)
    return {"@context": "https://schema.org", "@graph": g}

# ── passe principale ──────────────────────────────────────────────────────────
EXCLUDE = ('assets/', 'adultes-stitch/')   # gabarits de travail, pas des pages du site
files = sorted(f for f in glob.glob(f'{ROOT}/**/*.html', recursive=True)
               if not any(x in f.replace(os.sep, '/') for x in EXCLUDE))
rels  = {f[len(ROOT) + 1:].replace(os.sep, '/') for f in files}
pairs = {}
for r in rels:
    if r.startswith('en/'):
        fr = r[3:]
        if fr in rels: pairs[r] = fr
    else:
        en = 'en/' + r
        if en in rels: pairs[r] = en
pairs['meilleur-probiotique.html'] = 'en/best-probiotic.html'
pairs['en/best-probiotic.html']    = 'meilleur-probiotique.html'
pairs['etudes.html']               = 'studies.html'
pairs['studies.html']              = 'etudes.html'
# Les articles de blogue n'ont pas de paire : slugs différents d'une langue à l'autre,
# table de correspondance à valider avant de les déclarer.

done = skipped = 0
for f in files:
    rel = f[len(ROOT) + 1:].replace(os.sep, '/')
    if rel == 'dashboard.html':          # interdit dans robots.txt
        skipped += 1; continue
    h = open(f, encoding='utf-8', errors='ignore').read()
    if '</head>' not in h:
        skipped += 1; continue
    h = strip_old(h)
    h = set_canonical(h, url_for(rel))
    h = set_hreflang(h, rel, pairs.get(rel))
    h = set_lang(h, rel)
    h = re.sub(r'(?s)<script type="application/ld\+json">.*?</script>\n?', '', h)  # anciens blocs
    ld = build(rel, h, pairs)
    tag = ('<script type="application/ld+json" ' + MARK + '>\n'
           + json.dumps(ld, ensure_ascii=False, indent=2) + '\n</script>\n')
    open(f, 'w', encoding='utf-8').write(h.replace('</head>', tag + '</head>', 1))
    done += 1
print(f'JSON-LD + canonical écrits sur {done} pages · {skipped} ignorées')

# ── 301 .html → URL propre ────────────────────────────────────────────────────
# Netlify sert /page ET /page.html en 200. Une règle forcée par page supprime le doublon.
# Le bloc est régénéré entre ses deux marqueurs, le reste de _redirects n'est pas touché.
BEGIN, END = '# >>> 0 · .html → URL propre (généré par tools/build-jsonld.py)', '# <<< fin .html'
rules = []
for rel in sorted(rels - {'dashboard.html'}):
    dest = url_for(rel)[len(ORIGIN):]
    rules.append(f'/{rel:<96}  {dest:<50}  301!')

# Copies de sauvegarde de juillet, publiques par erreur : doublons sans canonical pour Google.
# Les fichiers restent dans le dépôt; toute URL qui les vise part vers la vraie page.
BACKUP = 'assets/wix/_html_backup'
BACKUP_DEST = {'adultes-stitch__index.html': 'probiotique-adulte.html'}   # gabarit de la page Adultes
for f in sorted(glob.glob(f'{ROOT}/{BACKUP}/*.html')):
    name = os.path.basename(f)
    target = BACKUP_DEST.get(name, name)
    if target not in rels:
        continue
    dest = url_for(target)[len(ORIGIN):]
    for src in (f'/{BACKUP}/{name}', f'/{BACKUP}/{name[:-5]}'):
        rules.append(f'{src:<97}  {dest:<50}  301!')
block =BEGIN + '\n' + '\n'.join(rules) + '\n' + END
rp = os.path.join(ROOT, '_redirects')
r = open(rp, encoding='utf-8').read()
if BEGIN in r:
    r = re.sub(r'(?s)' + re.escape(BEGIN) + r'.*?' + re.escape(END), lambda m: block, r)
else:
    anchor = '# ─── 1 · PAGES FR'
    r = r.replace(anchor, block + '\n\n\n' + anchor, 1)
open(rp, 'w', encoding='utf-8').write(r)
print(f'_redirects : {len(rules)} règles (.html + copies de sauvegarde)')

# ── sitemap.xml + robots.txt ──────────────────────────────────────────────────
# Mêmes URL que les canonical : apex, sans .html, une par page réelle.
# Pas de <lastmod> : les commits touchent souvent les 108 pages d'un coup (en-têtes),
# une date identique partout serait fausse et Google cesserait de s'y fier.
locs = [url_for(rel) for rel in sorted(rels - {'dashboard.html'}, key=lambda r: (r.count('/'), not r.endswith('index.html'), r))]
xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
       + ''.join(f'  <url><loc>{u}</loc></url>\n' for u in locs)
       + '</urlset>\n')
open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(xml)
rb = os.path.join(ROOT, 'robots.txt')
t = re.sub(r'(?m)^Sitemap:.*$', f'Sitemap: {ORIGIN}/sitemap.xml', open(rb, encoding='utf-8').read())
open(rb, 'w', encoding='utf-8').write(t)
print(f'sitemap.xml : {len(locs)} URL')

# -*- coding: utf-8 -*-
"""
Slugs anglais des pages /en/ — table de correspondance unique du site.
Les pages EN portaient les slugs français (/en/probiotique-voyage) : on les
renomme en anglais, on réécrit tous les liens internes, et _redirects reçoit
une 301 de chaque ancienne URL vers la nouvelle.

Usage : python3 tools/en-slugs.py          (renomme + réécrit, une seule fois)
Importé par tools/build-jsonld.py pour les paires hreflang FR ↔ EN.
"""
import os, re, glob, subprocess

# FR (chemin du fichier)            →  EN (chemin du fichier, sous en/)
EN_SLUGS = {
    'probiotique-adulte.html':             'en/adult-probiotic.html',
    'probiotique-50-et-plus.html':         'en/probiotic-50-plus.html',
    'probiotique-antibiotique.html':       'en/probiotic-for-antibiotics.html',
    'probiotique-bebes.html':              'en/baby-probiotic.html',
    'probiotique-colon-irritable.html':    'en/probiotic-for-ibs.html',
    'probiotique-enfant.html':             'en/kids-probiotic.html',
    'probiotique-extra-fort.html':         'en/extra-strength-probiotic.html',
    'probiotique-gastro-intestinal.html':  'en/gastrointestinal-probiotic.html',
    'probiotique-infection-a-levure.html': 'en/probiotic-for-yeast-infections.html',
    'probiotique-infection-urinaire.html': 'en/probiotic-for-uti.html',
    'probiotique-vaginal.html':            'en/vaginal-probiotic.html',
    'probiotique-voyage.html':             'en/travel-probiotic.html',
    'diarrhee-du-voyageur.html':           'en/travelers-diarrhea.html',
    'foire-aux-questions.html':            'en/faq.html',
    'histoire.html':                       'en/our-story.html',
    'microbiote.html':                     'en/microbiome.html',
    'blogue.html':                         'en/blog.html',
    'meilleur-probiotique.html':           'en/best-probiotic.html',
    'privacy-policy.html':                 'en/privacy-policy.html',
    'index.html':                          'en/index.html',
    'etudes.html':                         'studies.html',
}
# Le dossier des articles suit l'index : en/blogue/ → en/blog/
EN_BLOG_OLD, EN_BLOG_NEW = 'en/blogue/', 'en/blog/'
# Article EN resté avec son slug français
EN_ARTICLE_RENAME = {
    'les-probiotiques-panacee-pour-l-obesite.html': 'probiotics-the-solution-to-obesity.html',
}

def old_en(fr):
    """Ancien chemin EN : le slug FR sous en/ (sauf exceptions déjà anglaises)."""
    en = EN_SLUGS[fr]
    if fr in ('meilleur-probiotique.html', 'privacy-policy.html', 'index.html', 'etudes.html'):
        return en
    return 'en/' + fr

def renames(root):
    """{ancien chemin EN: nouveau chemin EN} pour toutes les pages et articles."""
    out = {old_en(fr): en for fr, en in EN_SLUGS.items() if old_en(fr) != en}
    names = subprocess.run(['git', 'ls-tree', '--name-only', 'HEAD', EN_BLOG_OLD],
                           cwd=root, capture_output=True, text=True).stdout.split()
    for name in sorted(os.path.basename(n) for n in names if n.endswith('.html')):
        out[EN_BLOG_OLD + name] = EN_BLOG_NEW + EN_ARTICLE_RENAME.get(name, name)
    return out


if __name__ == '__main__':
    ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
    ORIGIN_RE = r'(?:https?://(?:www\.)?probaclac\.ca)'
    MAP = renames(ROOT)
    # versions « URL propre » (sans .html) des mêmes chemins
    CLEAN = {o[:-5]: n[:-5] for o, n in MAP.items()}
    CLEAN['en/blogue'] = 'en/blog'

    def rewrite_target(target, here_dir, new_dir):
        """Réécrit une cible de lien si elle vise une ancienne page EN. Garde son style."""
        m = re.match(r'^([^?#]*)([?#].*)?$', target, re.S)
        path, tail = m.group(1), m.group(2) or ''
        if not path:
            return target
        am = re.match(ORIGIN_RE + r'(/.*)?$', path)
        if am:                                   # absolu probaclac.ca
            p = (am.group(1) or '/').lstrip('/')
            pre = path[:len(path) - len(am.group(1) or '')]
            key = p.rstrip('/')
            if key.endswith('.html') and key in MAP:
                return pre + '/' + MAP[key] + tail
            if key in CLEAN:
                return pre + '/' + CLEAN[key] + ('/' if p.endswith('/') else '') + tail
            return target
        if path.startswith('/'):                  # racine du site
            key = path.lstrip('/').rstrip('/')
            if key in MAP:   return '/' + MAP[key] + tail
            if key in CLEAN: return '/' + CLEAN[key] + tail
            return target
        if re.match(r'^[a-z]+:', path) or '${' in path:   # mailto:, autre domaine, gabarit JS
            return target
        if not path.endswith('.html'):
            return target
        resolved = os.path.normpath(os.path.join(here_dir, path)).replace(os.sep, '/')
        if resolved not in MAP:
            return target
        new = os.path.relpath(MAP[resolved], new_dir or '.').replace(os.sep, '/')
        return new + tail

    # 1 · renommer (git mv pour que l'historique suive; os.rename si non suivi)
    def mv(old, new):
        o, n = os.path.join(ROOT, old), os.path.join(ROOT, new)
        if not os.path.exists(o):
            return
        os.makedirs(os.path.dirname(n), exist_ok=True)
        if subprocess.run(['git', 'mv', old, new], cwd=ROOT, capture_output=True).returncode:
            os.rename(o, n)
    for old, new in MAP.items():
        mv(old, new)
    mv(EN_BLOG_OLD + '_src', EN_BLOG_NEW + '_src')
    for o, n in EN_ARTICLE_RENAME.items():
        mv(EN_BLOG_NEW + '_src/' + o[:-5] + '.txt', EN_BLOG_NEW + '_src/' + n[:-5] + '.txt')
    if os.path.isdir(os.path.join(ROOT, EN_BLOG_OLD)) and not os.listdir(os.path.join(ROOT, EN_BLOG_OLD)):
        os.rmdir(os.path.join(ROOT, EN_BLOG_OLD))

    # 2 · réécrire les liens de toutes les pages (après renommage : on lit le nouvel emplacement)
    INV = {n: o for o, n in MAP.items()}
    files = [f for f in glob.glob(f'{ROOT}/**/*.html', recursive=True)
             if '/assets/' not in f.replace(os.sep, '/') and '/adultes-stitch/' not in f]
    changed = 0
    for f in files:
        rel = os.path.relpath(f, ROOT).replace(os.sep, '/')
        # Les liens relatifs se résolvent depuis l'ANCIEN dossier du fichier. Le nouveau
        # dossier a la même profondeur (en/blogue → en/blog), donc les liens vers des
        # pages non renommées restent justes tels quels.
        here = os.path.dirname(INV.get(rel, rel))
        h = open(f, encoding='utf-8').read()
        # toute valeur de lien : attributs HTML (href, src, content…) et clés JS (url: "…")
        h2 = re.sub(r'''((?:href|src|content|action|url|data-[\w-]+)\s*[=:]\s*)(["'])([^"'<>\n]*?)\2''',
                    lambda m: m.group(1) + m.group(2) + rewrite_target(m.group(3), here, os.path.dirname(rel)) + m.group(2),
                    h)
        if h2 != h:
            open(f, 'w', encoding='utf-8').write(h2)
            changed += 1
    print(f'{len(MAP)} fichiers renommés · liens réécrits dans {changed} pages')

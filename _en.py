# -*- coding: utf-8 -*-
import re
# ---- shared FR->EN chrome replacements ----
CH=[
('<html lang="fr">','<html lang="en">'),
('<title>Probaclac — Probiotiques de grade pharmaceutique</title>','<title>Probaclac — Pharmaceutical-grade probiotics</title>'),
('<meta name="description" content="12 formules de probiotiques, formulées au Québec, validées par la science.">','<meta name="description" content="12 probiotic formulas, made in Quebec, validated by science.">'),
# nav
('Nos produits<span class="chev"','Our products<span class="chev"'),
('À propos des probiotiques<span class="chev"','Information<span class="chev"'),
('<a href="https://etudes.probaclac.ca/">Études</a>','<a href="https://etudes.probaclac.ca/studies">Studies</a>'),
('<a href="blogue.html">Blogue</a>','<a href="blogue.html">Blog</a>'),
# mega left
('<h3>12 formules, conçues au milliard près.</h3>','<h3>12 formulas, engineered to the billion.</h3>'),
('aria-selected="true">Toutes</button>','aria-selected="true">All</button>'),
('aria-selected="false">Quotidien</button>','aria-selected="false">Daily</button>'),
('aria-selected="false">Conditions ciblées</button>','aria-selected="false">Targeted conditions</button>'),
('aria-selected="false">Santé féminine</button>','aria-selected="false">Women’s health</button>'),
# mega help
('<h4>Trouvez la formule qui vous correspond.</h4>','<h4>Find the formula that fits you.</h4>'),
('<p>Un guide interactif vous aide à choisir selon votre âge, profil ou besoin.</p>','<p>An interactive guide helps you choose by age, profile or need.</p>'),
('          Choisir le bon probiotique\n','          Choosing the right probiotic\n'),
("<p>de diarrhée associée aux antibiotiques avec Probaclac Medic. <a href=\"https://etudes.probaclac.ca/\">Voir l'étude →</a></p>",
 '<p>reduction in antibiotic-associated diarrhea with Probaclac Medic. <a href="https://etudes.probaclac.ca/studies">See the study →</a></p>'),
# about mega
('aria-label="À propos des probiotiques" hidden','aria-label="Information" hidden'),
('<div class="eyebrow"><span class="dot"></span>À propos des probiotiques</div>','<div class="eyebrow"><span class="dot"></span>Information</div>'),
('<h3>Comprendre avant de choisir.</h3>','<h3>Understand before choosing.</h3>'),
('<p>Guides et références pour démystifier le microbiote et trouver la formule qui correspond à votre besoin.</p>','<p>Guides and references to demystify the microbiota and find the formula that fits your need.</p>'),
('<span class="title">Choisir le bon probiotique</span>','<span class="title">Choosing the right probiotic</span>'),
('<span class="desc">Un guide interactif de deux questions, selon votre âge ou votre condition.</span>','<span class="desc">A two-question interactive guide, based on your age or condition.</span>'),
('<span class="title">Le microbiote humain</span>','<span class="title">Human Microbiota</span>'),
('<span class="desc">Cinq microflores, un même écosystème — zone par zone, espèces et pathogènes.</span>','<span class="desc">Five microflora, one ecosystem — zone by zone, species and pathogens.</span>'),
('<span class="title">Diarrhée du voyageur</span>',"<span class=\"title\">Traveler's diarrhea</span>"),
('<span class="desc">Comment éviter la tourista — zones à risque, symptômes et prévention.</span>','<span class="desc">How to avoid traveler’s diarrhea — risk zones, symptoms and prevention.</span>'),
# comp labels
('<h2 class="comp__title">Ingrédients médicinaux</h2>','<h2 class="comp__title">Medicinal ingredients</h2>'),
('<div class="comp__caphdr">par capsule</div>','<div class="comp__caphdr">per capsule</div>'),
('<h3>Posologie</h3>','<h3>Dosage</h3>'),
('<h3>Ingrédients non-médicinaux</h3>','<h3>Non-medicinal ingredients</h3>'),
('Voir nos études<span class="arr">','See our studies<span class="arr">'),
# badges
('<span>Sans gluten</span>','<span>Gluten Free</span>'),
('<span>Sans soya</span>','<span>Soy Free</span>'),
('<span>Sans protéines laitières</span>','<span>No milk proteins</span>'),
('<span>Capsules végétales</span>','<span>Vegetable capsules</span>'),
# spec labels
('<dt>Formule</dt>','<dt>Formula</dt>'),
('<dt>Formats disponibles</dt>','<dt>Available formats</dt>'),
# allergens section
('<h2>Probiotiques sans allergènes</h2>','<h2>Allergen-free probiotics</h2>'),
("<p>Probaclac est fier d'offrir des probiotiques sans allergènes*. Tout au long de la production, les allergènes alimentaires prioritaires sont évités.</p>",
 '<p>Probaclac is proud to offer allergen-free* probiotics. Throughout the production of probiotics priority food allergens are avoided.</p>'),
("<p>Nous sommes engagés à fournir des suppléments adaptés à tous, peu importe la sensibilité. Probaclac est la référence pour des probiotiques sans protéines laitières, sans gluten, sans soya et sans tous les allergènes classiques.</p>",
 '<p>We are committed to providing supplements that are suitable for everyone, regardless of sensitivity. Probaclac is the reference for probiotics without dairy proteins, gluten, soy and all classic allergens.</p>'),
("<p class=\"small\">*Probaclac Croquable pour enfants peut contenir des traces de protéines laitières. Probaclac Medic peut contenir des traces de soya.</p>",
 '<p class="small">*Probaclac Chewable for children may contain traces of milk proteins. Probaclac Medic may contain traces of soy.</p>'),
# CTA conservation cols
('<div>Ne nécessite pas de réfrigération</div>','<div>Does not require refrigeration</div>'),
('<div>Conserver dans un endroit à l’abri de l’humidité</div>','<div>Store in a place protected from humidity</div>'),
('<div>Prendre après le repas pour une assimilation améliorée</div>','<div>Take after meals for improved assimilation</div>'),
('<div>S’il y a prise d’antibiotiques, prendre au moins 2 heures après la prise d’antibiotiques</div>','<div>If taking antibiotics, take at least 2 hours after taking antibiotics</div>'),
('href="https://www.monprobiotique.ca">Voir au magasin en ligne','href="https://myprobiotics.com/">Shop online'),
# footer
('<h5>Nos produits</h5>','<h5>Our products</h5>'),
('<a href="probiotique-adulte.html">Adultes</a>','<a href="probiotique-adulte.html">Adults</a>'),
('<a href="probiotique-50-et-plus.html">50 ans et +</a>','<a href="probiotique-50-et-plus.html">50+</a>'),
('<a href="probiotique-voyage.html">Voyageurs</a>','<a href="probiotique-voyage.html">Travelers</a>'),
('<a href="probiotique-colon-irritable.html">Côlon irritable</a>','<a href="probiotique-colon-irritable.html">IBS</a>'),
('<a href="probiotique-bebes.html">Enfants 1 à 3 ans</a>','<a href="probiotique-bebes.html">Toddlers</a>'),
('<a href="probiotique-enfant.html">Croquable</a>','<a href="probiotique-enfant.html">Chewable</a>'),
('<a href="probiotique-extra-fort.html">Extra-fort</a>','<a href="probiotique-extra-fort.html">Extra-Strength</a>'),
('<a href="probiotique-antibiotique.html">Medic</a>','<a href="probiotique-antibiotique.html">Medic</a>'),
('<a href="probiotique-gastro-intestinal.html">Gastro intestinal</a>','<a href="probiotique-gastro-intestinal.html">GI</a>'),
('<a href="probiotique-vaginal.html">Vaginose bactérienne</a>','<a href="probiotique-vaginal.html">Bacterial vaginosis</a>'),
('<a href="probiotique-infection-a-levure.html">Infection à levure</a>','<a href="probiotique-infection-a-levure.html">Yeast infection</a>'),
('<a href="probiotique-infection-urinaire.html">Infection urinaire</a>','<a href="probiotique-infection-urinaire.html">Urinary tract infection</a>'),
('Soutenez votre santé intestinale.','Support your intestinal health.'),
('>Questions fréquentes</div>','>Frequently asked questions</div>'),

('<h5>Nous joindre</h5>','<h5>Contact us</h5>'),
('Tél.&nbsp;','Tel.&nbsp;'),
('Tél. ','Tel. '),
('>Tél.','>Tel.'),

('31 Rue Gaston-Dumoulin, suite 103','31 Gaston-Dumoulin street, suite 103'),
('<h5>À propos</h5>','<h5>Information</h5>'),
('>Choisir le bon probiotique</a>','>Choosing the right probiotic</a>'),
('>Le microbiote humain</a>','>Human Microbiota</a>'),
('>Diarrhée du voyageur</a>',">Traveler's diarrhea</a>"),
('https://www.probaclac.ca/microbiote-probiotiques','https://www.probaclac.ca/en/microbiote-probiotiques'),
('https://www.probaclac.ca/diarrhee-du-voyageur','https://www.probaclac.ca/en/diarrhee-du-voyageur'),
('https://etudes.probaclac.ca/choisir.html','https://etudes.probaclac.ca/choose.html'),
('<a href="https://etudes.probaclac.ca" style="display:block;padding:.26rem 0;font-size:.92rem;">Études</a>','<a href="https://etudes.probaclac.ca/studies" style="display:block;padding:.26rem 0;font-size:.92rem;">Studies</a>'),
("<p class=\"pbl-foot__partner\">Fier partenaire d'Allergies Québec.</p>",'<p class="pbl-foot__partner">Proud partner of Allergies Québec.</p>'),
('>Politique de confidentialité</a>','>Privacy policy</a>'),
('https://www.probaclac.ca/privacy-policy','https://www.probaclac.ca/en/privacy-policy'),
('<span>Site web : <a','<span>Website: <a'),
]
EN_CAT='''const CATALOGUE = [
  {n:"01", cat:"qd", catLabel:"Daily",              name:"Adults",               meta:"7 strains · 6.5 billion CFU",          npn:"NPN 80013765", url:"probiotique-adulte.html",              img: T+"adultes.webp"},
  {n:"02", cat:"qd", catLabel:"Daily",              name:"50+",                  meta:"7 strains · 8.5 billion CFU",          npn:"NPN 80013814", url:"probiotique-50-et-plus.html",          img: T+"50plus.webp"},
  {n:"03", cat:"qd", catLabel:"Daily",              name:"Travelers",            meta:"9 strains + vitamin C",                npn:"NPN 80108358", url:"probiotique-voyage.html",              img: T+"voyage.webp"},
  {n:"04", cat:"qd", catLabel:"Daily",              name:"Chewable",             meta:"Kids 3 years and up · 3 billion",      npn:"NPN 80106376", url:"probiotique-enfant.html",              img: T+"croquable.webp"},
  {n:"05", cat:"qd", catLabel:"Daily",              name:"Toddlers",             meta:"Openable capsules · 2 billion",        npn:"NPN 80083662", url:"probiotique-bebes.html",               img: T+"enfants.webp"},
  {n:"06", cat:"cd", catLabel:"Targeted conditions", name:"IBS",                 meta:"IBS · 10 billion CFU",                 npn:"NPN 80140258", url:"probiotique-colon-irritable.html",     img: T+"sci.webp"},
  {n:"07", cat:"cd", catLabel:"Targeted conditions", name:"GI",                  meta:"Antibiotic therapy · 15 billion",      npn:"NPN 80083663", url:"probiotique-gastro-intestinal.html",   img: T+"gi.webp"},
  {n:"08", cat:"cd", catLabel:"Targeted conditions", name:"Medic",               meta:"During antibiotics · 5 billion",       npn:"NPN 80013796", url:"probiotique-antibiotique.html",        img: T+"medic.webp"},
  {n:"09", cat:"cd", catLabel:"Targeted conditions", name:"Extra-Strength",      meta:"8 strains · 10.5 billion",             npn:"NPN 80013798", url:"probiotique-extra-fort.html",          img: T+"extra.webp"},
  {n:"10", cat:"fm", catLabel:"Women’s health",     name:"Bacterial vaginosis",  meta:"3 strains · intravaginal",             npn:"NPN 80041302", url:"probiotique-vaginal.html",             img: T+"../mainvaginal.avif"},
  {n:"11", cat:"fm", catLabel:"Women’s health",     name:"Yeast infection",      meta:"Candidiasis · Rosella strain",         npn:"NPN 80136249", url:"probiotique-infection-a-levure.html",  img: T+"rosella.webp"},
  {n:"12", cat:"fm", catLabel:"Women’s health",     name:"Urinary tract infection", meta:"9 strains + cranberry",             npn:"NPN 80066788", url:"probiotique-infection-urinaire.html",  img: T+"canneberge.webp"},
];'''

def chrome(s):
    for a,b in CH:
        s=s.replace(a,b)
    # catalogue
    s=re.sub(r'const CATALOGUE = \[.*?\];', lambda m: EN_CAT.replace('\\','\\\\'), s, count=1, flags=re.S)
    # assets path (pages are in en/ subfolder)
    s=s.replace('"assets/','"../assets/').replace("'assets/","'../assets/")
    # strain ufc values FR->EN
    s=re.sub(r'(\d+),(\d+) milliards? ufc', lambda m: f'{m.group(1)}.{m.group(2)} billion cfu', s)
    s=re.sub(r'(\d+) milliards? ufc', r'\1 billion cfu', s)
    s=re.sub(r'(\d+) millions? ufc', r'\1 million cfu', s)
    return s

def build(src, out, body, forwhom=None):
    s=open(src,encoding='utf-8').read()
    s=chrome(s)
    miss=[]
    for a,b in body:
        if a in s: s=s.replace(a,b,1)
        else: miss.append(a[:55])
    if forwhom:
        new_s,n=re.subn(r'<h2 class="shead__title".*?</p>\s*</div>', forwhom.replace("\\","\\\\"), s, count=1, flags=re.S)
        if n==0: miss.append('FORWHOM-BLOCK')
        else: s=new_s
    open('en/'+out,'w',encoding='utf-8').write(s)
    if miss: print(out,'MISSES:',miss)
    else: print(out,'OK')

if __name__=='__main__':
    pass

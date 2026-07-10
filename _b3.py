# -*- coding: utf-8 -*-
import _gen
def hero(i): return f"https://static.wixstatic.com/media/{i}~mv2.jpg/v1/fill/w_900,h_900,al_c,q_85,enc_avif,quality_auto/p.jpg"
def png(i): return f"https://static.wixstatic.com/media/{i}~mv2.png"
G=_gen.STD_BADGES[0]; S=_gen.STD_BADGES[1]

P=[
{
 'slug':'probiotique-enfant','name':'Croquable','title':'Probiotique Croquable — Probaclac',
 'hero_img':hero('623234_d1e3a4f56c7e4013b560d97c6b54d607'),'h1':"Dès l'âge de 3 ans, croquable à saveur de petits fruits",
 'formule':'Enfants 3 ans et plus','formats':'40 / 75 comprimés','npn':'80106376',
 'desc':"Contribue à soutenir les fonctions immunitaires et à maintenir votre santé gastro-intestinale avec ce probiotique à croquer, regroupant <b>5 souches</b> soigneusement sélectionnées. Sa formule, composée de Bifidobactéries (côlon) et de Lactobacilles (intestin grêle), assure une couverture optimale de l'ensemble du tractus intestinal. Chaque comprimé croquable contient <b>3 milliards de cellules actives</b>, jusqu'à la date de péremption. Ne nécessite aucune réfrigération.",
 'badges':[G,S],
 'strains':[
  ("Lacticaseibacillus paracasei","NL-211","2,1 milliards ufc"),
  ("Lacticaseibacillus rhamnosus","NL-228","600 millions ufc"),
  ("Bifidobacterium longum","NL-235","207 millions ufc"),
  ("Bifidobacterium breve","NL-240","90 millions ufc"),
  ("Lactobacillus acidophilus","NL-214","3 millions ufc"),
  ("Vitamine C","","15 mg","noital"),
 ],
 'nonmed':"Sorbitol, xylitol, inuline, cellulose microcristalline, extrait de levure, maltodextrine, tréhalose, concentré de jus de betterave, saveur de baies, stéarate de magnésium, dioxyde de silicium, acide citrique.",
 'posology':"<p>Prendre un comprimé deux fois par jour, au déjeuner et au souper. Prendre 2 à 3 heures avant ou après la prise d'antibiotiques.</p>\n          <p><b>Mode d'emploi :</b> pour enfants de 3 ans et plus, dissoudre ou écraser les comprimés afin de prévenir l'étouffement.</p>",
 'stat':None,'shield_img':png('623234_b46b34c9f86a4c35b9708671406e569e'),
 'forwhom_title':"Probaclac maintient la santé des enfants.",
 'forwhom_ps':[
  "Les tout-petits méritent tout le soutien nécessaire pour grandir en santé, y compris un apport en bonnes bactéries. Leur curiosité naturelle et leurs interactions avec d'autres enfants les exposent davantage aux infections.",
  "Dès l'âge de 3 ans, renforcez leur système digestif, immunitaire, respiratoire et urinaire avec des souches probiotiques humaines adaptées. Notre comprimé croquable, faible en sucre et sans agent artificiel, a bon goût et est friable pour l'ajouter aux aliments ou aux breuvages.",
 ],
},
{
 'slug':'probiotique-extra-fort','name':'Extra-fort','title':'Probiotique Extra-fort — Probaclac',
 'hero_img':hero('623234_3c64e30ea6294c0091be12b94743e304'),'h1':'Pour les problèmes aigus au niveau des intestins',
 'formule':'Extra-fort','formats':'45 capsules','npn':'80013798',
 'desc':"Contribue à restaurer l'équilibre de votre flore intestinale avec ce complexe probiotique multi-souches, regroupant <b>8 souches</b> soigneusement sélectionnées. Sa formule assure une couverture optimale du tractus intestinal et favorise un rééquilibrage rapide du microbiote. Chaque capsule contient <b>10,5 milliards de cellules actives</b>, jusqu'à la date de péremption. Ne nécessite aucune réfrigération.",
 'strains':[
  ("Lacticaseibacillus rhamnosus","NL-228","3 milliards ufc"),
  ("Bifidobacterium bifidum","NL-236","2 milliards ufc"),
  ("Lactobacillus acidophilus","NL-214","2 milliards ufc"),
  ("Bifidobacterium breve","NL-240","1 milliard ufc"),
  ("Bifidobacterium longum","NL-235","1 milliard ufc"),
  ("Lacticaseibacillus paracasei","NL-211","1 milliard ufc"),
  ("Streptococcus thermophilus","NL-231","490 millions ufc"),
  ("Lactobacillus bulgaricus","NL-287","10 millions ufc"),
 ],
 'nonmed':"Maltodextrine, capsules végétales (hypromellose), inuline, stéarate de magnésium, acide ascorbique.",
 'posology':"<p><b>Adolescents (12 ans et plus) et adultes :</b> prendre une capsule deux fois par jour, au déjeuner et au souper.</p>\n          <p>Prendre au moins 2 à 3 heures avant ou après la prise d'antibiotiques.</p>",
 'stat':None,'shield_img':png('623234_449a15e9fb3b4971a31217576162a682'),
 'forwhom_title':"Probaclac maintient votre santé digestive.",
 'forwhom_ps':[
  "Les situations médicales et personnelles de la vie peuvent mettre à l'épreuve votre système immunitaire et votre santé digestive. Le lien entre le cerveau et les intestins est indéniable : les fonctions cognitives affectent les fonctions digestives, et vice versa.",
  "Notre formule puissante et complète contient 10,5 milliards de bactéries actives et pas moins de 8 souches humaines différentes. Elle agit rapidement contre les problèmes aigus grâce à sa forte concentration, et s'avère très efficace dans les cas d'antibiothérapie.",
 ],
},
]
for p in P: _gen.gen(p)

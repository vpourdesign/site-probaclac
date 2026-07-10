# -*- coding: utf-8 -*-
import _gen
def hero(i): return f"https://static.wixstatic.com/media/{i}~mv2.jpg/v1/fill/w_900,h_900,al_c,q_85,enc_avif,quality_auto/p.jpg"
def png(i): return f"https://static.wixstatic.com/media/{i}~mv2.png"

P=[
{
 'slug':'probiotique-colon-irritable','name':'Côlon irritable','title':'Probiotique Côlon irritable (SCI) — Probaclac',
 'hero_img':hero('623234_31f03188e94c40d5b213b432ad847171'),'h1':'Syndrome du côlon irritable',
 'formule':'SCI / IBS','formats':'45 capsules','npn':'80140258',
 'desc':"Contribue à soulager les symptômes du Syndrome du côlon irritable (SCI). Son complexe ciblé aide à réduire les gaz, les ballonnements, ainsi que les inconforts liés à la diarrhée et à la constipation. Chaque capsule renferme <b>10 milliards de cellules actives</b>, jusqu'à la date de péremption, pour un soutien efficace et constant. Conçu pour agir directement là où vous en avez besoin, ce probiotique vous accompagne au quotidien pour favoriser un mieux-être intestinal. Ne nécessite aucune réfrigération.",
 'strains':[("Lacticaseibacillus paracasei","HA-196","10 milliards ufc")],
 'nonmed':"Maltodextrine, capsule végétale (hypromellose), stéarate de magnésium, acide ascorbique.",
 'posology':"<p><b>Adultes :</b> prendre une capsule une fois par jour.</p>\n          <p>Prendre au moins 2 à 3 heures avant ou après la prise d'antibiotiques.</p>",
 'stat':None,'shield_img':png('623234_6f5f97bceff741be949e264710ccc5b8'),
 'forwhom_title':"Probaclac SCI vous accompagne au quotidien.",
 'forwhom_ps':[
  "Saviez-vous que le Canada présente l'un des taux les plus élevés de syndrome du côlon irritable (SCI) au monde, estimé à 18 % contre 11 % dans le monde ? Vivre au quotidien avec le SCI a un impact significatif sur la qualité de vie et peut devenir une source de stress et d'anxiété.",
  "Notre formule SCI est adaptée spécifiquement pour soulager les symptômes : douleurs et crampes abdominales, ballonnements, constipation et/ou diarrhée en alternance. En complément : faire de l'exercice, adopter une bonne hygiène de sommeil et diminuer les sources de stress.",
 ],
},
{
 'slug':'probiotique-bebes','name':'Enfants 1 à 3 ans','title':'Probiotique Enfants 1 à 3 ans — Probaclac',
 'hero_img':hero('623234_f7d1e9ca8c64485f892c5d6f45d3fabb'),'h1':"Capsules ouvrables pour enfants d'un an et plus",
 'formule':'Enfants 1 an et plus','formats':'40 capsules','npn':'80083662',
 'desc':"Contribue à soutenir la santé gastro-intestinale de votre enfant et à contrôler la diarrhée infectieuse aiguë avec ce complexe probiotique multi-souches, regroupant <b>5 souches</b> soigneusement sélectionnées. Sa formule, composée de Bifidobactéries (côlon) et de Lactobacilles (intestin grêle), assure une couverture optimale de l'ensemble du tractus intestinal. Chaque capsule contient <b>2 milliards de cellules actives</b>, jusqu'à la date de péremption. Ne nécessite aucune réfrigération.",
 'strains':[
  ("Lacticaseibacillus rhamnosus","GG","1 milliard ufc"),
  ("Bifidobacterium bifidum","NL-236","300 millions ufc"),
  ("Bifidobacterium infantis","NL-244","300 millions ufc"),
  ("Lactobacillus acidophilus","NL-214","300 millions ufc"),
  ("Limosilactobacillus reuteri","NL-219","100 millions ufc"),
 ],
 'nonmed':"Maltodextrine, capsules végétales (hypromellose), inuline, stéarate de magnésium, acide ascorbique.",
 'posology':"<p><b>Enfants 1 an et plus :</b> prendre une capsule une fois par jour. Prendre au moins 2 à 3 heures avant ou après la prise d'antibiotiques.</p>\n          <p><b>Mode d'emploi :</b> ouvrir la capsule, mélanger la poudre à un aliment et s'assurer de sa consommation en totalité.</p>",
 'stat':None,'shield_img':png('623234_85b873c9680949899a17031b4d5104c6'),
 'forwhom_title':"Probaclac maintient la santé de vos enfants.",
 'forwhom_ps':[
  "Il est très important d'incorporer au quotidien des probiotiques aux enfants dès le bas âge afin de leur permettre d'avoir une flore intestinale complète et un système digestif en bonne santé.",
  "Cette formule spécifique aux jeunes enfants est offerte sous forme de capsules ouvrables, permettant d'incorporer les bonnes bactéries à n'importe quel aliment ou breuvage — il suffit d'ouvrir la capsule et de saupoudrer les probiotiques sur la nourriture.",
 ],
},
]
for p in P: _gen.gen(p)

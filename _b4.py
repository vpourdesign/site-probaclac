# -*- coding: utf-8 -*-
import _gen
def hero(i): return f"https://static.wixstatic.com/media/{i}~mv2.jpg/v1/fill/w_900,h_900,al_c,q_85,enc_avif,quality_auto/p.jpg"
def png(i): return f"https://static.wixstatic.com/media/{i}~mv2.png"
P=[
{
 'slug':'probiotique-antibiotique','name':'Medic','title':'Probiotique Medic — Probaclac',
 'hero_img':hero('623234_f5c63088066d4f92b27cf3aa2e65e228'),'h1':"Réduit le risque de diarrhée durant l'antibiothérapie",
 'formule':'Medic','formats':'20 capsules','npn':'80013796',
 'desc':"Contribue à protéger votre microbiote lors de traitements antibiotiques avec ce complexe probiotique, regroupant <b>1 souche</b> (<span class=\"italic\">Saccharomyces boulardii</span>) soigneusement sélectionnée. Son action antimicrobienne aide à prévenir la diarrhée associée aux antibiotiques et à lutter contre les infections nosocomiales comme <span class=\"italic\">Clostridium difficile</span> et <span class=\"italic\">Escherichia coli</span>. Chaque capsule contient <b>5 milliards de cellules actives</b>, jusqu'à la date de péremption. Ne nécessite aucune réfrigération.",
 'strains':[("Saccharomyces boulardii","","5 milliards ufc")],
 'nonmed':"Maltodextrine, capsules végétales (hypromellose), stéarate de magnésium, acide ascorbique.",
 'posology':"<p><b>Enfants (6 ans et plus), adolescents (12 ans et plus) et adultes :</b> prendre une capsule deux fois par jour, au déjeuner et au souper.</p>\n          <p>Prendre simultanément avec la prise d'antibiotiques. Prendre au moins 2 à 3 heures avant ou après la prise d'antifongiques.</p>",
 'stat':'<b>−86&nbsp;%</b> de diarrhée associée aux antibiotiques avec Probaclac Medic',
 'shield_img':png('623234_8966fbc38d77481bb5d85d60283af9ee'),
 'forwhom_title':"Probaclac vous accompagne pendant votre antibiothérapie.",
 'forwhom_ps':[
  "Les traitements antibiotiques, bien qu'efficaces, ne font pas de distinction entre les bonnes et les mauvaises bactéries, affectant l'équilibre global de votre microbiote — ce qui peut entraîner des épisodes de diarrhée.",
  "Le probiotique Medic contient la levure <span class=\"italic\">Saccharomyces boulardii</span> à raison de 5 milliards de cellules actives par capsule. Comme elle n'est pas affectée par les antibiotiques, ils forment ensemble une équipe redoutable contre les bactéries pathogènes, et elle aide à lutter contre <span class=\"italic\">Clostridium difficile</span> et <span class=\"italic\">Escherichia coli</span>.",
 ],
},
{
 'slug':'probiotique-gastro-intestinal','name':'Gastro-Intestinal','title':'Probiotique Gastro-Intestinal — Probaclac',
 'hero_img':hero('623234_d7b0658893914abc9ae5d5275c0c2f41'),'h1':"Réduit le risque de diarrhée lors de la prise d'antibiotiques",
 'formule':'Probaclac GI','formats':'15 capsules','npn':'80083663',
 'desc':"Contribue à soutenir votre santé intestinale durant une antibiothérapie avec ce complexe probiotique multi-souches, regroupant <b>5 souches</b> soigneusement sélectionnées, dont <span class=\"italic\">Lactobacillus rhamnosus</span> GG, l'une des souches les plus étudiées au monde. Chaque capsule contient <b>15 milliards de cellules actives</b>, jusqu'à la date de péremption. Ne nécessite aucune réfrigération.",
 'strains':[
  ("Lacticaseibacillus rhamnosus","GG","10 milliards ufc"),
  ("Bifidobacterium longum","NL-235","2 milliards ufc"),
  ("Lacticaseibacillus paracasei","NL-211","2 milliards ufc"),
  ("Bifidobacterium breve","NL-240","600 millions ufc"),
  ("Bifidobacterium bifidum","NL-236","400 millions ufc"),
 ],
 'nonmed':"Maltodextrine, capsules végétales (hypromellose), inuline, stéarate de magnésium, acide ascorbique.",
 'posology':"<p><b>Adolescents (12 ans et plus) et adultes :</b> prendre une capsule deux fois par jour, 2 heures après la prise de l'antibiotique durant tout le traitement.</p>\n          <p>Continuer 3 à 5 jours après la fin du traitement antibiotique.</p>",
 'stat':None,'shield_img':png('623234_83be60d2f5084fc38ff5429c6d4be9ac'),
 'forwhom_title':"Probaclac GI vous accompagne durant votre antibiothérapie.",
 'forwhom_ps':[
  "L'antibiothérapie détruit non seulement les mauvaises bactéries, mais aussi les bonnes, causant les troubles communément appelés « diarrhée liée aux antibiotiques » et une flore débalancée. Il est important de la repeupler à l'aide de bonnes bactéries.",
  "Probaclac GI contient la souche <span class=\"italic\">Lactobacillus rhamnosus</span> GG, l'une des plus étudiées au monde. Avec 15 milliards de bactéries par capsule, 3 souches de Lactobacilles et 2 de Bifidobactéries, il est votre meilleur allié lors de votre prochaine antibiothérapie.",
 ],
},
]
for p in P: _gen.gen(p)

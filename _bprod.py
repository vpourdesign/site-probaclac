# -*- coding: utf-8 -*-
import _en

def fw(title,paras):
    h='<h2 class="shead__title" style="margin:0 0 1.1rem;">%s</h2>\n        '%title
    h+='\n        '.join('<p class="mute">%s</p>'%p for p in paras)
    return h+'\n      </div>'

# ---------- 50+ ----------
b50=[
('<h1>Pour un usage quotidien 50+</h1>','<h1>Probaclac Adults 50+</h1>'),
('<dd>50 ans et plus</dd>','<dd>50 years and over</dd>'),
('<p class="pbl-desc">Contribue à soutenir votre santé gastro-intestinale avec ce complexe probiotique multi-souches conçu pour les 50 ans et plus. Sa formule associe Bifidobactéries (côlon) et Lactobacilles (intestin grêle) et inclut <b>7 souches</b> spécifiques pour compenser la baisse naturelle des bifidobactéries. Chaque capsule fournit <b>8,5 milliards de cellules actives</b>, dont 60 % de Bifidobactéries (4,8 milliards), garantie jusqu\'à la date de péremption. Ne nécessite aucune réfrigération.</p>',
 '<p class="pbl-desc">Helps support your gastrointestinal health with this multi-strain probiotic complex, specially designed for individuals aged 50 and over. Its formula combines Bifidobacteria (colon) and Lactobacilli (small intestine) and includes <b>7 specific strains</b> to compensate for the natural decline of Bifidobacteria. Each capsule provides <b>8.5 billion active cells</b>, including 60% Bifidobacteria (4.8 billion), guaranteed until the expiration date. No refrigeration required.</p>'),
('<p class="nonmed">Maltodextrine, capsules végétales (hypromellose), inuline, stéarate de magnésium, acide ascorbique.</p>',
 '<p class="nonmed">Maltodextrin, vegetable capsules (hypromellose), inulin, magnesium stearate, ascorbic acid.</p>'),
('<p><b>Adultes :</b> prendre une capsule deux fois par jour, au déjeuner et au souper.</p>',
 '<p><b>Adults:</b> Take one capsule twice daily at breakfast and dinner.</p>'),
('<p>Prendre au moins 2 à 3 heures avant ou après la prise d\'antibiotiques.</p>',
 '<p>Take at least 2 to 3 hours before or after taking antibiotics.</p>'),
]
fw50=_en.__dict__  # noop
forwhom50=fw('Probaclac maintains your health.',[
'Any adult who has previously taken antibiotics, experiences digestive issues (such as bloating, constipation and/or diarrhea) or intestinal problems (such as Crohn\'s disease or irritable bowel syndrome), or is prone to infections would benefit from taking probiotics to maintain their health.',
'In addition, environmental changes (food processing, air pollution and hectic lifestyle) affect the balance of the intestinal microbiota and thus compromise protection against pathogenic bacteria.',
'Our 50+ probiotic offers a concentration of 8.5 billion active cells per capsule, specially designed to meet the specific needs linked to the natural decline of certain bacteria with age.',
'People aged 50 and over can benefit greatly from probiotic supplementation, helping to rebalance the good bacteria essential for well-being.',
'<b>Probaclac supports you throughout your life.</b> The blend of strains in the product helps prevent diarrhea and constipation while strengthening the immune system later in life.',
'Due to its high proportion of Bifidobacteria, this supplement is also beneficial for individuals experiencing malabsorption (in cases of allergies or intolerances) and/or colon-related issues such as Crohn\'s disease or irritable bowel syndrome.',
])
_en.build('probiotique-50-et-plus.html','probiotique-50-et-plus.html',b50,forwhom50)

# ---------- VOYAGE ----------
bvoy=[
('<h1>Réduit les risques de diarrhée du voyageur</h1>','<h1>Reduces the risk of traveler’s diarrhea</h1>'),
('<dd>Probiotique voyageurs</dd>','<dd>Travelers probiotic</dd>'),
('<p class="pbl-desc">Réduit les risques de diarrhée du voyageur et contribue à soutenir votre santé intestinale lors de vos déplacements avec ce complexe probiotique multi-souches, regroupant <b>9 souches</b> soigneusement sélectionnées. Sa formule, composée de souches naturelles dont <span class="italic">Lactobacillus plantarum</span> (anti-diarrhée), aide à diversifier votre microbiote et à mieux faire face aux bactéries pathogènes des autres régions du monde. Chaque capsule contient <b>6,5 milliards de cellules actives</b>, jusqu\'à la date de péremption. Ne nécessite aucune réfrigération.</p>',
 '<p class="pbl-desc">Helps support your intestinal health while traveling with this multi-strain probiotic and lactic ferment complex, containing <b>9 carefully selected strains</b>. Its formula, composed of Lactobacilli and Bifidobacteria, helps diversify your microbiota and better combat pathogenic bacteria from different regions of the world. Each capsule contains <b>6.5 billion active cells</b>, guaranteed until the expiration date. No refrigeration required.</p>'),
('<p class="nonmed">Extrait de levure, tréhalose, capsules végétales (hypromellose), stéarate de magnésium, maltodextrine.</p>',
 '<p class="nonmed">Yeast extract, trehalose, vegetable capsules (hypromellose), magnesium stearate, maltodextrin.</p>'),
('<p><b>Adolescents (12 ans et plus) et adultes :</b> prendre une capsule deux fois par jour, au déjeuner et au souper.</p>',
 '<p><b>Adolescents (12 years and up) and adults:</b> Take one capsule twice daily with breakfast and dinner.</p>'),
('<p>Prendre au moins 2 à 3 heures avant ou après la prise d\'antibiotiques ou antifongiques. Commencer 5 jours avant le voyage et continuer pendant toute sa durée.</p>',
 '<p>Take at least 2 to 3 hours before or after taking antibiotics or antifungals. Start 5 days before travel and continue for the duration of the trip.</p>'),
]
forwhomV=fw('Probaclac maintains your health while traveling.',[
'Planning a trip? You’ve mapped out your itinerary, packed your bags, and taken the necessary precautions for a safe journey.',
'Whether it\'s a leisure getaway or a business trip, be prepared by bringing probiotics specially designed for the occasion.',
'More than half of overseas travelers experience diarrhea, especially those visiting the Middle East, Asia, Africa, and Central or South America.',
'<b>Be Prepared!</b> A week before your departure, start taking Probaclac Travelers to prevent digestive issues.',
'Its multi-strain formula diversifies your bacterial profile, helping you better combat harmful bacteria from different regions of the world. Plus, it contains Lactobacillus plantarum, a strain known for its anti-diarrheal properties.',
'For those prone to constipation while traveling due to dehydration and prolonged sitting during transport, our supplement helps regulate intestinal transit to prevent any blockage.',
'Continue taking Probaclac Travelers throughout your trip and for a week after your return to maintain an optimal gut flora.',
])
_en.build('probiotique-voyage.html','probiotique-voyage.html',bvoy,forwhomV)

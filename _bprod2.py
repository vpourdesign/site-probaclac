# -*- coding: utf-8 -*-
import _en
def fw(title,paras):
    h='<h2 class="shead__title" style="margin:0 0 1.1rem;">%s</h2>\n        '%title
    h+='\n        '.join('<p class="mute">%s</p>'%p for p in paras)
    return h+'\n      </div>'

# ---- IBS ----
ibs=[
('<h1>Syndrome du côlon irritable</h1>','<h1>Irritable Bowel Syndrome</h1>'),
('<dd>SCI / IBS</dd>','<dd>IBS</dd>'),
('<p class="pbl-desc">Contribue à soulager les symptômes du Syndrome du côlon irritable (SCI). Son complexe ciblé aide à réduire les gaz, les ballonnements, ainsi que les inconforts liés à la diarrhée et à la constipation. Chaque capsule renferme <b>10 milliards de cellules actives</b>, jusqu\'à la date de péremption, pour un soutien efficace et constant. Conçu pour agir directement là où vous en avez besoin, ce probiotique vous accompagne au quotidien pour favoriser un mieux-être intestinal. Ne nécessite aucune réfrigération.</p>',
 '<p class="pbl-desc">Helps relieve symptoms of Irritable Bowel Syndrome (IBS). Its targeted complex helps reduce gas, bloating, and discomfort associated with diarrhea and constipation. Each capsule contains <b>10 billion active cells</b>, guaranteed until the expiry date, for effective and consistent support. Designed to act directly where you need it most, this probiotic supports your daily intestinal well-being. No refrigeration required.</p>'),
('<p class="nonmed">Maltodextrine, capsule végétale (hypromellose), stéarate de magnésium, acide ascorbique.</p>',
 '<p class="nonmed">Maltodextrin, vegetable capsules (hypromellose), inulin, magnesium stearate, ascorbic acid.</p>'),
('<p><b>Adultes :</b> prendre une capsule une fois par jour.</p>','<p><b>Adults:</b> Take one capsule one time per day.</p>'),
('<p>Prendre au moins 2 à 3 heures avant ou après la prise d\'antibiotiques.</p>','<p>Take at least 2 to 3 hours before or after taking antibiotics.</p>'),
]
fwibs=fw('Probaclac maintains your health.',[
"Any adult who has previously taken antibiotics, experiences digestive issues (such as bloating, constipation and/or diarrhea) or intestinal problems (such as Crohn's disease or irritable bowel syndrome), or is prone to infections would benefit from taking probiotics to maintain their health.",
"In addition, environmental changes (food processing, air pollution and hectic lifestyle) affect the balance of the intestinal microbiota and thus compromise protection against pathogenic bacteria.",
"<b>Why Probaclac Adult?</b> Taking Probaclac Adults twice daily, all year round, allows you to fully profit from the benefits of probiotics and will therefore help people who suffer from digestive disorders, people who are taking antibiotic treatment or simply those who want to have a healthy digestive system.",
"The Probaclac range of probiotics has been proven for over 20 years and used in hospitals, they are also recommended by pharmacists, doctors, nurses, nutritionists and other health professionals. The probiotic Probaclac adult is free of priority allergens and is therefore suitable for everyone.",
])
_en.build('probiotique-colon-irritable.html','probiotique-colon-irritable.html',ibs,fwibs)

# ---- BEBES (Kids/Toddlers) ----
beb=[
('<h1>Capsules ouvrables pour enfants d\'un an et plus</h1>','<h1>Sprinkle capsules for kids aged one year and older</h1>'),
('<dd>Enfants 1 an et plus</dd>','<dd>Children 1 year and older</dd>'),
('<dd>40 capsules</dd>','<dd>40 capsules (Sprinkle)</dd>'),
('<p class="pbl-desc">Contribue à soutenir la santé gastro-intestinale de votre enfant et à contrôler la diarrhée infectieuse aiguë avec ce complexe probiotique multi-souches, regroupant <b>5 souches</b> soigneusement sélectionnées. Sa formule, composée de Bifidobactéries (côlon) et de Lactobacilles (intestin grêle), assure une couverture optimale de l\'ensemble du tractus intestinal. Chaque capsule contient <b>2 milliards de cellules actives</b>, jusqu\'à la date de péremption. Ne nécessite aucune réfrigération.</p>',
 '<p class="pbl-desc">Helps support your child’s gastrointestinal health and control acute infectious diarrhea with this multi-strain probiotic and lactic ferment complex, containing <b>5 carefully selected strains</b>. Its formula, composed of Bifidobacteria, residents of the colon, and Lactobacilli, inhabitants of the small intestine, ensures optimal coverage of the entire intestinal tract. Each capsule contains <b>2 billion active cells</b>, guaranteed until the expiration date. No refrigeration required.</p>'),
('<p class="nonmed">Maltodextrine, capsules végétales (hypromellose), inuline, stéarate de magnésium, acide ascorbique.</p>',
 '<p class="nonmed">Maltodextrin, vegetable capsules (hypromellose), inulin, magnesium stearate, ascorbic acid.</p>'),
('<p><b>Enfants 1 an et plus :</b> prendre une capsule une fois par jour. Prendre au moins 2 à 3 heures avant ou après la prise d\'antibiotiques.</p>',
 '<p><b>Children 1 year and older:</b> Take one capsule once a day. Take at least 2-3 hours before or after antibiotics.</p>'),
('<p><b>Mode d\'emploi :</b> ouvrir la capsule, mélanger la poudre à un aliment et s\'assurer de sa consommation en totalité.</p>',
 '<p><b>Instructions for use:</b> Open one capsule and mix or sprinkle the powder with food, making sure the total content is ingested.</p>'),
]
fwbeb=fw("Probaclac maintains your children's health.",[
"Probaclac offers a brand-new formula for infants aged one year and older, allowing them to benefit from the advantages of Probaclac’s good bacteria.",
"It is very important to incorporate probiotics into a child's daily routine from an early age to help them develop a complete intestinal flora and maintain a healthy digestive system.",
"This new formula, specifically designed for young children, comes in openable capsules, allowing beneficial bacteria to be added to any food, beverage, or other type of nourishment.",
"Probiotics contribute to a more complete intestinal flora for your young children.",
"<b>How to take Probaclac Kids?</b> The Probaclac Children’s probiotic formula was designed to provide probiotics to young children.",
"The capsule can be opened, allowing the probiotics inside to be sprinkled onto any type of drink or food.",
])
_en.build('probiotique-bebes.html','probiotique-bebes.html',beb,fwbeb)

# -*- coding: utf-8 -*-
import _en
def fw(title,paras):
    h='<h2 class="shead__title" style="margin:0 0 1.1rem;">%s</h2>\n        '%title
    h+='\n        '.join('<p class="mute">%s</p>'%p for p in paras)
    return h+'\n      </div>'

# ---- CROQUABLE (Chewable) ----
cro=[
('<h1>Dès l\'âge de 3 ans, croquable à saveur de petits fruits</h1>','<h1>From the age of 3, chewable with a berry flavour</h1>'),
('<dd>Enfants 3 ans et plus</dd>','<dd>Chewable probiotic</dd>'),
('<dd>40 / 75 comprimés</dd>','<dd>40 / 75 tablets</dd>'),
('<p class="pbl-desc">Contribue à soutenir les fonctions immunitaires et à maintenir votre santé gastro-intestinale avec ce probiotique à croquer, regroupant <b>5 souches</b> soigneusement sélectionnées. Sa formule, composée de Bifidobactéries (côlon) et de Lactobacilles (intestin grêle), assure une couverture optimale de l\'ensemble du tractus intestinal. Chaque comprimé croquable contient <b>3 milliards de cellules actives</b>, jusqu\'à la date de péremption. Ne nécessite aucune réfrigération.</p>',
 '<p class="pbl-desc">Helps maintain immune function and supports gastrointestinal health with this chewable probiotic and lactic ferment complex, containing <b>5 carefully selected strains</b>. Its formula, composed of Bifidobacteria, residents of the colon, and Lactobacilli, inhabitants of the small intestine, ensures optimal coverage of the entire intestinal tract. Each chewable tablet contains <b>3 billion active cells</b>, guaranteed until the expiration date. No refrigeration required.</p>'),
('<p class="nonmed">Sorbitol, xylitol, inuline, cellulose microcristalline, extrait de levure, maltodextrine, tréhalose, concentré de jus de betterave, saveur de baies, stéarate de magnésium, dioxyde de silicium, acide citrique.</p>',
 '<p class="nonmed">Sorbitol, xylitol, inulin, microcrystalline cellulose, yeast extract, maltodextrin, trehalose, beet juice concentrate, berry flavor, magnesium stearate, silicon dioxide, citric acid.</p>'),
('<p>Prendre un comprimé deux fois par jour, au déjeuner et au souper. Prendre 2 à 3 heures avant ou après la prise d\'antibiotiques.</p>',
 '<p>Take one tablet twice daily with breakfast and dinner. Take 2 to 3 hours before or after taking antibiotics.</p>'),
('<p><b>Mode d\'emploi :</b> pour enfants de 3 ans et plus, dissoudre ou écraser les comprimés afin de prévenir l\'étouffement.</p>',
 '<p><b>Instructions for use:</b> For children under 6 years old: Dissolve or crush tablets to prevent choking.</p>'),
]
fwcro=fw("Probaclac maintains your children's health.",[
"Little ones deserve all the support they need to grow up healthy, including a supply of beneficial bacteria! Their natural curiosity and interactions with other children increase their exposure to infections.",
"Additionally, their boundless energy can lead to higher nutritional needs and a risk of deficiencies. Some children experience constipation, while others may develop digestive issues, such as diarrhea, after taking antibiotics.",
"For some infants, allergies, food intolerances, and picky eating habits limit the variety of foods they consume, making it more challenging to get essential nutrients.",
"<b>How to take Probaclac Chewable?</b> Starting at age 3, strengthen your child's digestive, immune, respiratory, and urinary systems with no less than six human probiotic strains tailored to their needs.",
"At birth, a baby’s microbiome is primarily composed of Bifidobacteria. That’s why the Children's supplement contains several Lactobacilli (Lactobacillus rhamnosus, casei, acidophilus, and paracasei) along with select Bifidobacteria (Bifidobacterium breve and longum) to help balance their intestinal flora.",
"Additionally, the dosage of 3 billion active cells aligns with the recommendations of the Canadian Paediatric Society.",
"The product is free from priority allergens but may contain dairy proteins.",
"Our low-sugar, chewable tablet is free from artificial ingredients, tastes great, and is easy to crumble into food or drinks.",
])
_en.build('probiotique-enfant.html','probiotique-enfant.html',cro,fwcro)

# ---- EXTRA-FORT ----
ext=[
('<h1>Pour les problèmes aigus au niveau des intestins</h1>','<h1>For acute intestinal problems</h1>'),
('<dd>Extra-fort</dd>','<dd>Extra-Strength probiotic</dd>'),
('<p class="pbl-desc">Contribue à restaurer l\'équilibre de votre flore intestinale avec ce complexe probiotique multi-souches, regroupant <b>8 souches</b> soigneusement sélectionnées. Sa formule assure une couverture optimale du tractus intestinal et favorise un rééquilibrage rapide du microbiote. Chaque capsule contient <b>10,5 milliards de cellules actives</b>, jusqu\'à la date de péremption. Ne nécessite aucune réfrigération.</p>',
 '<p class="pbl-desc">Helps restore the balance of your intestinal flora with this multi-strain probiotic and lactic ferment complex, containing <b>8 carefully selected strains</b>. Its formula ensures optimal coverage of the intestinal tract and promotes a rapid rebalancing of the microbiota. Each capsule contains <b>10.5 billion active cells</b>, guaranteed until the expiration date. No refrigeration required.</p>'),
('<p class="nonmed">Maltodextrine, capsules végétales (hypromellose), inuline, stéarate de magnésium, acide ascorbique.</p>',
 '<p class="nonmed">Maltodextrin, vegetable capsules (hypromellose), inulin (prebiotic), magnesium stearate, ascorbic acid.</p>'),
('<p><b>Adolescents (12 ans et plus) et adultes :</b> prendre une capsule deux fois par jour, au déjeuner et au souper.</p>',
 '<p><b>Adolescents (12 years and older) and adults:</b> Take one capsule twice daily with breakfast and dinner.</p>'),
('<p>Prendre au moins 2 à 3 heures avant ou après la prise d\'antibiotiques.</p>',
 '<p>Take at least 2 to 3 hours before or after taking antibiotics.</p>'),
]
fwext=fw('Probaclac maintains your digestive health.',[
"Medical and personal life situations can challenge your immune system—and your digestive health. The connection between the brain and the gut is undeniable, as cognitive functions influence digestive functions, and vice versa.",
"When stress affects either system, the gut microbiome is weakened, leading to direct consequences for the entire body.",
"Our powerful and comprehensive formula contains 10.5 billion active bacteria and no fewer than 8 different human strains.",
"<b>How to take Probaclac Extra-Strength?</b> Probaclac Extra-Strong is a formula designed for anyone suffering from acute intestinal issues.",
"It acts quickly and effectively thanks to its high concentration and diverse strains, providing comprehensive coverage of the intestinal tract.",
"It is also highly effective during antibiotic treatments.",
])
_en.build('probiotique-extra-fort.html','probiotique-extra-fort.html',ext,fwext)

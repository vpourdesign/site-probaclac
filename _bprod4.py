# -*- coding: utf-8 -*-
import _en
def fw(title,paras):
    h='<h2 class="shead__title" style="margin:0 0 1.1rem;">%s</h2>\n        '%title
    h+='\n        '.join('<p class="mute">%s</p>'%p for p in paras)
    return h+'\n      </div>'

# ---- MEDIC ----
med=[
('<h1>Réduit le risque de diarrhée durant l\'antibiothérapie</h1>','<h1>Reduces the risk of diarrhea during antibiotic treatment</h1>'),
('<dd>Medic</dd>','<dd>Probaclac Medic</dd>'),
('<p class="pbl-desc">Contribue à protéger votre microbiote lors de traitements antibiotiques avec ce complexe probiotique, regroupant <b>1 souche</b> (<span class="italic">Saccharomyces boulardii</span>) soigneusement sélectionnée. Son action antimicrobienne aide à prévenir la diarrhée associée aux antibiotiques et à lutter contre les infections nosocomiales comme <span class="italic">Clostridium difficile</span> et <span class="italic">Escherichia coli</span>. Chaque capsule contient <b>5 milliards de cellules actives</b>, jusqu\'à la date de péremption. Ne nécessite aucune réfrigération.</p>',
 '<p class="pbl-desc">Helps protect your microbiota during antibiotic treatments with this probiotic and lactic ferment complex, containing <b>1 carefully selected strain</b> (<span class="italic">Saccharomyces boulardii</span>). Its antimicrobial action helps prevent antibiotic-associated diarrhea and fight against hospital-acquired infections such as <span class="italic">Clostridium difficile</span> and <span class="italic">Escherichia coli</span>. Each capsule contains <b>5 billion active cells</b>, guaranteed until the expiration date. No refrigeration required.</p>'),
('<p class="nonmed">Maltodextrine, capsules végétales (hypromellose), stéarate de magnésium, acide ascorbique.</p>',
 '<p class="nonmed">Maltodextrin, vegetable capsules (hypromellose), magnesium stearate, ascorbic acid.</p>'),
('<p><b>Enfants (6 ans et plus), adolescents (12 ans et plus) et adultes :</b> prendre une capsule deux fois par jour, au déjeuner et au souper.</p>',
 '<p><b>Children (6 years and older), adolescents and adults:</b> Take one capsule twice daily with breakfast and dinner.</p>'),
('<p>Prendre simultanément avec la prise d\'antibiotiques. Prendre au moins 2 à 3 heures avant ou après la prise d\'antifongiques.</p>',
 '<p>Take simultaneously with taking antibiotics. Take at least 2 to 3 hours before or after taking antifungals.</p>'),
]
fwmed=fw('Probaclac supports you during your antibiotic treatment.',[
"Antibiotic treatments, while effective, do not always guarantee complete success. As they do their job, they do not differentiate between good and bad bacteria, disrupting the overall balance of your microbiome.",
"This can often lead to episodes of diarrhea, temporarily affecting your health and quality of life.",
"The Medic supplement contains Saccharomyces boulardii yeast, with 5 billion active cells per capsule.",
"People of all ages risk harboring drug-resistant bacteria, especially if they have undergone multiple antibiotic treatments.",
"<b>How to take Probaclac Medic?</b> Children over 6 years old, adults, and seniors should take Probaclac Medic at the same time as their antibiotic for a synergistic effect or 2 hours before or after if taking an antifungal (once or twice daily, as prescribed).",
"This strain has antimicrobial properties and is specifically recommended for preventing antibiotic-associated diarrhea. It also helps combat hospital-acquired infections such as Clostridium difficile and Escherichia coli.",
"Since Saccharomyces boulardii yeast is not affected by antibiotics, they form a powerful team against harmful bacteria!",
])
_en.build('probiotique-antibiotique.html','probiotique-antibiotique.html',med,fwmed)

# ---- GI ----
gi=[
('<h1>Réduit le risque de diarrhée lors de la prise d\'antibiotiques</h1>','<h1>Reduce the risk of antibiotic-associated diarrhea and help control acute infectious diarrhea</h1>'),
('<p class="pbl-desc">Contribue à soutenir votre santé intestinale durant une antibiothérapie avec ce complexe probiotique multi-souches, regroupant <b>5 souches</b> soigneusement sélectionnées, dont <span class="italic">Lactobacillus rhamnosus</span> GG, l\'une des souches les plus étudiées au monde. Chaque capsule contient <b>15 milliards de cellules actives</b>, jusqu\'à la date de péremption. Ne nécessite aucune réfrigération.</p>',
 '<p class="pbl-desc">Helps support your intestinal health during antibiotic therapy with this multi-strain probiotic and lactic ferment complex, containing <b>5 carefully selected strains</b>, including <span class="italic">Lactobacillus rhamnosus</span> GG, one of the most studied probiotic strains worldwide. Each capsule contains <b>15 billion active cells</b>, guaranteed until the expiration date. No refrigeration required.</p>'),
('<p class="nonmed">Maltodextrine, capsules végétales (hypromellose), inuline, stéarate de magnésium, acide ascorbique.</p>',
 '<p class="nonmed">Maltodextrin, vegetable capsules (hypromellose), inulin (prebiotic), magnesium stearate, ascorbic acid.</p>'),
('<p><b>Adolescents (12 ans et plus) et adultes :</b> prendre une capsule deux fois par jour, 2 heures après la prise de l\'antibiotique durant tout le traitement.</p>',
 '<p><b>Teens (12 years and up) and adults:</b> Take one capsule twice daily with breakfast and dinner.</p>'),
('<p>Continuer 3 à 5 jours après la fin du traitement antibiotique.</p>',
 '<p>Take at least 2 to 3 hours before or after taking antibiotics.</p>'),
]
fwgi=fw('Probaclac GI supports you during your antibiotic treatment.',[
"The use of antibiotics is becoming increasingly common, regardless of age. Antibiotic treatment not only eliminates harmful bacteria but also destroys beneficial ones, leading to intestinal issues commonly known as antibiotic-associated diarrhea. The result: an imbalanced gut flora.",
"It is therefore essential to replenish it with good bacteria to restore balance and prevent potential digestive issues.",
"Probaclac GI is specifically designed for use during antibiotic treatments. Its multi-strain formula includes Lactobacillus rhamnosus GG, one of the most studied and well-documented probiotic strains worldwide.",
"With a concentration of 15 billion bacteria per capsule, including 3 strains of Lactobacilli and 2 strains of Bifidobacteria, Probaclac GI will be your best ally during your next antibiotic treatment.",
"Antibiotic therapy disrupts the intestinal flora—restore it with Probaclac GI.",
"<b>How to take Probaclac GI?</b> Take one capsule twice a day, two hours after taking the antibiotic, throughout the entire treatment, and continue for 3 to 5 days after completing the antibiotic course.",
"Probaclac GI is specifically designed to reduce the risk of antibiotic-associated diarrhea and helps manage acute infectious diarrhea.",
"One of the strains in Probaclac GI is Lactobacillus rhamnosus GG, one of the most extensively studied probiotic strains worldwide, with most research focusing on its effectiveness in preventing antibiotic-related diarrhea.",
])
_en.build('probiotique-gastro-intestinal.html','probiotique-gastro-intestinal.html',gi,fwgi)

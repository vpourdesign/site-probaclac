# -*- coding: utf-8 -*-
import _en
def fw(title,paras):
    h='<h2 class="shead__title" style="margin:0 0 1.1rem;">%s</h2>\n        '%title
    h+='\n        '.join('<p class="mute">%s</p>'%p for p in paras)
    return h+'\n      </div>'
uri=[
('<h1>Prévention des infections des voies urinaires</h1>','<h1>For prevention of urinary tract infections</h1>'),
('<dd>Avec canneberges</dd>','<dd>Cranberries</dd>'),
('<p class="pbl-desc">Contribue à soutenir votre santé gastro-intestinale et à prévenir les infections des voies urinaires avec ce complexe probiotique, regroupant <b>9 souches</b> soigneusement sélectionnées, enrichi d\'un extrait de canneberges. Sa formule, composée de Bifidobactéries (côlon) et de Lactobacilles (intestin grêle), assure une couverture optimale du tractus intestinal. Chaque capsule contient <b>5 milliards de cellules actives</b>, jusqu\'à la date de péremption. Ne nécessite aucune réfrigération.</p>',
 '<p class="pbl-desc">Helps support your gastrointestinal health and prevent urinary tract infections with this multi-strain probiotic and lactic ferment complex, containing <b>9 carefully selected strains</b>. Its formula, composed of Bifidobacteria, residents of the colon, and Lactobacilli, inhabitants of the small intestine, ensures optimal coverage of the entire intestinal tract. Each capsule contains <b>5 billion active cells</b>, guaranteed until the expiration date. No refrigeration required.</p>'),
('<p class="nonmed">Maltodextrine, capsules végétales (hypromellose), stéarate de magnésium, acide ascorbique.</p>',
 '<p class="nonmed">Maltodextrin, vegetable capsule (hypromellose), magnesium stearate, ascorbic acid.</p>'),
('<p><b>Adultes :</b> prendre une capsule deux fois par jour, au déjeuner et au souper. Prendre 2 à 3 heures avant ou après la prise d\'antibiotiques.</p>',
 '<p><b>Adults:</b> Take one capsule twice daily with breakfast and dinner. Take 2 to 3 hours before or after taking antibiotics.</p>'),
('<p><b>Durée :</b> utiliser un minimum de 4 semaines pour des effets bénéfiques.</p>',
 '<p><b>Duration of use:</b> Use for a minimum of 4 weeks for beneficial effects.</p>'),
]
fwuri=fw('Probaclac helps prevent urinary tract infections.',[
"Do you have an urgent need to go? Are your bathroom visits frequent? Do you feel pain or a burning sensation when urinating, along with a sense of incomplete emptying?",
"These are classic symptoms of a urinary tract infection (UTI), a condition that particularly affects: seniors, diabetics, pregnant women, men with an enlarged prostate, individuals with a catheter, and patients with kidney stones.",
"An excess of harmful bacteria like Escherichia coli causes cystitis, which can otherwise be prevented by the protective barrier formed by good bacteria in a healthy urinary tract.",
"Probaclac helps restore beneficial bacteria in the urinary tract to fight urinary tract infections.",
"<b>How to take Probaclac Cranberries?</b> To prevent urinary tract infections, there’s nothing better than combining probiotics and cranberries!",
"Our product features 9 human bacterial strains (with a concentration of 5 billion active cells per capsule) and cranberry extract (200 milligrams per capsule).",
"Probiotics help recolonize the intestinal and urogenital environments, while cranberry provides proanthocyanidins (PACs) that prevent harmful bacteria from adhering to the bladder.",
"Prevention is key. Take the supplement for at least 4 weeks to allow it to work effectively.",
])
_en.build('probiotique-infection-urinaire.html','probiotique-infection-urinaire.html',uri,fwuri)

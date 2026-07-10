# -*- coding: utf-8 -*-
import _en
def fw(title,paras):
    h='<h2 class="shead__title" style="margin:0 0 1.1rem;">%s</h2>\n        '%title
    h+='\n        '.join('<p class="mute">%s</p>'%p for p in paras)
    return h+'\n      </div>'

FAQ=[
("Puis-je l'utiliser durant le cycle menstruel ?","Can I use Probaclac Vaginal probiotic during the menstrual cycle?"),
("Il est préférable d'attendre la fin du cycle avant de commencer le traitement. L'écoulement menstruel ne permet pas aux probiotiques d'exercer leur effet bénéfique : les bonnes bactéries sont évacuées avec le flux menstruel et ne peuvent donc pas équilibrer le pH vaginal.",
 "It is best to wait until the end of cycle before starting treatment. The menstrual flow does not allow the probiotics to exert their beneficial effect. Good bacteria are evacuated with the menstrual flow and therefore can not balance the vaginal pH."),
("Puis-je l'utiliser durant une antibiothérapie ?","Can I use Probaclac Vaginal probiotic during antibiotherapy?"),
("Si la prise d'antibiotiques se fait par voie buccale, vous pouvez utiliser Probaclac Vaginose bactérienne. Si les antibiotiques sont administrés par voie vaginale, attendez la fin du traitement.",
 "If taking oral antibiotics, you can use Probaclac vaginal. If taking vaginally administered antibiotics, wait until the end of treatment."),
("Les femmes enceintes ou qui allaitent peuvent-elles l'utiliser ?","Can pregnant women take Probaclac Vaginal probiotic?"),
("Oui. L'innocuité des probiotiques a été démontrée. Par contre, il serait préférable de consulter un professionnel de la santé si vous êtes enceinte avant l'utilisation de ce produit.",
 "Yes, probiotics have been proven to be safe and harmless, and there is no reason to avoid taking Probaclac, because it is beneficial for both the mother and the unborn child."),
("Est-il possible d'avoir des relations sexuelles pendant la probiothérapie vaginale ?","Is it possible to have sex during vaginal probiotherapy?"),
("Oui absolument, mais vous devez attendre après la relation pour commencer le traitement quotidien du Probaclac.",
 "Yes, but you should wait until after intercourse before starting the daily treatment with Probaclac Vaginal probiotic."),
]

# ---- VAGINAL ----
vag=[
('<h1>Réduit la récurrence de la vaginose bactérienne</h1>','<h1>For recurrence of bacterial vaginosis</h1>'),
('<dd>Probaclac vaginal</dd>','<dd>Vaginal probiotic</dd>'),
('<p class="pbl-desc">Réduit la récurrence de la vaginose bactérienne et contribue à maintenir l\'équilibre de la flore vaginale avec ce complexe probiotique, regroupant <b>3 souches</b> naturellement présentes dans la flore féminine : <span class="italic">Lactobacillus rhamnosus</span>, <span class="italic">Lactobacillus acidophilus</span> et <span class="italic">Streptococcus thermophilus</span>. Ce traitement cible directement les bactéries pathogènes à l\'origine de l\'infection. Chaque capsule contient plusieurs milliards de cellules actives, jusqu\'à la date de péremption. Ne nécessite aucune réfrigération.</p>',
 '<p class="pbl-desc">Helps maintain the balance of your intimate flora with this probiotic and lactic ferment complex, containing <b>3 carefully selected strains</b>: <span class="italic">Lactobacillus rhamnosus</span>, <span class="italic">Lactobacillus acidophilus</span>, and <span class="italic">Streptococcus thermophilus</span>. This treatment directly targets pathogenic bacteria responsible for vaginal infections. Each capsule contains several billion active cells, guaranteed until the expiration date. No refrigeration required. Our clinical study with this product demonstrated a reduction of over 84% in the recurrence of bacterial vaginosis within the year following treatment.</p>'),
('<p class="nonmed">Maltodextrine, lactose, gélatine, stéarate de magnésium, acide ascorbique.</p>',
 '<p class="nonmed">Maltodextrin, lactose, gelatin, magnesium stearate, ascorbic acid.</p>'),
('<p><b>Femmes adultes (18 ans et plus) :</b> insérer une capsule intravaginale au coucher pendant 14 jours consécutifs, ou selon l\'avis d\'un praticien de la santé.</p>',
 '<p><b>Adult women (18 years and older):</b> Insert one capsule intravaginally at bedtime for 14 consecutive days or as directed by a healthcare practitioner.</p>'),
('<p>Voir les instructions sur la boîte Probaclac Vaginal.</p>','<p>See instructions on the Probaclac Vaginal box.</p>'),
('<p class="studyband__txt"><b>−84&nbsp;%</b> de récurrence de la vaginose bactérienne dans l\'année suivant le traitement</p>',
 '<p class="studyband__txt"><b>−84&nbsp;%</b> recurrence of bacterial vaginosis within the year following treatment</p>'),
('Vos questions sur Probaclac Vaginal.','Your questions about Probaclac Vaginal.'),
]+FAQ
fwvag=fw('Probaclac fights vaginal infections.',[
"Women know that with hormonal fluctuations and changes in the acidity of the reproductive system environment, fighting vaginal infections is not always an easy task!",
"At least 1 in 10 women will experience bacterial vaginosis at least once in their lifetime (the prevalence triples during pregnancy).",
"The symptoms associated with bacterial vaginosis are caused by a high vaginal pH, which results from certain lifestyle factors (such as stress, poor eating habits, number of sexual partners, alcohol consumption, etc.) and antibiotic treatments.",
])
_en.build('probiotique-vaginal.html','probiotique-vaginal.html',vag,fwvag)

# ---- LEVURE (Yeast infection) ----
lev=[
('<h1>Réduit les signes de candidose vulvo-vaginale</h1>','<h1>Reduces the signs of vulvovaginal candidiasis (VVC)</h1>'),
('<dd>Infection à levure</dd>','<dd>Yeast infection</dd>'),
('<p class="pbl-desc">Réduit les signes de candidose vulvo-vaginale (CVV) et aide à traiter la candidose vulvo-vaginale récurrente. Contribue à maintenir l\'équilibre de la flore vaginale avec sa souche unique <span class="italic">Lactiplantibacillus plantarum</span> Rosella. Sa formule agit directement à la source des inconforts : pertes et odeurs, démangeaisons, brûlures, rougeurs et gonflements, et atténue les douleurs lors des rapports sexuels et de la miction. Ne nécessite aucune réfrigération. <span class="italic">En combinaison avec un traitement antifongique.</span></p>',
 '<p class="pbl-desc">Reduces the signs of vulvovaginal candidiasis (VVC) and helps treat recurrent vulvovaginal candidiasis.* It also helps maintain the balance of vaginal flora with its unique strain, <span class="italic">Lactiplantibacillus plantarum</span> Rosella. Its formula acts directly at the source of discomfort to reduce vaginal discharge and odor, as well as itching, burning, redness, and swelling. It also helps relieve pain during sexual intercourse and urination, promoting overall intimate well-being. No refrigeration required. <span class="italic">*In combination with an antifungal treatment.</span></p>'),
('<p class="nonmed">Maltodextrine, gélatine, stéarate de magnésium, acide ascorbique.</p>',
 '<p class="nonmed">Maltodextrin, gelatin, magnesium stearate, ascorbic acid.</p>'),
('<p><b>Femmes adultes (18 ans et plus) :</b> après une infection ou en présence de signes, utiliser une capsule par jour pendant 6 jours consécutifs. Prendre au moins 2 à 3 heures avant ou après la prise d\'antibiotiques. Répéter au besoin.</p>',
 '<p><b>Adult women (18 years and older):</b> after an infection or in the presence of signs, use one capsule per day for 6 consecutive days. Take at least 2 to 3 hours before or after taking antibiotics. Repeat as needed.</p>'),
('<p>Voir les instructions sur la boîte Probaclac Infection à levure.</p>','<p>See instructions on the Probaclac Yeast Infection box.</p>'),
('<p class="studyband__txt"><b>91&nbsp;%</b> des femmes n\'ont pas eu de rechute après 4 mois (étude Carriero, 476 femmes)</p>',
 '<p class="studyband__txt"><b>91&nbsp;%</b> of women had no relapse after 4 months (Carriero study, 476 women)</p>'),
('Vos questions sur Probaclac Infection à levure.','Your questions about Probaclac Yeast Infection.'),
]+FAQ
fwlev=fw('Probaclac fights yeast infections.',[
'Yeast infections, commonly known as vaginitis, are among the most frequently discussed. They are caused by a decrease in good bacteria and an overgrowth of fungi, mainly <span class="italic">Candida</span>. This imbalance leads to white discharge that causes itching and burning.',
"These infections can be attributed to several factors such as: a hormonal imbalance, taking antibiotics or an oral contraceptive, fatigue, stress, or a weakened immune system.",
])
_en.build('probiotique-infection-a-levure.html','probiotique-infection-a-levure.html',lev,fwlev)

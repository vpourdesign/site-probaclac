# -*- coding: utf-8 -*-
import _en, re
src=open('foire-aux-questions.html',encoding='utf-8').read()
qs=re.findall(r'<span>(.*?)</span><span class="faq__ic"',src,re.S)
ans=re.findall(r'<p class="faq__a">(.*?)</p>',src,re.S)
ENQ=[
"Can I take probiotics every day?",
"What is the ideal daily concentration of probiotics?",
"Do I need to refrigerate probiotics once the bottle is opened?",
"When should Probaclac be taken?",
"Can the capsule be opened?",
"What is the difference between yogurt and Probaclac?",
"Did you know that as you age, the strength of your immune system decreases?",
"Can my child take Probaclac chewable every day?",
"If my child is very young, how can I give them Probaclac?",
"Can Probaclac Travelers help if I experience intestinal issues while traveling?",
"If planning to travel, when should Probaclac Travelers be started?",
"How can I ensure that the cranberry concentration is effective?",
"Can Probaclac Vaginal be used for prevention?",
"Why should probiotics be taken during antibiotic therapy?",
"Can pregnant women take Probaclac?",
"Can Probaclac be taken if I have lactose intolerance?",
"Can Probaclac be taken with anticoagulants (such as Coumadin)?",
"If taking an antibiotic, when should Probaclac MEDIC be taken?",
"If taking medication, can Probaclac be taken?",
]
ENA=[
"Absolutely, taking probiotics every day stimulates your white blood cells which acts beneficially on your immune system. Probiotics taken daily will also help strengthen your intestinal flora, aid in the digestion of food and reduce food intolerances and allergies in the long term.",
"It is recommended to consume between 10 and 20 billion probiotics per day in order to have a beneficial effect if taken for maintenance or prevention. All our formulas are adapted accordingly for daily consumption or treatment.",
"Our probiotics are stable at room temperature and do not need to be refrigerated. Our probiotics are guaranteed until the expiration date if stored in a cool, dry place.",
"At mealtimes unless taking antibiotics, take Probaclac 2 hours after taking the antibiotic.",
"Yes. If you cannot take a capsule, you can sprinkle the powder on food, such as yogurt, or dilute it with milk or water.",
"Although yogurts are good foods, they are not truly multi-strain probiotic supplements that ensure the balance of the entire intestinal flora. In commercial yogurts, the concentrations are often insufficient and the probiotic strains used are generally of animal origin. Since they are natural inhabitants of the flora in humans, it is preferable to use probiotic strains of human origin such as those found in Probaclac products.",
"The intestinal flora undergoes changes throughout your life, from early childhood to advanced adulthood, it adapts and changes. However, around the age of fifty, the population of bifidobacteria naturally decreases drastically, which has the consequence of acting on the immune system, which is why it is important to consume probiotics with a good concentration of bifidobacteria.",
"Absolutely, a child's intestinal flora is often disrupted by stress, adaptation problems or other environmental factors, which causes irregularities in them. Therefore, it is important to support them with probiotics that will help maintain their intestinal flora healthy.",
"Our new Probaclac for Children formula is now available in an openable capsule, allowing you to sprinkle the probiotics on any food or drink while retaining their benefits.",
"Yes absolutely, if you have not taken Probaclac Voyageurs as a preventative measure before your departure, it is recommended to take 1 to 2 capsules per day during your stay in order to restore your intestinal flora.",
"It is recommended to start taking Probaclac VOYAGEURS 10 days before departure, for the entire duration of the trip and for a period of one week upon return.",
"In fact, what is important is the amount of PAC (pro-anthocyanidins) which is the active ingredient in cranberries and prevents bad bacteria from lodging in the bladder.",
"Yes absolutely, in this case it is not necessary to use the product for 14 days in a row. The product can therefore be used a few days in a row at a time as a preventative measure.",
"Antibiotics destroy not only bad bacteria, but also good ones, which has the effect of unbalancing the intestinal flora. The new Probaclac GI is designed specifically for taking antibiotics, it helps to control infectious diarrhea and reduce the risk of developing diarrhea associated with taking antibiotics. It is therefore important to take 1 capsule 2 hours after taking the antibiotic.",
"Yes. The safety and security of probiotics has been demonstrated. In fact, it is recommended to consume Probaclac regularly since it is beneficial for both the mother and the unborn child.",
"Yes. In fact, if you suffer from lactose intolerance, Probaclac can help you because the probiotic strains have the property of producing lactase which helps metabolize lactose.",
"Yes. Probiotics do not exert activity on clotting factors.",
"Children over 6 years old, adults and the elderly should take Probaclac Medic simultaneously with taking the antibiotic for a synergistic effect or 2 hours before or after if it is an antifungal (depending on the prescription, it will be once or twice a day).",
"As a general rule, if a medicine is to be taken on an empty stomach, it is best to leave a gap of 2 hours between taking the medicine and taking Probaclac. For all other medicines, there is no interaction and therefore one can consume Probaclac as specified in the dosage.",
]
assert len(qs)==len(ENQ)==len(ans)==len(ENA)==19, (len(qs),len(ans))
b=[
('<title>'+src.split('<title>')[1].split('</title>')[0]+'</title>','<title>Answers to your questions about probiotics | Probaclac</title>'),
('<div class="eyebrow"><span class="dot"></span>Foire aux questions</div>','<div class="eyebrow"><span class="dot"></span>Frequently asked questions</div>'),
('<h1 class="hero__h1">Vos questions, nos réponses.</h1>','<h1 class="hero__h1">Your questions, our answers.</h1>'),
]
for i in range(19):
    b.append(('<span>'+qs[i]+'</span>','<span>'+ENQ[i]+'</span>'))
    b.append(('<p class="faq__a">'+ans[i]+'</p>','<p class="faq__a">'+ENA[i]+'</p>'))
_en.build('foire-aux-questions.html','foire-aux-questions.html',b)

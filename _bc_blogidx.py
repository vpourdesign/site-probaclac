# -*- coding: utf-8 -*-
import _en, re
EN={
"trop-d-appetit-pensez-aux-bacteries":("Insatiable appetite? Think of Bacteria!","Two subjects that fascinate human beings and that may actually be… intimately connected! We now have reason to believe that our eating behaviors are partly driven by our gut microbiota."),
"la-bacteriotherapie-a-portee-de-main":("Bacteriotherapy at your fingertips","Microorganisms colonize different regions of the human body, from the skin to the oral and nasal cavities, as well as the digestive and urogenital systems. The majority of microbes reside in the intestinal tract."),
"d-ou-proviennent-vos-probiotiques":("Where do probiotics come from?","The probiotics market is booming and all the – often contradictory – information available can rapidly overwhelm consumers. Such a commercial wave should not deter you from navigating the ocean of probiotics, as long as you consider some key elements of their formulation."),
"des-bibittes-pour-aider-les-diabetiques":("Bacteria help people with diabetes!?","The World Health Organization (WHO) predicts that non-insulin-dependent type 2 diabetes will become the seventh leading cause of death in 2030. This is due to the fact that these diabetics have an increased risk of developing cardiovascular diseases, the leading cause of death in the world."),
"peaux-acneiques-a-vos-probiotiques":("Acne-prone skins, get your probiotics!","Skin is the largest organ of the body. Needless to say, this site is constantly exposed to physical, chemical, bacterial and fungal irritants. The healthy human dermis can produce an army of antimicrobial substances that play an important role in the elimination of potential skin pathogens."),
"quand-les-bacteries-l-emportent-s-o-s-sibo":("When bacteria takes over: S.O.S. SIBO","Have you ever heard of SIBO (Small Intestinal Bacterial Overgrowth)?"),
"plein-feux-sur-les-prebiotiques":("Spotlight on Prebiotics","“The dependence of our gut microbiota on food makes it possible to modify this intestinal flora, to replace pathogenic bacteria with those that benefit us.” – Ilya Metchnikov, Nobel Laureate in Physiology or Medicine (1908)"),
"probiotiques-une-revolution-immunitaire":("Probiotics: immune revolution","The human organism, despite all its complexity and resilience, is constantly at risk of infection."),
"les-probiotiques-panacee-pour-l-obesite-1":("Probiotics, the solution to obesity?","In Quebec, the prevalence of obesity has doubled in the last 25 years. According to the most recent statistics, one in five people in the province has clinical obesity."),
"aide-probiotique-a-la-menopause":("Probiotic support during menopause","Menopause is usually between the ages of 48 and 55, although it can vary greatly from one woman to another."),
"pour-vieillir-en-sante-l-affaire-est-microbiote-1":("Healthy aging…through the microbiota","After Japan and South Korea, Quebec is one of the societies with more people accessing advanced stages of life."),
"les-probiotiques-et-la-grossesse-font-bon-menage":("Probiotics and pregnancy mix well","To witness the birth of a child is our best opportunity to experience the meaning of the word miracle. – Paul Carvel"),
"l-emporter-sur-la-vaginite-vaginose-bacterienne":("Prevail over Vaginitis (bacterial vaginosis)","Bacterial vaginosis is the most common vaginal infection, so we have to talk about it!"),
"les-allergies-alimentaires-pandemique":("Food allergies: Pandemic?","Food allergy is an overreaction of the immune system to a normally harmless protein in a food."),
"vaincre-la-constipation-une-fois-pour-toute":("Defeat constipation Once and for all","The person who suffers from constipation has infrequent stools and/or a difficult evacuation of “bodily waste”."),
"ne-partez-jamais-sans-eux-probiotiques-en-voyage":("Never leave without them: Travel probiotics","On the road to the unknown or the all-inclusive resort! Although traveler’s diarrhea is more common in tropical and developing countries, other destinations are not exempt."),
"agrementez-votre-menu-de-probiotiques":("Brighten up your menu with probiotics","The benefits of probiotics on health are well recognized. They have positive effects on the digestive and immune system and on organs in the body such as the heart and brain."),
"probiotiques-pour-un-esprit-de-genie":("Probiotics for a genius mind","The effects of probiotics go far beyond the intestines: they optimize digestion at any age, but also develop the brain of the little ones, in addition to supporting their immune system."),
"colonisation-bacterienne-et-dentition":("Bacterial colonization and dentition","Bite into life with your pearly whites! Humans are made up of more bacterial cells than cells specific to the body. Only a few hours after birth, the mouth is richly colonized."),
"la-sante-par-le-ventre":("Health through the belly","“Happiness: a good bank account, a good cook and a good digestion.” – Jean-Jacques Rousseau"),
}
MO={'janvier':'January','février':'February','mars':'March','avril':'April','mai':'May','juin':'June','juillet':'July','août':'August','septembre':'September','octobre':'October','novembre':'November','décembre':'December'}
s=_en.chrome(open('blogue.html',encoding='utf-8').read())
# header
s=s.replace('<title>Blogue — Probaclac</title>','<title>Blog — Probaclac</title>')
s=s.replace('<div class="eyebrow"><span class="dot"></span>Le blogue Probaclac</div>','<div class="eyebrow"><span class="dot"></span>The Probaclac blog</div>')
s=s.replace('<h1>Comprendre le microbiote, un article à la fois.</h1>','<h1>Understanding the microbiota, one article at a time.</h1>')
s=s.replace('Conseils, science et habitudes de vie autour des probiotiques de grade pharmaceutique — rédigés au Québec.','Advice, science and lifestyle around pharmaceutical-grade probiotics — written in Quebec.')
s=s.replace("Lire l'article →","Read article →")
# process cards
def card_sub(m):
    block=m.group(0); slug=m.group(1)
    if slug not in EN: return ''  # drop non-EN article
    title,exc=EN[slug]
    block=re.sub(r'(<h2 class="blogcard__title">).*?(</h2>)', lambda x:x.group(1)+title+x.group(2), block, flags=re.S)
    block=re.sub(r'(<p class="blogcard__excerpt">).*?(</p>)', lambda x:x.group(1)+exc+x.group(2), block, flags=re.S)
    # alt
    block=re.sub(r'(alt=")[^"]*(")', lambda x:x.group(1)+title.replace('"','')+x.group(2), block)
    # date months
    for fr,en in MO.items(): block=block.replace(fr,en)
    return block
s=re.sub(r'<a class="blogcard r" href="blogue/([^"]+)\.html">.*?</a>', card_sub, s, flags=re.S)
open('en/blogue.html','w',encoding='utf-8').write(s)
kept=len(re.findall(r'class="blogcard r"',s))
print("EN blog index built — cards kept:",kept)

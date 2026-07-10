# -*- coding: utf-8 -*-
import re
SRC='probiotique-adulte.html'
s=open(SRC,encoding='utf-8').read()
HEAD=s[:s.index('<!-- ─── 1. HERO')]
TAIL=s[s.index('<!-- ─── FOOTER'):]

STD_BADGES=[
 ("https://static.wixstatic.com/media/623234_e34e7d51c0b045f892556e4a17c1713d~mv2.jpg","Sans gluten"),
 ("https://static.wixstatic.com/media/623234_82219e3c86ae48d9954baac0210d9aaf~mv2.jpg","Sans soya"),
 ("https://static.wixstatic.com/media/623234_a069aaba10fc4cc2a0555f996d3cdf90~mv2.jpg","Sans protéines laitières"),
 ("https://static.wixstatic.com/media/623234_3f4f653f708d4a38879c16ecb35f8292~mv2.jpg","Capsules végétales"),
]

def badges_html(bs):
    return '\n'.join(f'          <div class="hero-badge"><img src="{i}" alt=""><span>{l}</span></div>' for i,l in bs)

def strains_html(rows):
    out=[]
    for r in rows:
        n,c,u=r[0],r[1],r[2]; noital=len(r)>3 and r[3]=='noital'
        st=' style="font-style:normal"' if noital else ''
        out.append(f'        <div class="strain"><span class="strain__name"{st}>{n}</span><span class="strain__code">{c}</span><span class="strain__ufc">{u}</span></div>')
    return '\n'.join(out)

ALLERG='''<!-- ─── ALLERGÈNES ─── -->
<section class="allerg-video">
  <video autoplay muted loop playsinline poster="https://static.wixstatic.com/media/11062b_3da4a26484194105bde5b3935f5afb7bf000.jpg">
    <source src="https://video.wixstatic.com/video/11062b_3da4a26484194105bde5b3935f5afb7b/1080p/mp4/file.mp4" type="video/mp4">
  </video>
  <div class="frost reveal">
    <h2>Probiotiques sans allergènes</h2>
    <p>Probaclac est fier d'offrir des probiotiques sans allergènes*. Tout au long de la production, les allergènes alimentaires prioritaires sont évités.</p>
    <p>Nous sommes engagés à fournir des suppléments adaptés à tous, peu importe la sensibilité. Probaclac est la référence pour des probiotiques sans protéines laitières, sans gluten, sans soya et sans tous les allergènes classiques.</p>
    <p class="small">*Probaclac Croquable pour enfants peut contenir des traces de protéines laitières. Probaclac Medic peut contenir des traces de soya.</p>
  </div>
</section>
'''

CTA='''<style>
.cta-cols{ display:grid; grid-template-columns:repeat(4,1fr); gap:0; max-width:1120px; margin:0 auto 2.2rem; align-items:center; }
.cta-cols > div{ font-weight:700; font-size:1rem; line-height:1.35; color:var(--ink); padding:.2rem 1.6rem; text-align:center; }
.cta-cols > div + div{ border-left:1px solid rgba(10,10,10,.24); }
@media(max-width:760px){ .cta-cols{ grid-template-columns:1fr 1fr; gap:1.2rem 0; } .cta-cols > div + div{ border-left:0; } .cta-cols > div:nth-child(odd){ border-right:1px solid rgba(10,10,10,.24); } }
@media(max-width:430px){ .cta-cols{ grid-template-columns:1fr; } .cta-cols > div{ border:0 !important; padding:.4rem 0; } }
</style>
<!-- ─── CTA ─── -->
<section class="section on-accent" id="final">
  <div class="wrap" style="text-align:center;">
    <h2 class="reveal" style="font-weight:700;letter-spacing:-.04em;font-size:var(--t-h2);line-height:1;margin:0 0 1.2rem;">__CTATITLE__</h2>
    <div class="cta-cols reveal">
      <div>Ne nécessite pas de réfrigération</div>
      <div>Conserver dans un endroit à l’abri de l’humidité</div>
      <div>Prendre après le repas pour une assimilation améliorée</div>
      <div>S’il y a prise d’antibiotiques, prendre au moins 2 heures après la prise d’antibiotiques</div>
    </div>
    <a class="btn btn--solid reveal" href="https://www.monprobiotique.ca">Voir au magasin en ligne<span class="arr">→</span></a>
  </div>
</section>
'''

def body(p):
    studyband=''
    if p.get('stat'):
        studyband=f'''<!-- ÉTUDE -->
<section class="section" id="etude-band" style="padding-top:clamp(5rem,9vw,7.5rem);padding-bottom:clamp(2.5rem,5vw,4rem);">
  <div class="wrap">
    <div class="studyband reveal">
      <img class="studyband__img" src="{p['hero_img']}" alt="Probaclac {p['name']}">
      <p class="studyband__txt">{p['stat']}</p>
      <a class="btn btn--solid" href="https://etudes.probaclac.ca/">Voir nos études<span class="arr">→</span></a>
    </div>
  </div>
</section>

'''
    fw='\n        '.join(f'<p class="mute">{x}</p>' for x in p['forwhom_ps'])
    return f'''<!-- HERO -->
<header class="section hero pbl-hero">
  <div class="wrap">
    <div class="pbl-hero__grid">
      <div class="pbl-hero__media reveal">
        <img src="{p['hero_img']}" alt="Probaclac {p['name']}">
      </div>
      <div class="hero__left">
        <h1>{p['h1']}</h1>
        <dl class="spec">
          <div><dt>Formule</dt><dd>{p['formule']}</dd></div>
          <div><dt>Formats disponibles</dt><dd>{p['formats']}</dd></div>
          <div><dt>NPN</dt><dd><b>{p['npn']}</b></dd></div>
        </dl>
        <p class="pbl-desc">{p['desc']}</p>
        <div class="hero-badges">
{badges_html(p.get('badges',STD_BADGES))}
        </div>
      </div>
    </div>
  </div>
</header>

<!-- COMPO -->
<section class="section comp-section" id="souches">
  <div class="wrap">
    <div class="comp">
      <div class="comp__strains reveal">
        <h2 class="comp__title">Ingrédients médicinaux</h2>
        <div class="comp__caphdr">par capsule</div>
{strains_html(p['strains'])}
      </div>
      <aside class="comp__side reveal">
        <div class="card-white">
          <h3>Posologie</h3>
          {p['posology']}
        </div>
        <div class="card-white">
          <h3>Ingrédients non-médicinaux</h3>
          <p class="nonmed">{p['nonmed']}</p>
        </div>
      </aside>
    </div>
  </div>
</section>

{studyband}<!-- POUR QUI -->
<section class="section" id="pourqui">
  <div class="wrap">
    <div class="forwhom">
      <div class="forwhom__visual reveal"><img src="{p['shield_img']}" alt="Probaclac {p['name']}"></div>
      <div class="forwhom__rule" aria-hidden="true"></div>
      <div class="reveal">
        <h2 class="shead__title" style="margin:0 0 1.1rem;">{p['forwhom_title']}</h2>
        {fw}
      </div>
    </div>
  </div>
</section>

{ALLERG}
{CTA.replace("__CTATITLE__", p.get('cta_title','Soutenez votre santé intestinale.'))}'''

def gen(p):
    head=re.sub(r'<title>.*?</title>', '<title>'+p['title']+'</title>', HEAD, count=1, flags=re.S)
    open(p['slug']+'.html','w',encoding='utf-8').write(head+body(p)+TAIL)
    print('wrote', p['slug']+'.html')

PRODUCTS=[
{
 'slug':'probiotique-50-et-plus','name':'50 ans et +','title':'Probiotique 50 ans et + — Probaclac',
 'hero_img':'assets/cdn/pblx-card-50plus.jpg','h1':'Pour un usage quotidien 50+',
 'formule':'50 ans et plus','formats':'30 / 60 capsules','npn':'80013814',
 'desc':"Contribue à soutenir votre santé gastro-intestinale avec ce complexe probiotique multi-souches conçu pour les 50 ans et plus. Sa formule associe Bifidobactéries (côlon) et Lactobacilles (intestin grêle) et inclut <b>7 souches</b> spécifiques pour compenser la baisse naturelle des bifidobactéries. Chaque capsule fournit <b>8,5 milliards de cellules actives</b>, dont 60 % de Bifidobactéries (4,8 milliards), garantie jusqu'à la date de péremption. Ne nécessite aucune réfrigération.",
 'strains':[
  ("Lacticaseibacillus rhamnosus","NL-228","1,7 milliard ufc"),
  ("Bifidobacterium bifidum","NL-236","1,6 milliard ufc"),
  ("Bifidobacterium breve","NL-240","1,6 milliard ufc"),
  ("Bifidobacterium longum","NL-235","1,6 milliard ufc"),
  ("Lactobacillus acidophilus","NL-214","1,5 milliard ufc"),
  ("Streptococcus thermophilus","NL-231","490 millions ufc"),
  ("Lactobacillus bulgaricus","NL-287","10 millions ufc"),
 ],
 'nonmed':"Maltodextrine, capsules végétales (hypromellose), inuline, stéarate de magnésium, acide ascorbique.",
 'posology':"<p><b>Adultes :</b> prendre une capsule deux fois par jour, au déjeuner et au souper.</p>\n          <p>Prendre au moins 2 à 3 heures avant ou après la prise d'antibiotiques.</p>",
 'stat':None,
 'shield_img':"https://static.wixstatic.com/media/623234_b85c1ce4f42b4f7f875d9fd9d6f55c5b~mv2.png",
 'forwhom_title':"Probaclac vous accompagne toute votre vie.",
 'forwhom_ps':[
  "Un des nombreux changements à se produire avec les années est la décroissance naturelle et éventuelle des espèces bifido-bactériennes qui résident dans le côlon.",
  "Notre probiotique 50+ offre une concentration de 8,5 milliards de cellules actives par capsule, spécialement conçue pour répondre aux besoins liés à la diminution naturelle de certaines bactéries avec l'âge. Les personnes de 50 ans et plus peuvent grandement bénéficier d'une supplémentation en probiotiques.",
 ],
},
{
 'slug':'probiotique-voyage','name':'Voyageurs','title':'Probiotique Voyageurs — Probaclac',
 'hero_img':'assets/cdn/pblx-card-voyage.jpg','h1':'Réduit les risques de diarrhée du voyageur',
 'formule':'Probiotique voyageurs','formats':'30 / 60 capsules','npn':'80108358',
 'desc':"Réduit les risques de diarrhée du voyageur et contribue à soutenir votre santé intestinale lors de vos déplacements avec ce complexe probiotique multi-souches, regroupant <b>9 souches</b> soigneusement sélectionnées. Sa formule, composée de souches naturelles dont <span class=\"italic\">Lactobacillus plantarum</span> (anti-diarrhée), aide à diversifier votre microbiote et à mieux faire face aux bactéries pathogènes des autres régions du monde. Chaque capsule contient <b>6,5 milliards de cellules actives</b>, jusqu'à la date de péremption. Ne nécessite aucune réfrigération.",
 'strains':[
  ("Saccharomyces boulardii","","2,5 milliards ufc"),
  ("Lacticaseibacillus paracasei","NL-211","1,8 milliard ufc"),
  ("Lacticaseibacillus rhamnosus","GG","800 millions ufc"),
  ("Bifidobacterium breve","NL-240","600 millions ufc"),
  ("Bifidobacterium bifidum","NL-236","200 millions ufc"),
  ("Bifidobacterium longum","NL-235","200 millions ufc"),
  ("Streptococcus thermophilus","NL-231","200 millions ufc"),
  ("Lactiplantibacillus plantarum","NL-210","160 millions ufc"),
  ("Lactobacillus acidophilus","NL-214","40 millions ufc"),
  ("Vitamine C","","15 mg","noital"),
 ],
 'nonmed':"Extrait de levure, tréhalose, capsules végétales (hypromellose), stéarate de magnésium, maltodextrine.",
 'posology':"<p><b>Adolescents (12 ans et plus) et adultes :</b> prendre une capsule deux fois par jour, au déjeuner et au souper.</p>\n          <p>Prendre au moins 2 à 3 heures avant ou après la prise d'antibiotiques ou antifongiques. Commencer 5 jours avant le voyage et continuer pendant toute sa durée.</p>",
 'stat':None,
 'shield_img':"https://static.wixstatic.com/media/623234_1401e0501d8b4cdf8951d0e73669c094~mv2.png",
 'forwhom_title':"Probaclac maintient votre santé en voyage.",
 'forwhom_ps':[
  "Plus de la moitié des voyageurs outre-mer souffrent de diarrhée, surtout ceux qui visitent le Moyen-Orient, l'Asie, l'Afrique, l'Amérique Centrale et du Sud. Une semaine avant de partir, prenez Probaclac Voyageurs pour éviter les pépins digestifs.",
  "Sa formule multi-souches diversifie votre profil bactérien pour mieux affronter les bactéries pathogènes des autres régions du Globe. Il contient en plus la souche <span class=\"italic\">Lactobacillus plantarum</span>, un anti-diarrhée. Prenez-le pendant votre séjour et dans la semaine suivant votre retour.",
 ],
},
]

if __name__=='__main__':
    for p in PRODUCTS: gen(p)

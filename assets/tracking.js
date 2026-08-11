/* ══════════════════════════════════════════════════════════════════
   PROBACLAC — Mesure (Google Tag Manager · GA4 · pixel Meta)
   Identifiants relevés sur le site live www.probaclac.ca (Wix), 2026-08-11.

     GTM   GTM-NSW3TFP5        conteneur (contient les tags GA4
                               add_to_cart et begin_checkout)
     GA4   G-HEREHR4J20        même propriété que le site actuel
     Meta  2440628703062561    pixel « probaclac.ca »

   ⚠ Deux pixels existent sur le compte Nicar Canada :
     · 2440628703062561 — « probaclac.ca »       (celui-ci)
     · 2510674395669106 — « Pixel de Probaclac »
   Le premier porte le nom du domaine et était déjà en place dans
   etudes.html / studies.html. Si la boutique utilise l'autre, il suffit
   de changer META_PIXEL_ID ci-dessous — un seul endroit, 108 pages.

   ⚠ GA4 est chargé ici avec l'envoi de page_view actif. Si le conteneur
   GTM contient AUSSI un tag de configuration GA4 qui envoie les pages,
   les vues seront comptées deux fois. Vérification : GA4 → Temps réel,
   charger une page, compter les page_view. S'il y en a deux, passer
   SEND_PAGE_VIEW à false ci-dessous.
   ══════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var GTM_ID = 'GTM-NSW3TFP5';
  var GA4_ID = 'G-HEREHR4J20';
  var META_PIXEL_ID = '2440628703062561';
  var SEND_PAGE_VIEW = true;

  /* ── Google Tag Manager ── */
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({ 'gtm.start': new Date().getTime(), event: 'gtm.js' });
  (function () {
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtm.js?id=' + GTM_ID;
    document.head.appendChild(s);
  })();

  /* ── GA4 (gtag) ── */
  (function () {
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA4_ID;
    document.head.appendChild(s);
  })();
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;
  gtag('js', new Date());
  gtag('config', GA4_ID, { send_page_view: SEND_PAGE_VIEW });

  /* ── Pixel Meta ── */
  (function (f, b, e, v, n, t, s) {
    if (f.fbq) return;
    n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
    if (!f._fbq) f._fbq = n;
    n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = [];
    t = b.createElement(e); t.async = !0; t.src = v;
    s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
  })(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
  window.fbq('init', META_PIXEL_ID);
  window.fbq('track', 'PageView');
})();

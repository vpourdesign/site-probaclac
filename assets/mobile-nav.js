/* ══════════════════════════════════════════════════════════════════
   PROBACLAC — Navigation mobile (≤ 860px)
   Construit le bouton et le panneau à partir du DOM déjà présent :
   CATALOGUE pour les produits, #megaAbout pour la section « À propos »,
   .nav__links pour les liens directs, .nav__lang pour la langue.
   Aucune URL n'est écrite en dur : les chemins relatifs restent donc
   corrects à la racine comme dans /blogue/ ou /en/blogue/.
   Les libellés viennent du DOM, donc FR et EN sortent traduits seuls.
   ══════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var nav = document.getElementById('nav');
  if (!nav || document.getElementById('navDrawer')) return;

  var links = nav.querySelector('.nav__links');
  var right = nav.querySelector('.nav__right');
  if (!links || !right) return;

  var ARROW = '<span class="arr" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>';

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }
  function label(el) {
    if (!el) return '';
    var t = el.cloneNode(true);
    Array.prototype.forEach.call(t.querySelectorAll('.chev, svg'), function (n) { n.remove(); });
    return t.textContent.trim();
  }

  /* ── Produits : CATALOGUE si présent, sinon la grille du méga-menu ── */
  function products() {
    var out = [];
    if (typeof CATALOGUE !== 'undefined' && Array.isArray(CATALOGUE)) {
      CATALOGUE.forEach(function (p) { out.push({ url: p.url, name: p.name, meta: p.meta }); });
      return out;
    }
    Array.prototype.forEach.call(document.querySelectorAll('#megaGrid a'), function (a) {
      var b = a.querySelector('b, .title');
      var s = a.querySelector('small, .meta');
      out.push({
        url: a.getAttribute('href'),
        name: b ? b.childNodes[0].textContent.trim() : a.textContent.trim(),
        meta: s ? s.textContent.trim() : ''
      });
    });
    return out;
  }

  /* ── « À propos » : les rangées du méga-menu correspondant ── */
  function about() {
    var out = [];
    Array.prototype.forEach.call(document.querySelectorAll('#megaAbout .about-row'), function (a) {
      var t = a.querySelector('.title');
      out.push({ url: a.getAttribute('href'), name: t ? t.textContent.trim() : a.textContent.trim() });
    });
    if (!out.length) {
      Array.prototype.forEach.call(document.querySelectorAll('#megaAbout a'), function (a) {
        out.push({ url: a.getAttribute('href'), name: a.textContent.trim() });
      });
    }
    return out;
  }

  /* ── Bouton ── */
  var burger = document.createElement('button');
  burger.className = 'navburger';
  burger.id = 'navBurger';
  burger.type = 'button';
  burger.setAttribute('aria-expanded', 'false');
  burger.setAttribute('aria-controls', 'navDrawer');
  burger.setAttribute('aria-label', document.documentElement.lang === 'en' ? 'Menu' : 'Menu');
  burger.innerHTML = '<span class="navburger__box" aria-hidden="true"><i></i><i></i><i></i></span>';
  right.appendChild(burger);

  /* ── Panneau ── */
  var prods = products();
  var abouts = about();
  var directs = Array.prototype.slice.call(links.querySelectorAll(':scope > a'));

  var html = '<div class="navdrawer__inner">';

  if (prods.length) {
    html += '<div class="navdrawer__grp"><span class="navdrawer__lbl">' +
      esc(label(document.getElementById('megaToggle'))) + '</span><div class="navdrawer__prods">';
    prods.forEach(function (p) {
      html += '<a class="navdrawer__prod" href="' + esc(p.url) + '"><b>' + esc(p.name) + '</b>' +
        (p.meta ? '<small>' + esc(p.meta) + '</small>' : '') + '</a>';
    });
    html += '</div></div>';
  }

  if (abouts.length) {
    html += '<div class="navdrawer__grp"><span class="navdrawer__lbl">' +
      esc(label(document.getElementById('aboutToggle'))) + '</span><div class="navdrawer__list">';
    abouts.forEach(function (a) {
      html += '<a class="navdrawer__link" href="' + esc(a.url) + '">' + esc(a.name) + ARROW + '</a>';
    });
    html += '</div></div>';
  }

  if (directs.length) {
    html += '<div class="navdrawer__grp"><div class="navdrawer__list">';
    directs.forEach(function (a) {
      html += '<a class="navdrawer__link" href="' + esc(a.getAttribute('href')) + '">' +
        esc(label(a)) + ARROW + '</a>';
    });
    html += '</div></div>';
  }

  /* Le sélecteur FR/EN reste visible dans la barre : pas de doublon ici. */

  html += '</div>';

  var drawer = document.createElement('div');
  drawer.className = 'navdrawer';
  drawer.id = 'navDrawer';
  drawer.hidden = false;
  drawer.setAttribute('aria-label', label(burger) || 'Menu');
  drawer.innerHTML = html;
  nav.parentNode.insertBefore(drawer, nav.nextSibling);

  /* ── Hauteur de la barre : le panneau démarre juste dessous ── */
  function navh() {
    document.documentElement.style.setProperty('--navh', nav.offsetHeight + 'px');
  }
  navh();
  window.addEventListener('resize', navh);

  /* ── Ouverture / fermeture ── */
  var open = false;

  function set(state) {
    open = state;
    drawer.classList.toggle('is-open', open);
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.classList.toggle('navdrawer-open', open);
    if (open && window.lenis && typeof window.lenis.stop === 'function') window.lenis.stop();
    if (!open && window.lenis && typeof window.lenis.start === 'function') window.lenis.start();
  }

  burger.addEventListener('click', function () {
    if (!open) {
      /* On ferme les méga-menus du bureau avant d'ouvrir le panneau. */
      ['megaToggle', 'aboutToggle'].forEach(function (id) {
        var b = document.getElementById(id);
        if (b && b.getAttribute('aria-expanded') === 'true') b.click();
      });
      navh();
    }
    set(!open);
  });

  drawer.addEventListener('click', function (e) {
    if (e.target.closest('a')) set(false);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && open) { set(false); burger.focus(); }
  });

  window.addEventListener('resize', function () {
    if (open && window.innerWidth > 860) set(false);
  });
})();

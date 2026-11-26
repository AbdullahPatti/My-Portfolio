(function () {
  'use strict';
  var nav = document.getElementById('nav');
  var toggle = document.getElementById('nav-toggle');
  var menu = document.getElementById('menu');

  // Glass nav gets denser once you scroll.
  function onScroll() { nav.classList.toggle('is-scrolled', window.scrollY > 20); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile menu.
  function setMenu(open) {
    toggle.setAttribute('aria-expanded', String(open));
    menu.classList.toggle('is-open', open);
  }
  toggle.addEventListener('click', function () { setMenu(toggle.getAttribute('aria-expanded') !== 'true'); });
  menu.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });

  // Reveal on scroll + active nav link.
  var links = {};
  document.querySelectorAll('.nav__links a').forEach(function (a) { links[a.getAttribute('href').slice(1)] = a; });
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });

    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting || !links[e.target.id]) return;
        Object.keys(links).forEach(function (k) { links[k].classList.toggle('is-active', k === e.target.id); });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    document.querySelectorAll('section[id]').forEach(function (s) { spy.observe(s); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('is-in'); });
  }

  // Stacking deck: each card pins, the next slides over it, the covered one recedes.
  var stacks = [].map.call(document.querySelectorAll('.stack'), function (s) { return [].slice.call(s.children); });
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function fit() {
    stacks.forEach(function (cards) {
      cards.forEach(function (c, i) {
        // Pin under the nav; a card taller than the screen pins by its bottom edge instead,
        // so it is fully read before the next one slides over it.
        c.style.top = Math.min(88 + i * 12, window.innerHeight - c.offsetHeight - 16) + 'px';
      });
    });
    depth();
  }
  function depth() {
    if (reduce) return;
    stacks.forEach(function (cards) {
      cards.forEach(function (c, i) {
        var next = cards[i + 1];
        if (!next) { c.style.transform = ''; c.style.filter = ''; return; }
        var a = c.getBoundingClientRect(), b = next.getBoundingClientRect();
        var p = Math.min(1, Math.max(0, (a.bottom - b.top) / a.height));
        c.style.transform = p ? 'scale(' + (1 - p * 0.06).toFixed(4) + ')' : '';
        c.style.filter = p ? 'brightness(' + (1 - p * 0.07).toFixed(3) + ')' : '';
      });
    });
  }
  var ticking = false;
  window.addEventListener('scroll', function () {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () { depth(); ticking = false; });
  }, { passive: true });
  window.addEventListener('resize', fit);
  document.querySelectorAll('.more').forEach(function (d) { d.addEventListener('toggle', fit); });
  window.addEventListener('load', fit);
  fit();

  // Contact form via Formspree, without leaving the page.
  var form = document.getElementById('contact-form');
  var status = document.getElementById('form-status');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    status.textContent = 'Sending…';
    fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
      .then(function (r) {
        if (!r.ok) throw new Error();
        form.reset();
        status.textContent = 'Thanks, I’ll get back to you soon.';
      })
      .catch(function () { status.textContent = 'Couldn’t send. Please email me directly.'; });
  });

  document.getElementById('year').textContent = new Date().getFullYear();
})();

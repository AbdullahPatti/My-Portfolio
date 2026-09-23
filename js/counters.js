(function () {
  var strip = document.getElementById('stat-strip');
  if (!strip) return;
  function run() {
    strip.querySelectorAll('[data-target]').forEach(function (el) {
      var target = Number(el.getAttribute('data-target')); var suffix = el.getAttribute('data-suffix') || ''; var start = performance.now();
      function tick(now) { var progress = Math.min((now - start) / 820, 1); el.textContent = Math.round(target * (1 - Math.pow(1 - progress, 4))).toLocaleString() + suffix; if (progress < 1) requestAnimationFrame(tick); }
      requestAnimationFrame(tick);
    });
  }
  if (!('IntersectionObserver' in window)) { run(); return; }
  var observer = new IntersectionObserver(function (entries) { if (entries[0].isIntersecting) { run(); observer.disconnect(); } }, { threshold: .3 });
  observer.observe(strip);

  var research = document.getElementById('research');
  if (!research || !('IntersectionObserver' in window)) return;
  var researchObserver = new IntersectionObserver(function (entries) {
    if (!entries[0].isIntersecting) return;
    research.querySelectorAll('.paper-metrics strong').forEach(function (el) {
      var raw = el.textContent.trim();
      if (!/^\d{1,6}$/.test(raw)) return;
      var target = Number(raw), start = performance.now();
      function tick(now) { var p = Math.min((now - start) / 720, 1); el.textContent = Math.round(target * (1 - Math.pow(1 - p, 4))).toLocaleString(); if (p < 1) requestAnimationFrame(tick); }
      el.textContent = '0'; requestAnimationFrame(tick);
    });
    researchObserver.disconnect();
  }, { threshold: .25 });
  researchObserver.observe(research);
})();

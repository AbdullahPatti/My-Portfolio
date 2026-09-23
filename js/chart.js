(function () {
  var charts = document.querySelectorAll('.chart');
  if (!charts.length) return;

  function run(chart) {
    var bars = chart.querySelectorAll('.chart-bar');
    var values = chart.querySelectorAll('.chart-row-value');
    var maxVal = 0.771;

    bars.forEach(function (bar) {
      var target = parseFloat(bar.getAttribute('data-target'));
      var pct = (target / maxVal) * 100;
      requestAnimationFrame(function () { bar.style.width = pct + '%'; });
    });

    values.forEach(function (val) {
      var target = parseFloat(val.getAttribute('data-value'));
      var duration = 1100;
      var start = null;

      function step(ts) {
        if (!start) start = ts;
        var progress = Math.min((ts - start) / duration, 1);
        val.textContent = (target * progress).toFixed(3);
        if (progress < 1) requestAnimationFrame(step);
        else val.textContent = target.toFixed(3);
      }
      requestAnimationFrame(step);
    });
  }

  if (!('IntersectionObserver' in window)) {
    charts.forEach(run);
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        run(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  charts.forEach(function (c) { observer.observe(c); });
})();

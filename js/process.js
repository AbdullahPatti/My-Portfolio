(function () {
  var track = document.getElementById('process-track');
  if (!track) return;
  var steps = Array.prototype.slice.call(track.querySelectorAll('.process-step'));
  function update() {
    var rect = track.getBoundingClientRect();
    var progress = Math.max(0, Math.min(1, (window.innerHeight * .68 - rect.top) / Math.max(rect.height, 1)));
    track.style.setProperty('--progress', (progress * 100) + '%');
    var active = Math.min(steps.length - 1, Math.floor(progress * steps.length));
    steps.forEach(function (step, index) {
      step.classList.toggle('is-active', index === active);
      step.classList.toggle('is-done', index < active);
      step.classList.toggle('is-upcoming', index > active);
    });
  }
  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update); update();
})();

(function () {
  var heroKicker = document.querySelector('.hero-copy .kicker');
  if (heroKicker) heroKicker.textContent = 'AI · SOFTWARE · RESEARCH';
  var progress = document.getElementById('scroll-progress');
  function updateProgress() { var max = document.documentElement.scrollHeight - window.innerHeight; if (progress) progress.style.width = (max > 0 ? (window.scrollY / max) * 100 : 0) + '%'; }
  window.addEventListener('scroll', updateProgress, { passive: true }); updateProgress();
  var year = document.getElementById('footer-year');
  if (year) year.innerHTML = '&copy; ' + new Date().getFullYear() + ' Muhammad Abdullah Haroon.';
})();

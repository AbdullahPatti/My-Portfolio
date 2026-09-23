(function () {
  var clock = document.getElementById('live-clock');
  if (!clock) return;
  function update() { clock.textContent = new Intl.DateTimeFormat('en-PK', { timeZone: 'Asia/Karachi', hour: '2-digit', minute: '2-digit', hour12: true }).format(new Date()) + ' PKT'; }
  update(); setInterval(update, 30000);
})();

(function () {
  var form = document.getElementById('contact-form');
  var status = document.getElementById('form-status');

  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var data = new FormData(form);
      status.textContent = 'Sending…';
      status.style.color = 'var(--text-faint)';

      fetch(form.action, {
        method: 'POST',
        body: data,
        headers: { 'Accept': 'application/json' }
      }).then(function (res) {
        if (res.ok) {
          status.textContent = 'Sent. I\u2019ll reply soon.';
          status.style.color = 'var(--signal)';
          form.reset();
        } else {
          status.textContent = 'Form isn\u2019t connected yet, use the email link below.';
          status.style.color = 'var(--danger)';
        }
      }).catch(function () {
        status.textContent = 'Couldn\u2019t send, use the email link below.';
        status.style.color = 'var(--danger)';
      });
    });
  }
})();

(function () {
  var copyBtn = document.getElementById('copy-btn');
  var copyLabel = document.getElementById('copy-btn-label');
  if (!copyBtn) return;

  copyBtn.addEventListener('click', function (e) {
    e.preventDefault();
    e.stopPropagation();
    var email = copyBtn.dataset.email || '';
    navigator.clipboard.writeText(email).then(function () {
      copyLabel.textContent = 'copied';
      setTimeout(function () { copyLabel.textContent = 'copy'; }, 1600);
    }).catch(function () {
      copyLabel.textContent = 'ctrl+c';
    });
  });
})();

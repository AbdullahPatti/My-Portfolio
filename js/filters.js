(function () {
  var filterBtns = document.querySelectorAll('.filter-btn');
  var cards = document.querySelectorAll('.case-study');
  var pills = document.querySelectorAll('[data-tag]');

  function applyFilter(tag) {
    filterBtns.forEach(function (b) {
      b.classList.toggle('active', b.getAttribute('data-filter') === tag);
    });
    cards.forEach(function (card) {
      var tags = (card.getAttribute('data-tags') || '').split(' ');
      var show = tag === 'all' || tags.indexOf(tag) !== -1;
      card.classList.toggle('hidden', !show);
    });
  }

  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      applyFilter(btn.getAttribute('data-filter'));
    });
  });

  pills.forEach(function (pill) {
    pill.addEventListener('click', function () {
      var tag = pill.getAttribute('data-tag');
      applyFilter(tag);
      var target = document.getElementById('projects');
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
})();

(function () {
  var nav = document.getElementById('site-nav');
  var links = Array.prototype.slice.call(document.querySelectorAll('[data-nav]'));

  function setActiveLink() {
    var activeId = null;
    var scrollPos = window.scrollY + 120;
    document.querySelectorAll('main section[id]').forEach(function (section) {
      if (section.offsetTop <= scrollPos) activeId = section.id;
    });

    links.forEach(function (link) {
      var isActive = link.getAttribute('href') === '#' + activeId;
      link.classList.toggle('active', isActive);
    });
  }

  setActiveLink();
  window.addEventListener('scroll', function () { if (nav) nav.classList.toggle('scrolled', window.scrollY > 8); setActiveLink(); }, { passive: true });
})();

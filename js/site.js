(function () {
  'use strict';

  var nav = document.getElementById('site-nav');
  var year = document.getElementById('footer-year');
  var form = document.getElementById('contact-form');
  var status = document.getElementById('form-status');
  var heroEmailBtn = document.getElementById('hero-email-btn');
  var copyEmailBtn = document.getElementById('copy-email-btn');
  var copyEmailText = document.getElementById('copy-email-text');
  var toast = document.getElementById('copy-toast');
  var toastMessage = document.getElementById('toast-message');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ============ NAVBAR SCROLL EFFECT ============ */
  function onScroll() {
    if (nav) {
      if (window.scrollY > 20) {
        nav.classList.add('is-scrolled');
      } else {
        nav.classList.remove('is-scrolled');
      }
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ============ ACTIVE NAVIGATION TRACKER ============ */
  var sections = document.querySelectorAll('[data-nav]');
  var navLinks = document.querySelectorAll('.nav-desktop a[href^="#"], .mobile-menu-links a[href^="#"]');

  function updateActiveNav() {
    var scrollY = window.scrollY + window.innerHeight * 0.35;
    var active = null;
    sections.forEach(function (sec) {
      if (sec.offsetTop <= scrollY) active = sec;
    });
    navLinks.forEach(function (link) {
      var href = link.getAttribute('href');
      if (!href || href.charAt(0) !== '#') return;
      var match = active && href === '#' + active.id;
      link.classList.toggle('active', !!match);
    });
  }
  window.addEventListener('scroll', updateActiveNav, { passive: true });
  updateActiveNav();

  /* ============ MOBILE MENU DRAWER ============ */
  var navToggle = document.getElementById('nav-toggle');
  var mobileMenu = document.getElementById('mobile-menu');

  function openMobileMenu() {
    if (!navToggle || !mobileMenu) return;
    navToggle.classList.add('is-open');
    navToggle.setAttribute('aria-expanded', 'true');
    mobileMenu.classList.add('is-open');
    mobileMenu.setAttribute('aria-hidden', 'false');
    document.body.classList.add('menu-locked');
  }

  function closeMobileMenu() {
    if (!navToggle || !mobileMenu) return;
    navToggle.classList.remove('is-open');
    navToggle.setAttribute('aria-expanded', 'false');
    mobileMenu.classList.remove('is-open');
    mobileMenu.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('menu-locked');
  }

  if (navToggle) {
    navToggle.addEventListener('click', function (e) {
      e.stopPropagation();
      var isOpen = navToggle.classList.contains('is-open');
      if (isOpen) {
        closeMobileMenu();
      } else {
        openMobileMenu();
      }
    });
  }

  if (mobileMenu) {
    mobileMenu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        closeMobileMenu();
      });
    });
  }

  window.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && navToggle && navToggle.classList.contains('is-open')) {
      closeMobileMenu();
    }
  });

  /* ============ FOOTER YEAR ============ */
  if (year) {
    year.innerHTML = '&copy; ' + new Date().getFullYear() + ' Muhammad Abdullah Haroon';
  }

  /* ============ SCROLL REVEAL ANIMATIONS ============ */
  var reveals = document.querySelectorAll('.reveal');
  function revealElement(el) {
    el.classList.add('in');
  }

  if (reduce) {
    reveals.forEach(revealElement);
  } else if ('IntersectionObserver' in window) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          revealElement(entry.target);
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });

    reveals.forEach(function (el) {
      revealObserver.observe(el);
    });
  } else {
    reveals.forEach(revealElement);
  }

  /* ============ STACKING CARDS (publications & projects) ============ */
  // Each card sticks just under the nav, a few px lower than the one before.
  // Cards taller than the viewport stick by their bottom edge so they are
  // read in full before the next card slides over them.
  var stacks = document.querySelectorAll('.pub-list, .projects-stack');
  var stackTicking = false;

  function layoutStacks() {
    var navH = nav ? nav.offsetHeight : 52;
    stacks.forEach(function (stack) {
      var cards = stack.querySelectorAll('.stack-card');
      cards.forEach(function (card, i) {
        var top = Math.min(navH + 16 + i * 10, window.innerHeight - card.offsetHeight - 16);
        card.style.top = top + 'px';
      });
    });
    updateStacks();
  }

  function updateStacks() {
    stackTicking = false;
    if (reduce) return;
    stacks.forEach(function (stack) {
      var cards = stack.querySelectorAll('.stack-card');
      for (var i = 0; i < cards.length; i++) {
        var next = cards[i + 1];
        var p = 0;
        if (next) {
          var top = cards[i].getBoundingClientRect().top;
          var h = cards[i].offsetHeight;
          p = (top + h - next.getBoundingClientRect().top) / h;
          p = Math.max(0, Math.min(1, p));
        }
        cards[i].style.setProperty('--stack-p', p.toFixed(3));
      }
    });
  }

  if (stacks.length) {
    window.addEventListener('scroll', function () {
      if (!stackTicking) {
        stackTicking = true;
        requestAnimationFrame(updateStacks);
      }
    }, { passive: true });
    window.addEventListener('resize', layoutStacks, { passive: true });
    window.addEventListener('load', layoutStacks);
    layoutStacks();
  }

  /* ============ STATS COUNTER ANIMATION ============ */
  var strip = document.getElementById('stat-strip');
  function animateCounters() {
    if (!strip) return;
    strip.querySelectorAll('[data-count]').forEach(function (el) {
      var target = Number(el.getAttribute('data-count'));
      var suffix = el.getAttribute('data-suffix') || '';
      if (reduce) {
        el.textContent = target + suffix;
        return;
      }
      var startTime = performance.now();
      var duration = 1200;

      function tick(now) {
        var elapsed = now - startTime;
        var progress = Math.min(elapsed / duration, 1);
        var eased = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
        var current = Math.round(target * eased);
        el.textContent = current + suffix;
        if (progress < 1) {
          requestAnimationFrame(tick);
        } else {
          el.textContent = target + suffix;
        }
      }
      requestAnimationFrame(tick);
    });
  }

  if (strip && 'IntersectionObserver' in window) {
    var statObserver = new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) {
        animateCounters();
        statObserver.disconnect();
      }
    }, { threshold: 0.2 });
    statObserver.observe(strip);
  } else {
    animateCounters();
  }

  /* ============ PROCESS VERTICAL TIMELINE SCROLL TRACKER ============ */
  var processTimeline = document.getElementById('process-timeline');
  var processRailFill = document.getElementById('process-rail-fill');
  var processSteps = document.querySelectorAll('.process-step-item');

  function updateProcessScroll() {
    if (!processTimeline || !processRailFill || !processSteps.length) return;
    
    var rect = processTimeline.getBoundingClientRect();
    var viewH = window.innerHeight;
    var focusY = viewH * 0.5; // Focus line in viewport
    
    // Calculate progress through timeline
    var start = rect.top;
    var totalHeight = rect.height;
    var progress = (focusY - start) / totalHeight;
    progress = Math.max(0, Math.min(1, progress));

    if (reduce) {
      processRailFill.style.height = '100%';
    } else {
      processRailFill.style.height = (progress * 100) + '%';
    }

    // Determine currently focused step item
    var activeIndex = -1;
    var minDistance = Infinity;

    processSteps.forEach(function (step, idx) {
      var stepRect = step.getBoundingClientRect();
      var stepCenter = stepRect.top + stepRect.height * 0.4;
      var dist = Math.abs(stepCenter - focusY);

      if (dist < minDistance && stepRect.top < viewH && stepRect.bottom > 0) {
        minDistance = dist;
        activeIndex = idx;
      }
    });

    processSteps.forEach(function (step, idx) {
      step.classList.toggle('is-active', idx === activeIndex);
    });
  }

  window.addEventListener('scroll', updateProcessScroll, { passive: true });
  window.addEventListener('resize', updateProcessScroll, { passive: true });
  updateProcessScroll();

  /* ============ CLIPBOARD AND TOAST UTILITIES ============ */
  var toastTimer = null;
  function showCopyToast(msg) {
    if (!toast) return;
    if (toastMessage && msg) {
      toastMessage.textContent = msg;
    }
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      toast.classList.remove('show');
    }, 2800);
  }

  function copyTextToClipboard(text, onSuccess) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        if (onSuccess) onSuccess();
      }).catch(function () {
        fallbackCopy(text, onSuccess);
      });
    } else {
      fallbackCopy(text, onSuccess);
    }
  }

  function fallbackCopy(text, onSuccess) {
    var tempInput = document.createElement('textarea');
    tempInput.value = text;
    tempInput.style.position = 'fixed';
    tempInput.style.left = '-9999px';
    tempInput.style.top = '-9999px';
    document.body.appendChild(tempInput);
    tempInput.focus();
    tempInput.select();
    try {
      document.execCommand('copy');
      if (onSuccess) onSuccess();
    } catch (e) {
      console.warn('Clipboard copy failed', e);
    }
    document.body.removeChild(tempInput);
  }

  /* ============ HERO EMAIL ME BUTTON ============ */
  if (heroEmailBtn) {
    heroEmailBtn.addEventListener('click', function (e) {
      var email = 'abdullaharoon.work@gmail.com';
      // Copy to clipboard immediately
      copyTextToClipboard(email, function () {
        showCopyToast('Email copied: ' + email);
      });
      // Also attempt mail client launch
      setTimeout(function () {
        window.location.href = 'mailto:' + email;
      }, 100);
    });
  }

  /* ============ BOTTOM COPY EMAIL BUTTON ============ */
  if (copyEmailBtn) {
    copyEmailBtn.addEventListener('click', function (e) {
      e.preventDefault();
      var email = 'abdullaharoon.work@gmail.com';
      copyTextToClipboard(email, function () {
        showCopyToast('Email address copied to clipboard!');
        if (copyEmailText) {
          var original = copyEmailText.textContent;
          copyEmailText.textContent = 'Copied to clipboard!';
          setTimeout(function () {
            copyEmailText.textContent = original;
          }, 2000);
        }
      });
    });
  }

  /* ============ CONTACT FORM HANDLER ============ */
  if (form && status) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      status.textContent = 'Sending message…';
      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      }).then(function (res) {
        if (res.ok) {
          status.textContent = '✓ Message sent. I will get back to you soon.';
          status.style.color = '#34c759';
          form.reset();
        } else {
          status.textContent = 'Could not send. Please use the direct email below.';
          status.style.color = '#ff3b30';
        }
      }).catch(function () {
        status.textContent = 'Network error. Please use the direct email below.';
        status.style.color = '#ff3b30';
      });
    });
  }

  /* ============ SMOOTH SCROLLING FOR HASH LINKS ============ */
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var href = link.getAttribute('href');
      if (!href || href === '#') return;
      var target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

})();

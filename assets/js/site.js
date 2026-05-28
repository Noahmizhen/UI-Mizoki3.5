/* MIZOKI3 — Shared subpage interactions */

(function () {
  'use strict';

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  document.body.classList.add('page-sub');
  requestAnimationFrame(function () {
    document.body.classList.add('is-loaded');
  });

  var nav = document.querySelector('.site-nav');
  var toggle = document.querySelector('.nav-toggle');
  var panel = document.querySelector('.mobile-panel');
  var backdrop = document.querySelector('.mobile-backdrop');

  function setNavSolid() {
    if (!nav) return;
    nav.classList.toggle('is-solid', window.scrollY > 48);
  }

  function closeMobileMenu() {
    if (!toggle || !panel || !backdrop) return;
    toggle.setAttribute('aria-expanded', 'false');
    panel.classList.remove('is-open');
    backdrop.classList.remove('is-open');
    document.body.style.overflow = '';
  }

  function openMobileMenu() {
    if (!toggle || !panel || !backdrop) return;
    toggle.setAttribute('aria-expanded', 'true');
    panel.classList.add('is-open');
    backdrop.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  }

  if (toggle) {
    toggle.addEventListener('click', function () {
      if (toggle.getAttribute('aria-expanded') === 'true') closeMobileMenu();
      else openMobileMenu();
    });
  }

  if (backdrop) backdrop.addEventListener('click', closeMobileMenu);
  if (panel) panel.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', closeMobileMenu);
  });

  window.addEventListener('scroll', setNavSolid, { passive: true });
  setNavSolid();

  function loadBackground(el) {
    var src = el.getAttribute('data-bg');
    if (!src) return;
    el.style.backgroundImage = 'url("' + src + '")';
    el.classList.add('is-loaded');
    el.style.opacity = '1';
    el.style.transition = 'opacity 1.2s ease';
  }

  document.querySelectorAll('.section-bg[data-bg]').forEach(function (el) {
    if (el.classList.contains('section-bg--immediate')) {
      loadBackground(el);
      return;
    }
    if ('IntersectionObserver' in window) {
      var obs = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            loadBackground(entry.target);
            obs.unobserve(entry.target);
          }
        });
      }, { rootMargin: '200px 0px' });
      obs.observe(el);
    } else {
      loadBackground(el);
    }
  });

  if ('IntersectionObserver' in window && !reducedMotion) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.reveal').forEach(function (el) {
      revealObserver.observe(el);
    });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) {
      el.classList.add('is-visible');
    });
  }

  var parallaxEls = document.querySelectorAll('[data-parallax]');

  function updateParallax() {
    if (reducedMotion) return;
    parallaxEls.forEach(function (section) {
      var bg = section.querySelector('.section-bg');
      if (!bg) return;
      var rect = section.getBoundingClientRect();
      var center = rect.top + rect.height * 0.5;
      var viewCenter = window.innerHeight * 0.5;
      var offset = (center - viewCenter) * 0.25;
      bg.style.transform = 'translate3d(0, ' + offset + 'px, 0)';
    });
  }

  if (parallaxEls.length && !reducedMotion) {
    window.addEventListener('scroll', updateParallax, { passive: true });
    updateParallax();
  }
})();

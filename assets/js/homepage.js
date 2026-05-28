/* MIZOKI3 — Homepage: knowledge graph, parallax, scroll reveals */

(function () {
  'use strict';

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* —— Navigation —— */
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
      if (toggle.getAttribute('aria-expanded') === 'true') {
        closeMobileMenu();
      } else {
        openMobileMenu();
      }
    });
  }

  if (backdrop) {
    backdrop.addEventListener('click', closeMobileMenu);
  }

  panel && panel.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', closeMobileMenu);
  });

  window.addEventListener('scroll', setNavSolid, { passive: true });
  setNavSolid();

  /* —— Hero load sequence —— */
  var heroLoad = document.querySelector('.hero-load');
  if (heroLoad) {
    requestAnimationFrame(function () {
      heroLoad.classList.add('is-ready');
    });
  }

  var heroBg = document.querySelector('.section-bg--hero');
  if (heroBg) {
    heroBg.style.opacity = '1';
  }

  /* —— Lazy-load below-fold backgrounds —— */
  function loadBackground(el) {
    var src = el.getAttribute('data-bg');
    if (!src) return;
    el.style.backgroundImage = 'url("' + src + '")';
    el.classList.add('is-loaded');
    el.style.opacity = '1';
    el.style.transition = 'opacity 1.2s ease';
  }

  if ('IntersectionObserver' in window) {
    var bgObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          loadBackground(entry.target);
          bgObserver.unobserve(entry.target);
        }
      });
    }, { rootMargin: '200px 0px' });

    document.querySelectorAll('.section-bg[data-bg]').forEach(function (el) {
      bgObserver.observe(el);
    });
  } else {
    document.querySelectorAll('.section-bg[data-bg]').forEach(loadBackground);
  }

  /* —— Scroll reveals —— */
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

  /* —— Parallax —— */
  var parallaxEls = document.querySelectorAll('[data-parallax]');

  function updateParallax() {
    if (reducedMotion) return;
    var scrollY = window.scrollY;
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

  /* —— Ambient data texture —— */
  var ambient = document.querySelector('.ambient-data');
  if (ambient && !reducedMotion) {
    var chars = '0123456789ABCDEF';
    var lines = [];
    for (var i = 0; i < 18; i++) {
      var line = '';
      for (var j = 0; j < 48; j++) {
        line += chars[Math.floor(Math.random() * chars.length)];
      }
      lines.push(line);
    }
    ambient.textContent = lines.join('\n');
  }

  /* —— Knowledge graph canvas —— */
  var canvas = document.getElementById('kg-canvas');
  if (!canvas || reducedMotion) {
    if (canvas) canvas.style.display = 'none';
    return;
  }

  var ctx = canvas.getContext('2d');
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var w, h;
  var nodes = [];
  var edges = [];
  var nodeCount = 50;
  var time = 0;
  var lastEdgeTime = 0;
  var nextEdgeIn = 6;
  var rafId = null;

  function rand(min, max) {
    return min + Math.random() * (max - min);
  }

  function initGraph() {
    nodes = [];
    edges = [];
    for (var i = 0; i < nodeCount; i++) {
      var nx = rand(0.45, 0.98);
      var ny = rand(0.05, 0.75);
      nodes.push({
        x: nx,
        y: ny,
        r: rand(1.5, 3.5),
        pulse: rand(0, Math.PI * 2),
        pulseSpeed: rand(0.4, 0.9),
      });
    }
    for (var j = 0; j < nodeCount * 0.8; j++) {
      var a = Math.floor(Math.random() * nodeCount);
      var b = Math.floor(Math.random() * nodeCount);
      if (a !== b) {
        edges.push({ a: a, b: b, progress: 1, born: 0 });
      }
    }
  }

  function resizeCanvas() {
    w = window.innerWidth;
    h = window.innerHeight;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    canvas.style.width = w + 'px';
    canvas.style.height = h + 'px';
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.scale(dpr, dpr);
  }

  function addEdge() {
    if (edges.length > nodeCount * 1.2) return;
    var a = Math.floor(Math.random() * nodeCount);
    var b = Math.floor(Math.random() * nodeCount);
    if (a === b) return;
    edges.push({ a: a, b: b, progress: 0, born: time });
  }

  function drawGraph() {
    ctx.clearRect(0, 0, w, h);

    var scrollFade = Math.max(0.15, 1 - window.scrollY / (h * 1.2));
    ctx.globalAlpha = scrollFade;

    edges.forEach(function (edge) {
      var na = nodes[edge.a];
      var nb = nodes[edge.b];
      if (!na || !nb) return;

      if (edge.progress < 1) {
        edge.progress = Math.min(1, edge.progress + 0.008);
      }

      var x1 = na.x * w;
      var y1 = na.y * h;
      var x2 = nb.x * w;
      var y2 = nb.y * h;
      var px = x1 + (x2 - x1) * edge.progress;
      var py = y1 + (y2 - y1) * edge.progress;

      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(px, py);
      ctx.strokeStyle = 'rgba(201, 168, 85, 0.15)';
      ctx.lineWidth = 0.75;
      ctx.stroke();
    });

    nodes.forEach(function (node) {
      var pulse = 0.2 + 0.3 * (0.5 + 0.5 * Math.sin(time * node.pulseSpeed + node.pulse));
      var cx = node.x * w;
      var cy = node.y * h;

      ctx.beginPath();
      ctx.arc(cx, cy, node.r, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(201, 168, 85, ' + pulse + ')';
      ctx.fill();
    });

    ctx.globalAlpha = 1;
  }

  function tick(ts) {
    time = ts * 0.001;
    if (time - lastEdgeTime > nextEdgeIn) {
      addEdge();
      lastEdgeTime = time;
      nextEdgeIn = rand(5, 8);
    }
    drawGraph();
    rafId = requestAnimationFrame(tick);
  }

  initGraph();
  resizeCanvas();
  window.addEventListener('resize', resizeGraph, { passive: true });

  function resizeGraph() {
    resizeCanvas();
  }

  rafId = requestAnimationFrame(tick);

  document.addEventListener('visibilitychange', function () {
    if (document.hidden) {
      if (rafId) cancelAnimationFrame(rafId);
      rafId = null;
    } else if (!rafId) {
      rafId = requestAnimationFrame(tick);
    }
  });
})();

/* MIZOKI3 — Interactive TCO-KG hero (ACT-991 narrative) */

(function () {
  'use strict';

  var canvas = document.getElementById('tckgCanvas');
  if (!canvas) return;

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ctx = canvas.getContext('2d');
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var w, h, mx = -1, my = -1, hoverId = null, paused = false;
  var time = 0;
  var phaseIndex = 0;
  var phaseT = 0;
  var particles = [];

  var COLORS = {
    counsel: '#7a9cc4',
    capital: '#d4ad78',
    risk: '#d47272',
    core: '#f0ebe3',
    muted: '#7a7468',
    line: 'rgba(236,232,224,0.18)',
  };

  var nodes = [
    { id: 'amend', label: 'AMEND-842', sub: 'Counsel', nx: 0.5, ny: 0.13, r: 22, color: COLORS.counsel },
    { id: 'cov01', label: 'COV-01', sub: 'Min $10M', nx: 0.5, ny: 0.43, r: 30, color: COLORS.core, core: true },
    { id: 'acme', label: 'Acme Holdings', sub: 'Entity graph', nx: 0.5, ny: 0.84, r: 19, color: '#b0a898' },
    { id: 'act991', label: '$5M', sub: 'ACT-991', nx: 0.14, ny: 0.66, r: 19, color: COLORS.capital },
    { id: 'risk', label: 'Gate', sub: 'Vetoed', nx: 0.86, ny: 0.5, r: 19, color: COLORS.risk, veto: true },
  ];

  var edges = [
    { id: 'e1', from: 'amend', to: 'cov01' },
    { id: 'e2', from: 'cov01', to: 'acme' },
    { id: 'e3', from: 'act991', to: 'cov01' },
    { id: 'e4', from: 'act991', to: 'risk', veto: true },
    { id: 'e5', from: 'cov01', to: 'risk', veto: true },
  ];

  var phases = [
    { ms: 3200, trace: 0, edges: ['e1'], nodes: ['amend', 'cov01'] },
    { ms: 3200, trace: 1, edges: ['e3'], nodes: ['act991', 'cov01'] },
    { ms: 4200, trace: 2, edges: ['e4', 'e5'], nodes: ['act991', 'cov01', 'risk'] },
  ];

  var nodeMap = {};
  nodes.forEach(function (n) { nodeMap[n.id] = n; });

  function resize() {
    var box = canvas.parentElement;
    w = box.clientWidth;
    h = box.clientHeight || 260;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    canvas.style.width = w + 'px';
    canvas.style.height = h + 'px';
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.scale(dpr, dpr);
    layoutNodes();
  }

  function layoutNodes() {
    var px = paused ? 0 : (mx >= 0 ? (mx / w - 0.5) * 8 : 0);
    var py = paused ? 0 : (my >= 0 ? (my / h - 0.5) * 6 : 0);
    nodes.forEach(function (n) {
      n.x = n.nx * w + px * (n.core ? 0.25 : 1);
      n.y = n.ny * h + py * (n.core ? 0.25 : 1);
    });
  }

  function hoverPhase(id) {
    var map = {
      amend: { trace: 0, edges: ['e1'], nodes: ['amend', 'cov01'] },
      cov01: { trace: 1, edges: ['e1', 'e3', 'e5'], nodes: ['amend', 'cov01', 'act991', 'risk'] },
      acme: { trace: 0, edges: ['e2'], nodes: ['acme', 'cov01'] },
      act991: { trace: 1, edges: ['e3', 'e4'], nodes: ['act991', 'cov01', 'risk'] },
      risk: { trace: 2, edges: ['e4', 'e5'], nodes: ['act991', 'cov01', 'risk'] },
    };
    return map[id] || phases[phaseIndex];
  }

  function activePhase() {
    return hoverId ? hoverPhase(hoverId) : phases[phaseIndex];
  }

  function syncTrace(index) {
    document.querySelectorAll('.trace-list [data-trace]').forEach(function (el, i) {
      el.classList.toggle('trace-active', i === index);
    });
    var hint = document.getElementById('graphPhaseHint');
    if (hint) {
      hint.textContent = [
        'Counsel maps obligation into graph memory',
        'Liquidity projected post-action',
        'Gate halts execution — arithmetic cited',
      ][index] || '';
    }
    var panel = document.querySelector('.product-panel');
    if (panel) panel.classList.toggle('gate-active', index === 2);
  }

  function spawnParticle(edge) {
    if (reduced || particles.length > 40) return;
    particles.push({
      edge: edge,
      t: 0,
      speed: edge.veto ? 0.018 : 0.014,
      color: edge.veto ? COLORS.risk : COLORS.capital,
      size: edge.veto ? 4 : 3.5,
    });
  }

  function drawGrid() {
    ctx.strokeStyle = 'rgba(236,232,224,0.05)';
    ctx.lineWidth = 1;
    var step = 20;
    for (var x = 0; x < w; x += step) {
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
    }
    for (var y = 0; y < h; y += step) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
    }
  }

  function edgePoints(edge) {
    var a = nodeMap[edge.from];
    var b = nodeMap[edge.to];
    var dx = b.x - a.x, dy = b.y - a.y;
    var len = Math.sqrt(dx * dx + dy * dy) || 1;
    return {
      sx: a.x + (dx / len) * a.r,
      sy: a.y + (dy / len) * a.r,
      ex: b.x - (dx / len) * b.r,
      ey: b.y - (dy / len) * b.r,
    };
  }

  function drawEdge(edge, phase, glow) {
    var active = phase.edges.indexOf(edge.id) >= 0;
    var pts = edgePoints(edge);
    ctx.beginPath();
    ctx.moveTo(pts.sx, pts.sy);
    ctx.lineTo(pts.ex, pts.ey);
    ctx.lineWidth = active ? 2.5 : 1;
    if (edge.veto && active) {
      ctx.strokeStyle = 'rgba(212,114,114,' + (0.55 + glow * 0.4) + ')';
      ctx.setLineDash([6, 4]);
    } else if (active) {
      ctx.strokeStyle = 'rgba(212,173,120,' + (0.5 + glow * 0.45) + ')';
      ctx.setLineDash([]);
    } else {
      ctx.strokeStyle = COLORS.line;
      ctx.setLineDash(edge.veto ? [4, 6] : []);
    }
    ctx.stroke();
    ctx.setLineDash([]);

    if (active && !reduced) {
      if (Math.random() < 0.12) spawnParticle(edge);
      ctx.beginPath();
      ctx.moveTo(pts.sx, pts.sy);
      ctx.lineTo(pts.ex, pts.ey);
      ctx.strokeStyle = edge.veto
        ? 'rgba(212,114,114,0.15)'
        : 'rgba(212,173,120,0.2)';
      ctx.lineWidth = 8;
      ctx.stroke();
    }
  }

  function drawNode(node, phase, glow) {
    var active = phase.nodes.indexOf(node.id) >= 0;
    var pulse = active ? 0.5 + 0.5 * Math.sin(time * 4) : 0;
    var r = node.r + pulse * 3;

    if (node.core) {
      ctx.beginPath();
      ctx.arc(node.x, node.y, r + 20 + pulse * 4, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(212,173,120,' + (active ? 0.25 + glow * 0.2 : 0.08) + ')';
      ctx.lineWidth = 1;
      ctx.stroke();
    }

    if (active) {
      ctx.beginPath();
      ctx.arc(node.x, node.y, r + 16, 0, Math.PI * 2);
      ctx.fillStyle = node.veto
        ? 'rgba(212,114,114,' + (0.12 + glow * 0.1) + ')'
        : 'rgba(212,173,120,' + (0.1 + glow * 0.08) + ')';
      ctx.fill();
    }

    ctx.beginPath();
    ctx.arc(node.x, node.y, r, 0, Math.PI * 2);
    ctx.fillStyle = node.veto ? 'rgba(212,114,114,0.2)' : '#141a24';
    ctx.fill();
    ctx.lineWidth = active ? 2 : 1;
    ctx.strokeStyle = active
      ? (node.veto ? COLORS.risk : (node.core ? COLORS.core : node.color))
      : 'rgba(236,232,224,0.22)';
    ctx.stroke();

    if (node.veto && active) {
      ctx.strokeStyle = COLORS.risk;
      ctx.lineWidth = 2;
      ctx.lineCap = 'round';
      var s = 7;
      ctx.beginPath();
      ctx.moveTo(node.x - s, node.y - s);
      ctx.lineTo(node.x + s, node.y + s);
      ctx.moveTo(node.x + s, node.y - s);
      ctx.lineTo(node.x - s, node.y + s);
      ctx.stroke();
    }

    ctx.textAlign = 'center';
    ctx.fillStyle = active ? COLORS.core : '#b8b0a4';
    ctx.font = '600 ' + (node.core ? 12 : 10) + 'px "DM Sans", system-ui, sans-serif';
    ctx.fillText(node.label, node.x, node.y + (node.veto && active ? -1 : 1));
    ctx.fillStyle = active ? COLORS.muted : '#6a6458';
    ctx.font = '500 8px "DM Sans", system-ui, sans-serif';
    ctx.fillText(node.sub, node.x, node.y + (node.veto && active ? 11 : 13));
  }

  function drawParticles(phase) {
    for (var i = particles.length - 1; i >= 0; i--) {
      var p = particles[i];
      if (phase.edges.indexOf(p.edge.id) < 0) { particles.splice(i, 1); continue; }
      p.t += p.speed;
      if (p.t >= 1) { particles.splice(i, 1); continue; }
      var a = nodeMap[p.edge.from];
      var b = nodeMap[p.edge.to];
      var ease = p.t < 0.5 ? 2 * p.t * p.t : -1 + (4 - 2 * p.t) * p.t;
      var x = a.x + (b.x - a.x) * ease;
      var y = a.y + (b.y - a.y) * ease;
      ctx.beginPath();
      ctx.arc(x, y, p.size, 0, Math.PI * 2);
      ctx.fillStyle = p.color;
      ctx.shadowBlur = 12;
      ctx.shadowColor = p.color;
      ctx.fill();
      ctx.shadowBlur = 0;
    }
  }

  function hitTest(x, y) {
    for (var i = nodes.length - 1; i >= 0; i--) {
      var n = nodes[i];
      var dx = x - n.x, dy = y - n.y;
      if (dx * dx + dy * dy <= (n.r + 12) * (n.r + 12)) return n.id;
    }
    return null;
  }

  var last = performance.now();
  function frame(now) {
    var dt = now - last;
    last = now;
    time += 0.016;

    if (!reduced && !paused && !hoverId) {
      phaseT += dt;
      if (phaseT >= phases[phaseIndex].ms) {
        phaseT = 0;
        phaseIndex = (phaseIndex + 1) % phases.length;
      }
    }

    layoutNodes();
    var phase = activePhase();
    var glow = 0.5 + 0.5 * Math.sin(time * 2.5);
    syncTrace(phase.trace);

    ctx.clearRect(0, 0, w, h);
    drawGrid();
    edges.forEach(function (e) { drawEdge(e, phase, glow); });
    drawParticles(phase);
    nodes.forEach(function (n) { drawNode(n, phase, glow); });

    requestAnimationFrame(frame);
  }

  canvas.addEventListener('mousemove', function (e) {
    var rect = canvas.getBoundingClientRect();
    mx = e.clientX - rect.left;
    my = e.clientY - rect.top;
    hoverId = hitTest(mx, my);
    canvas.style.cursor = hoverId ? 'pointer' : 'crosshair';
  });
  canvas.addEventListener('mouseleave', function () {
    mx = my = -1;
    hoverId = null;
  });
  canvas.addEventListener('click', function () {
    paused = !paused;
    canvas.parentElement.classList.toggle('graph-paused', paused);
  });

  window.addEventListener('resize', resize);
  resize();

  if (reduced) {
    var staticPhase = phases[2];
    syncTrace(2);
    ctx.clearRect(0, 0, w, h);
    drawGrid();
    edges.forEach(function (e) { drawEdge(e, staticPhase, 1); });
    nodes.forEach(function (n) { drawNode(n, staticPhase, 1); });
  } else {
    requestAnimationFrame(frame);
  }
})();

/* MIZOKI3 — Governed decision flow diagram animation */

(function () {
  'use strict';

  var diagram = document.getElementById('srpvdalDiagram');
  if (!diagram) return;

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var steps = diagram.querySelectorAll('[data-flow-step]');
  var connectors = diagram.querySelectorAll('[data-flow-connector]');
  var pill = document.getElementById('flowStagePill');
  var labels = ['Signal ingested', 'Graph reasoning', 'Pipeline stages', 'Gate authorization', 'Action executed', 'Outcome learned'];
  var index = 0;
  var visible = false;
  var timer = null;

  function setActive(i) {
    index = Math.max(0, Math.min(i, steps.length - 1));
    steps.forEach(function (el, n) {
      el.classList.toggle('flow-active', n <= index);
      el.classList.toggle('flow-current', n === index);
    });
    connectors.forEach(function (el, n) {
      el.classList.toggle('flow-connector-active', n < index);
    });
    if (pill) pill.textContent = labels[index] || '';
  }

  function startCycle() {
    if (timer || reduced) return;
    timer = setInterval(function () {
      if (!visible) return;
      setActive((index + 1) % steps.length);
    }, 2200);
  }

  function stopCycle() {
    if (timer) { clearInterval(timer); timer = null; }
  }

  if (reduced) {
    setActive(steps.length - 1);
    return;
  }

  var section = document.getElementById('how-it-works');
  var pillars = section ? section.querySelectorAll('.pillar') : [];

  var diagramObs = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        visible = entry.isIntersecting;
        if (visible) {
          setActive(0);
          startCycle();
        } else {
          stopCycle();
        }
      });
    },
    { threshold: 0.25 }
  );
  diagramObs.observe(diagram);

  if (pillars.length) {
    var pillarObs = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var i = Array.prototype.indexOf.call(pillars, entry.target);
          if (i === 0) setActive(1);
          if (i === 1) setActive(2);
          if (i === 2) setActive(3);
        });
      },
      { threshold: 0.5 }
    );
    pillars.forEach(function (p) { pillarObs.observe(p); });
  }

  setActive(0);
})();

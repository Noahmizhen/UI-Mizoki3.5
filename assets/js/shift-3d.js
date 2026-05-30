/* MIZOKI3 — "One Brain" living knowledge-graph centerpiece for #shift.
   Progressive enhancement: the section is fully readable as static markup
   (the gold-core fallback SVG). When motion is allowed and WebGL is available,
   this module replaces it with a continuously-living 3D brain. Three.js is
   lazy-loaded. No scroll dependency — it animates on a time clock while in view. */

const GOLD = 0xc9a855;
const COPPER = 0xb87333;
const FOG = 0x0a0e1a;
const IS_MOBILE = window.matchMedia('(max-width: 768px)').matches;
const NODE_R = 2.3;

const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
const lerp = (a, b, t) => a + (b - a) * t;
function smoothstep(e0, e1, x) {
  const t = clamp((x - e0) / (e1 - e0), 0, 1);
  return t * t * (3 - 2 * t);
}

function supportsWebGL() {
  try {
    const c = document.createElement('canvas');
    return !!(window.WebGLRenderingContext && (c.getContext('webgl') || c.getContext('experimental-webgl')));
  } catch (e) {
    return false;
  }
}

const section = document.querySelector('[data-shift-3d]');
const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (section && !reduced && supportsWebGL()) {
  const trigger = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        trigger.disconnect();
        init().catch(() => {
          // Any failure (CDN import, context loss) leaves the static fallback intact.
          section.classList.remove('is-live');
        });
      }
    });
  }, { rootMargin: '400px 0px' });
  trigger.observe(section);
}

async function init() {
  const THREE = await import('three');
  const { EffectComposer } = await import('three/addons/postprocessing/EffectComposer.js');
  const { RenderPass } = await import('three/addons/postprocessing/RenderPass.js');
  const { UnrealBloomPass } = await import('three/addons/postprocessing/UnrealBloomPass.js');
  const { OutputPass } = await import('three/addons/postprocessing/OutputPass.js');

  const canvas = document.getElementById('shift-canvas');
  const core = section.querySelector('.shift-core');
  if (!canvas || !core) throw new Error('shift core missing');

  section.classList.add('is-live');

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.setClearColor(0x000000, 0);

  const scene = new THREE.Scene();
  scene.fog = new THREE.FogExp2(FOG, 0.03);

  const camera = new THREE.PerspectiveCamera(46, 1, 0.1, 100);
  camera.position.set(0, 0, 8);

  scene.add(new THREE.AmbientLight(0x4a5468, 0.7));
  const keyLight = new THREE.PointLight(GOLD, 1.4, 40);
  keyLight.position.set(0, 0, 4);
  scene.add(keyLight);

  const center = new THREE.Vector3(0, 0, 0);

  /* —— Core: gold point-cloud sphere + icosahedron wireframe —— */
  const coreGroup = new THREE.Group();
  const cCount = IS_MOBILE ? 900 : 1700;
  const cPos = new Float32Array(cCount * 3);
  for (let i = 0; i < cCount; i++) {
    const rr = 1.1 + Math.random() * 0.32;
    const a = Math.random() * Math.PI * 2;
    const b = Math.acos(2 * Math.random() - 1);
    cPos[i * 3] = Math.sin(b) * Math.cos(a) * rr;
    cPos[i * 3 + 1] = Math.sin(b) * Math.sin(a) * rr;
    cPos[i * 3 + 2] = Math.cos(b) * rr;
  }
  const cGeo = new THREE.BufferGeometry();
  cGeo.setAttribute('position', new THREE.BufferAttribute(cPos, 3));
  const cMat = new THREE.PointsMaterial({
    color: GOLD,
    size: 0.05,
    transparent: true,
    opacity: 0,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
    sizeAttenuation: true,
  });
  const corePoints = new THREE.Points(cGeo, cMat);
  const icosaMat = new THREE.LineBasicMaterial({ color: GOLD, transparent: true, opacity: 0 });
  const icosa = new THREE.LineSegments(
    new THREE.EdgesGeometry(new THREE.IcosahedronGeometry(1.35, 1)),
    icosaMat
  );
  coreGroup.add(corePoints, icosa);
  scene.add(coreGroup);

  /* —— Orbiting domain nodes, hub + ring edges, and traveling pulses —— */
  const nodeGroup = new THREE.Group();
  nodeGroup.rotation.x = 0.4;
  const nodeCount = 5;
  const nodeLocal = [];
  const nodes = [];
  const nodeMats = [];
  const nodeSphere = new THREE.SphereGeometry(0.1, 14, 14);
  for (let i = 0; i < nodeCount; i++) {
    const a = (i / nodeCount) * Math.PI * 2;
    const p = new THREE.Vector3(Math.cos(a) * NODE_R, 0, Math.sin(a) * NODE_R);
    nodeLocal.push(p);
    const nMat = new THREE.MeshBasicMaterial({ color: GOLD, transparent: true, opacity: 0 });
    const node = new THREE.Mesh(nodeSphere, nMat);
    node.position.copy(p);
    nodeGroup.add(node);
    nodes.push(node);
    nodeMats.push(nMat);
  }

  const hubPts = [];
  const ringPts = [];
  for (let i = 0; i < nodeCount; i++) {
    hubPts.push(0, 0, 0, nodeLocal[i].x, nodeLocal[i].y, nodeLocal[i].z);
    const n = nodeLocal[(i + 1) % nodeCount];
    ringPts.push(nodeLocal[i].x, nodeLocal[i].y, nodeLocal[i].z, n.x, n.y, n.z);
  }
  const hubMat = new THREE.LineBasicMaterial({ color: COPPER, transparent: true, opacity: 0 });
  const hubEdges = new THREE.LineSegments(
    new THREE.BufferGeometry().setAttribute('position', new THREE.Float32BufferAttribute(hubPts, 3)),
    hubMat
  );
  const ringMat = new THREE.LineBasicMaterial({ color: GOLD, transparent: true, opacity: 0 });
  const ringEdges = new THREE.LineSegments(
    new THREE.BufferGeometry().setAttribute('position', new THREE.Float32BufferAttribute(ringPts, 3)),
    ringMat
  );
  nodeGroup.add(hubEdges, ringEdges);

  // Traveling pulse beads: one per spoke, flowing core -> node on a loop.
  const beadPos = new Float32Array(nodeCount * 3);
  const beadGeo = new THREE.BufferGeometry();
  beadGeo.setAttribute('position', new THREE.BufferAttribute(beadPos, 3));
  const beadMat = new THREE.PointsMaterial({
    color: GOLD,
    size: 0.16,
    transparent: true,
    opacity: 0,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
    sizeAttenuation: true,
  });
  const beads = new THREE.Points(beadGeo, beadMat);
  nodeGroup.add(beads);
  scene.add(nodeGroup);

  /* —— Bloom: only the gold geometry is bright enough to ignite —— */
  const composer = new EffectComposer(renderer);
  composer.addPass(new RenderPass(scene, camera));
  const bloom = new UnrealBloomPass(new THREE.Vector2(1, 1), 0.8, 0.75, 0.5);
  composer.addPass(bloom);
  composer.addPass(new OutputPass());

  function resize() {
    const w = core.clientWidth || 1;
    const h = core.clientHeight || 1;
    renderer.setSize(w, h, false);
    composer.setSize(w, h);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  }

  let pointerX = 0;
  let pointerY = 0;
  window.addEventListener('pointermove', (e) => {
    pointerX = (e.clientX / window.innerWidth - 0.5) * 0.6;
    pointerY = -(e.clientY / window.innerHeight - 0.5) * 0.35;
  }, { passive: true });

  let appearStart = 0;
  const worldPos = new THREE.Vector3();

  function update(now) {
    if (appearStart === 0) appearStart = now;
    const appear = smoothstep(0, 1.2, now - appearStart);

    // Breathing core
    const breath = 0.5 + 0.5 * Math.sin(now * 0.8);
    coreGroup.scale.setScalar(appear * (1 + 0.04 * breath));
    coreGroup.rotation.y = now * 0.16;
    coreGroup.rotation.x = now * 0.045;
    cMat.opacity = appear;
    icosaMat.opacity = appear * 0.5;

    // Orbiting graph
    nodeGroup.rotation.y = now * 0.22;
    hubMat.opacity = appear * 0.4;
    ringMat.opacity = appear * 0.22;

    // Per-node proximity highlight (nearest the camera glows brighter/larger)
    for (let i = 0; i < nodeCount; i++) {
      nodes[i].getWorldPosition(worldPos);
      const prox = smoothstep(-NODE_R, NODE_R, worldPos.z);
      nodeMats[i].opacity = appear * (0.55 + 0.45 * prox);
      nodes[i].scale.setScalar(0.85 + 0.5 * prox);
    }

    // Flowing pulses core -> node
    const bArr = beadGeo.attributes.position.array;
    for (let i = 0; i < nodeCount; i++) {
      const frac = (now * 0.32 + i * 0.21) % 1;
      const p = nodeLocal[i];
      bArr[i * 3] = p.x * frac;
      bArr[i * 3 + 1] = p.y * frac;
      bArr[i * 3 + 2] = p.z * frac;
    }
    beadGeo.attributes.position.needsUpdate = true;
    beadMat.opacity = appear * 0.9;

    // Breathing bloom
    bloom.strength = lerp(0.6, 1.05, breath);

    // Gentle cursor parallax (no scroll, no dolly)
    camera.position.x += (pointerX - camera.position.x) * 0.04;
    camera.position.y += (pointerY - camera.position.y) * 0.04;
    camera.position.z = 8;
    camera.lookAt(center);
  }

  /* —— Run loop with offscreen + tab-hidden pausing —— */
  let rafId = null;
  let inView = false;
  let visible = !document.hidden;

  function frame() {
    rafId = requestAnimationFrame(frame);
    update(performance.now() * 0.001);
    composer.render();
  }
  function start() {
    if (rafId == null && inView && visible) {
      resize();
      rafId = requestAnimationFrame(frame);
    }
  }
  function stop() {
    if (rafId != null) {
      cancelAnimationFrame(rafId);
      rafId = null;
    }
  }

  const viewObserver = new IntersectionObserver((entries) => {
    inView = entries[0].isIntersecting;
    if (inView) start();
    else stop();
  }, { rootMargin: '100px 0px' });
  viewObserver.observe(section);

  document.addEventListener('visibilitychange', () => {
    visible = !document.hidden;
    if (visible) start();
    else stop();
  });

  window.addEventListener('resize', resize, { passive: true });

  resize();
  inView = true;
  start();

  /* —— Release GPU resources if the page is being torn down —— */
  window.addEventListener('pagehide', () => {
    stop();
    viewObserver.disconnect();
    scene.traverse((obj) => {
      if (obj.geometry) obj.geometry.dispose();
      if (obj.material) {
        const mats = Array.isArray(obj.material) ? obj.material : [obj.material];
        mats.forEach((m) => {
          if (m.map) m.map.dispose();
          m.dispose();
        });
      }
    });
    composer.dispose && composer.dispose();
    renderer.dispose();
  }, { once: true });
}

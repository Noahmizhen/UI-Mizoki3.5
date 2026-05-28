#!/usr/bin/env python3
"""Generate MIZOKI3 subpages matching the homepage design system."""
from __future__ import annotations

import html
from pathlib import Path

from _build_site_data import (
    ARCHITECTURE_PAGE,
    BLOG_POSTS,
    DCP_DIMENSIONS,
    LENS_PAGES,
    SRPVDAL_STAGES,
)

OUT = Path(__file__).parent
LENS_ORDER = ["counsel", "signal", "capital", "risk", "estate"]

NAV_ITEMS = [
    ("Platform", "/#platform"),
    ("Counsel", "/counsel"),
    ("Signal", "/signal"),
    ("Capital", "/capital"),
    ("Risk", "/risk"),
    ("Estate", "/estate"),
    ("Architecture", "/architecture"),
    ("Blog", "/blog/"),
]

FONTS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Outfit:wght@300;400;500;600&family=Playfair+Display:wght@500;600;700&display=swap"
)


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def page_head(title: str, description: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="{FONTS_URL}" rel="stylesheet" />
<link rel="stylesheet" href="/assets/css/homepage.css" />
<link rel="stylesheet" href="/assets/css/subpages.css" />
</head>
<body class="page-sub">
"""


def render_nav(active: str | None = None) -> str:
    links = []
    for label, href in NAV_ITEMS:
        cls = "nav-link"
        if active and href.rstrip("/") == active.rstrip("/"):
            cls += " is-active"
        elif active == "/#platform" and href == "/#platform":
            cls += " is-active"
        links.append(f'<a href="{href}" class="{cls}">{esc(label)}</a>')

    mobile_links = "\n      ".join(links)
    desktop_links = "\n      ".join(links)

    return f"""
<header class="site-nav is-solid" role="banner">
  <div class="container nav-inner">
    <a href="/" class="nav-wordmark">MIZOKI3</a>
    <nav class="nav-links" aria-label="Primary">
      {desktop_links}
    </nav>
    <a href="mailto:hello@mizoki3.com?subject=MIZOKI3%20Executive%20Demo%20Request" class="nav-cta">Request Demo</a>
    <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<div class="mobile-backdrop" aria-hidden="true"></div>
<nav id="mobile-nav" class="mobile-panel" aria-label="Mobile">
  <div class="mobile-panel-links">
    {mobile_links}
    <a href="mailto:hello@mizoki3.com?subject=MIZOKI3%20Executive%20Demo%20Request" class="nav-cta">Request Demo</a>
  </div>
</nav>
"""


def render_footer() -> str:
    return """
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <span class="footer-wordmark">MIZOKI3</span>
        <p class="footer-tagline">Patented Autonomous Decision Intelligence.</p>
        <a href="mailto:hello@mizoki3.com" class="footer-email">hello@mizoki3.com</a>
      </div>
      <div class="footer-col">
        <h4>Platform</h4>
        <ul class="footer-links">
          <li><a href="/counsel">Counsel</a></li>
          <li><a href="/signal">Signal</a></li>
          <li><a href="/capital">Capital</a></li>
          <li><a href="/risk">Risk</a></li>
          <li><a href="/estate">Estate</a></li>
          <li><a href="/architecture">Architecture</a></li>
          <li><a href="/blog/">Blog</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Trust</h4>
        <div class="trust-badges">
          <span>GDPR</span>
          <span>Patented Technology</span>
          <span>Customer-Managed Encryption</span>
        </div>
      </div>
    </div>
    <div class="footer-bar">
      <span>© 2026 MIZOKI3</span>
      <div class="footer-legal">
        <a href="mailto:hello@mizoki3.com?subject=Privacy%20Inquiry">Privacy</a>
        <a href="mailto:hello@mizoki3.com?subject=Terms%20Inquiry">Terms</a>
      </div>
    </div>
  </div>
</footer>

<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""


def render_closing_cta(
    headline: str,
    *,
    body: str | None = None,
    cta_label: str = "Schedule a Briefing",
    mail_subject: str = "MIZOKI3%20Executive%20Demo%20Request",
    bg_url: str | None = None,
    bg_aria: str | None = None,
    solid: bool = False,
) -> str:
    body_html = ""
    if body:
        body_html = f'\n        <p class="closing-sub">{esc(body)}</p>'

    if solid:
        return f"""
  <section class="section section--closing-solid" aria-labelledby="closing-heading">
    <div class="container section-content">
      <div class="closing-inner reveal">
        <h2 id="closing-heading" class="serif-headline">{esc(headline)}</h2>{body_html}
        <a href="mailto:hello@mizoki3.com?subject={mail_subject}" class="btn-closing">{esc(cta_label)}</a>
        <a href="mailto:hello@mizoki3.com" class="closing-email">hello@mizoki3.com</a>
      </div>
    </div>
  </section>
"""

    return f"""
  <section class="section section--cinematic section--closing" data-parallax aria-labelledby="closing-heading">
    <div
      class="section-bg section-bg--closing"
      data-bg="{esc(bg_url or '')}"
      role="img"
      aria-label="{esc(bg_aria or '')}"
    ></div>
    <div class="section-overlay section-overlay--heavy"></div>
    <div class="container section-content">
      <div class="closing-inner reveal">
        <h2 id="closing-heading" class="serif-headline">{esc(headline)}</h2>{body_html}
        <a href="mailto:hello@mizoki3.com?subject={mail_subject}" class="btn-closing">{esc(cta_label)}</a>
        <a href="mailto:hello@mizoki3.com" class="closing-email">hello@mizoki3.com</a>
      </div>
    </div>
  </section>
"""


def cross_diagram_svg(center_slug: str) -> str:
    """Five-lens cross-domain diagram with center lens highlighted."""
    positions = {
        "counsel": (360, 200),
        "signal": (120, 80),
        "capital": (600, 80),
        "risk": (120, 320),
        "estate": (600, 320),
    }
    center = positions[center_slug]
    lines = []
    for slug, (x, y) in positions.items():
        if slug == center_slug:
            continue
        lines.append(
            f'<line x1="{center[0]}" y1="{center[1]}" x2="{x}" y2="{y}" '
            f'stroke="rgba(201,168,85,0.35)" stroke-width="1"/>'
        )

    nodes = []
    for slug, (x, y) in positions.items():
        title = LENS_PAGES[slug]["title"]
        is_center = slug == center_slug
        fill = "rgba(201,168,85,0.15)" if is_center else "rgba(26,34,53,0.9)"
        stroke = "rgba(201,168,85,0.55)" if is_center else "rgba(30,42,58,1)"
        text_fill = "#c9a855" if is_center else "#8a919e"
        nodes.append(
            f'<circle cx="{x}" cy="{y}" r="36" fill="{fill}" stroke="{stroke}" stroke-width="1"/>'
            f'<text x="{x}" y="{y + 5}" text-anchor="middle" fill="{text_fill}" '
            f'font-family="Outfit,sans-serif" font-size="12" font-weight="500">{esc(title)}</text>'
        )

    return f"""<div class="cross-diagram reveal" aria-hidden="true">
  <svg viewBox="0 0 720 400" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="360" cy="200" r="140" fill="none" stroke="rgba(201,168,85,0.08)" stroke-width="1"/>
    {''.join(lines)}
    {''.join(nodes)}
    <text x="360" y="24" text-anchor="middle" fill="#5a6270" font-family="Outfit,sans-serif" font-size="10" letter-spacing="0.12em">SHARED KNOWLEDGE GRAPH</text>
  </svg>
</div>"""


def arch_diagram_svg() -> str:
    return """<div class="arch-diagram-wrap reveal" aria-hidden="true">
  <svg viewBox="0 0 900 420" fill="none" xmlns="http://www.w3.org/2000/svg">
    <text x="450" y="28" text-anchor="middle" fill="#5a6270" font-family="Outfit,sans-serif" font-size="10" letter-spacing="0.14em">GOVERNED DECISION ARCHITECTURE</text>
    <circle cx="450" cy="210" r="72" fill="rgba(201,168,85,0.12)" stroke="rgba(201,168,85,0.45)" stroke-width="1"/>
    <text x="450" y="206" text-anchor="middle" fill="#c9a855" font-family="Outfit,sans-serif" font-size="13" font-weight="500">TCO-KG</text>
    <text x="450" y="224" text-anchor="middle" fill="#8a919e" font-family="Outfit,sans-serif" font-size="10">The Brain</text>
    <rect x="60" y="88" width="88" height="36" rx="4" fill="#111827" stroke="rgba(30,42,58,1)"/>
    <text x="104" y="111" text-anchor="middle" fill="#8a919e" font-family="Outfit,sans-serif" font-size="11">Counsel</text>
    <rect x="752" y="88" width="88" height="36" rx="4" fill="#111827" stroke="rgba(30,42,58,1)"/>
    <text x="796" y="111" text-anchor="middle" fill="#8a919e" font-family="Outfit,sans-serif" font-size="11">Signal</text>
    <rect x="60" y="296" width="88" height="36" rx="4" fill="#111827" stroke="rgba(30,42,58,1)"/>
    <text x="104" y="319" text-anchor="middle" fill="#8a919e" font-family="Outfit,sans-serif" font-size="11">Risk</text>
    <rect x="752" y="296" width="88" height="36" rx="4" fill="#111827" stroke="rgba(30,42,58,1)"/>
    <text x="796" y="319" text-anchor="middle" fill="#8a919e" font-family="Outfit,sans-serif" font-size="11">Estate</text>
    <rect x="406" y="356" width="88" height="36" rx="4" fill="#111827" stroke="rgba(30,42,58,1)"/>
    <text x="450" y="379" text-anchor="middle" fill="#8a919e" font-family="Outfit,sans-serif" font-size="11">Capital</text>
    <line x1="148" y1="106" x2="378" y2="190" stroke="rgba(201,168,85,0.25)" stroke-width="1"/>
    <line x1="752" y1="106" x2="522" y2="190" stroke="rgba(201,168,85,0.25)" stroke-width="1"/>
    <line x1="148" y1="314" x2="378" y2="230" stroke="rgba(201,168,85,0.25)" stroke-width="1"/>
    <line x1="752" y1="314" x2="522" y2="230" stroke="rgba(201,168,85,0.25)" stroke-width="1"/>
    <line x1="450" y1="356" x2="450" y2="282" stroke="rgba(201,168,85,0.25)" stroke-width="1"/>
    <ellipse cx="450" cy="210" rx="155" ry="95" fill="none" stroke="rgba(201,168,85,0.2)" stroke-width="1" stroke-dasharray="4 6"/>
    <text x="640" y="210" fill="#8a919e" font-family="Outfit,sans-serif" font-size="10">SRPVDAL</text>
    <rect x="700" y="178" width="120" height="64" rx="4" fill="rgba(201,168,85,0.1)" stroke="rgba(201,168,85,0.4)" stroke-width="1"/>
    <text x="760" y="206" text-anchor="middle" fill="#c9a855" font-family="Outfit,sans-serif" font-size="12" font-weight="500">DCP</text>
    <text x="760" y="224" text-anchor="middle" fill="#8a919e" font-family="Outfit,sans-serif" font-size="10">The Gate</text>
    <line x1="522" y1="210" x2="700" y2="210" stroke="rgba(201,168,85,0.35)" stroke-width="1"/>
    <rect x="848" y="188" width="52" height="44" rx="4" fill="#111827" stroke="rgba(30,42,58,1)"/>
    <text x="874" y="216" text-anchor="middle" fill="#8a919e" font-family="Outfit,sans-serif" font-size="10">Act</text>
    <line x1="820" y1="210" x2="848" y2="210" stroke="rgba(201,168,85,0.35)" stroke-width="1"/>
    <text x="120" y="210" fill="#5a6270" font-family="Outfit,sans-serif" font-size="9" letter-spacing="0.08em">SENSE → LEARN</text>
  </svg>
</div>"""


def render_cross_nav(current_slug: str) -> str:
    cards = []
    for slug in LENS_ORDER:
        if slug == current_slug:
            continue
        page = LENS_PAGES[slug]
        cards.append(
            f"""        <a href="/{slug}" class="cross-nav-card">
          <h4>{esc(page["title"])}</h4>
          <span>{esc(page["tag"])}</span>
        </a>"""
        )
    return f"""
  <nav class="cross-nav" aria-label="Continue exploring lenses">
    <div class="container">
      <header class="cross-nav-head reveal">
        <p class="accent-label">Continue Exploring</p>
        <h2 class="serif-headline">One brain. Five lenses.</h2>
      </header>
      <div class="cross-nav-grid reveal">
{chr(10).join(cards)}
      </div>
    </div>
  </nav>
"""


def render_cross_section(slug: str, page: dict) -> str:
    inner = f"""
      <header class="section-head section-head--center reveal">
        <p class="accent-label">{esc(page["cross_label"])}</p>
        <h2 id="cross-heading" class="serif-headline">{esc(page["cross_headline"])}</h2>
        <p class="section-intro">{esc(page["cross_body"])}</p>
      </header>
      {cross_diagram_svg(slug)}
"""
    if page.get("cross_solid"):
        return f"""
  <section class="section section--solid has-grain" aria-labelledby="cross-heading">
    <div class="container">
{inner}
    </div>
  </section>
"""
    return f"""
  <section class="section section--cinematic" data-parallax aria-labelledby="cross-heading">
    <div
      class="section-bg"
      data-bg="{esc(page["cross_image"])}"
      role="img"
      aria-label="{esc(page["cross_aria"])}"
    ></div>
    <div class="section-overlay section-overlay--heavy"></div>
    <div class="container section-content">
{inner}
    </div>
  </section>
"""


def render_lens(slug: str) -> str:
    page = LENS_PAGES[slug]
    active = f"/{slug}"

    pillars = []
    for card in page["capabilities"]:
        pillars.append(
            f"""        <article class="pillar-card reveal-child">
          <span class="accent-label">{esc(card["title"])}</span>
          <p>{esc(card["body"])}</p>
        </article>"""
        )

    ingest_items = "\n".join(f"            <li>{esc(item)}</li>" for item in page["ingests"])
    produce_items = "\n".join(f"            <li>{esc(item)}</li>" for item in page["produces"])

    return (
        page_head(f"MIZOKI3 — {page['title']} · {page['tag']}", page["meta_description"])
        + render_nav(active)
        + """
<main>
"""
        + f"""
  <section class="sub-hero section" aria-labelledby="lens-heading">
    <div
      class="section-bg section-bg--immediate"
      style="background-image: url('{esc(page["hero_image"])}');"
      role="img"
      aria-label="{esc(page["hero_aria"])}"
    ></div>
    <div class="section-overlay section-overlay--heavy"></div>
    <div class="container section-content">
      <div class="sub-hero-inner reveal">
        <p class="breadcrumb"><a href="/">MIZOKI3</a> → <span>{esc(page["title"])}</span></p>
        <p class="accent-label">{esc(page["label"])}</p>
        <h1 id="lens-heading" class="serif-headline">{esc(page["headline"])}</h1>
        <p class="sub-hero-lead">{esc(page["hero_body"])}</p>
      </div>
    </div>
  </section>

  <section class="section section--solid has-grain" aria-labelledby="capabilities-heading">
    <div class="container">
      <header class="section-head reveal">
        <p class="accent-label">{esc(page["capabilities_label"])}</p>
        <h2 id="capabilities-heading" class="serif-headline">{esc(page["capabilities_headline"])}</h2>
        <p class="section-intro">{esc(page["capabilities_intro"])}</p>
      </header>
      <div class="pillars reveal">
{chr(10).join(pillars)}
      </div>
    </div>
  </section>
"""
        + render_cross_section(slug, page)
        + f"""
  <section class="section section--solid" aria-labelledby="io-heading">
    <div class="container">
      <header class="section-head reveal">
        <p class="accent-label">Lens Anatomy</p>
        <h2 id="io-heading" class="serif-headline">What enters. What emerges.</h2>
      </header>
      <div class="io-grid reveal">
        <article class="io-card">
          <h3>{esc(page["title"])} Ingests</h3>
          <ul class="io-list">
{ingest_items}
          </ul>
        </article>
        <div class="io-divider" aria-hidden="true"></div>
        <article class="io-card">
          <h3>{esc(page["title"])} Produces</h3>
          <ul class="io-list">
{produce_items}
          </ul>
        </article>
      </div>
    </div>
  </section>
"""
        + render_closing_cta(
            page["cta_headline"],
            cta_label="Schedule a Briefing",
            mail_subject=page["cta_subject"],
            solid=page.get("closing_solid", False),
            bg_url=page.get("closing_image", page["hero_image"]),
            bg_aria=page.get("closing_aria", page["hero_aria"]),
        )
        + render_cross_nav(slug)
        + """
</main>
"""
        + render_footer()
    )


def render_architecture() -> str:
    arch = ARCHITECTURE_PAGE

    pipeline_steps = []
    for i, stage in enumerate(SRPVDAL_STAGES):
        connector = ""
        if i < len(SRPVDAL_STAGES) - 1:
            connector = '        <div class="pipeline-connector" aria-hidden="true"></div>\n'
        pipeline_steps.append(
            f"""        <article class="pipeline-step reveal-child">
          <p class="step-num">{esc(stage["num"])} · {esc(stage["name"])}</p>
          <h4>{esc(stage["name"])}</h4>
          <p>{esc(stage["description"])}</p>
        </article>
{connector}"""
        )

    dcp_dims = "\n".join(
        f"""        <article class="dcp-dim reveal-child">
          <h4>{esc(dim["title"])}</h4>
          <p>{esc(dim["description"])}</p>
        </article>"""
        for dim in DCP_DIMENSIONS
    )

    tckg_details = """
        <ul class="detail-list">
          <li><strong>Graph schema</strong>Property graph with temporal and causal edge types</li>
          <li><strong>Storage</strong>Cloud Spanner with graph-native query</li>
          <li><strong>Update mechanism</strong>Continuous ingestion from all domain lenses</li>
          <li><strong>Query model</strong>Causal traversal with counterfactual branching</li>
        </ul>"""

    return (
        page_head("MIZOKI3 — Technical Architecture", arch["meta_description"])
        + render_nav("/architecture")
        + f"""
<main>

  <section class="sub-hero section" aria-labelledby="arch-heading">
    <div
      class="section-bg section-bg--immediate"
      style="background-image: url('{esc(arch["hero_image"])}');"
      role="img"
      aria-label="{esc(arch["hero_aria"])}"
    ></div>
    <div class="section-overlay section-overlay--heavy"></div>
    <div class="container section-content">
      <div class="sub-hero-inner reveal">
        <p class="breadcrumb"><a href="/">MIZOKI3</a> → <span>Architecture</span></p>
        <p class="accent-label">TECHNICAL ARCHITECTURE</p>
        <h1 id="arch-heading" class="serif-headline">Three subsystems. One governed decision loop.</h1>
        <p class="sub-hero-lead">MIZOKI3 is a ground-up proprietary platform — not a wrapper on third-party language models. The architecture comprises three integrated subsystems that every domain lens shares.</p>
      </div>
    </div>
  </section>

  <section class="section section--solid has-grain" aria-labelledby="system-arch-heading">
    <div class="container">
      <header class="section-head reveal">
        <p class="accent-label">Overview</p>
        <h2 id="system-arch-heading" class="serif-headline">System Architecture</h2>
        <p class="section-intro">The Temporal-Causal Knowledge Graph sits at the center. The SRPVDAL pipeline governs every decision cycle. The Decision Control Plane authorizes what reaches your systems — with every domain lens reading and writing the same substrate.</p>
      </header>
      {arch_diagram_svg()}
    </div>
  </section>

  <section class="section section--cinematic" data-parallax aria-labelledby="tckg-heading">
    <div
      class="section-bg"
      data-bg="{esc(arch["tckg_image"])}"
      role="img"
      aria-label="{esc(arch["tckg_aria"])}"
    ></div>
    <div class="section-overlay section-overlay--heavy"></div>
    <div class="container section-content">
      <article class="subsystem-block reveal">
        <p class="accent-label">Subsystem 01</p>
        <h2 id="tckg-heading" class="serif-headline">Temporal-Causal Knowledge Graph</h2>
        <p>The graph models entities, relationships, obligations, events, and outcomes over time — tracking not only what happened, but what caused it and what would change under alternate conditions. Causal edges bind legal, financial, marketing, and fiduciary signals into one traversable substrate. Counterfactual simulation runs on the same structure proposals are validated against.</p>
        <div class="detail-card">
{tckg_details}
        </div>
      </article>
    </div>
  </section>

  <section class="section section--solid" aria-labelledby="srpvdal-heading">
    <div class="container">
      <header class="section-head reveal">
        <p class="accent-label">Subsystem 02</p>
        <h2 id="srpvdal-heading" class="serif-headline">Seven-Stage Decision Pipeline</h2>
        <p class="section-intro">Every consequential decision flows through seven stages. Nothing skips a step. Nothing reaches execution without traversing the full loop — each stage auditable, each handoff verified.</p>
      </header>
      <div class="pipeline-flow reveal">
{"".join(pipeline_steps)}
      </div>
    </div>
  </section>

  <section class="section section--cinematic" data-parallax aria-labelledby="dcp-heading">
    <div
      class="section-bg"
      data-bg="{esc(arch["dcp_image"])}"
      role="img"
      aria-label="{esc(arch["dcp_aria"])}"
    ></div>
    <div class="section-overlay section-overlay--heavy"></div>
    <div class="container section-content">
      <article class="subsystem-block reveal">
        <p class="accent-label">Subsystem 03</p>
        <h2 id="dcp-heading" class="serif-headline">Decision Control Plane</h2>
        <p>The DCP is a mandatory, non-bypass governance layer between what AI agents recommend and what actually executes. Every action is scored across causal confidence, validation agreement, simulation delta, policy compliance, and historical performance before authorization. When the Gate vetoes, the decision carries the arithmetic, policy citation, and causal trace — not a black-box refusal. Patented.</p>
        <div class="dcp-dimensions">
{dcp_dims}
        </div>
      </article>
    </div>
  </section>

  <section class="section section--solid has-grain" aria-labelledby="infra-heading">
    <div class="container">
      <article class="subsystem-block reveal">
        <p class="accent-label">Infrastructure</p>
        <h2 id="infra-heading" class="serif-headline">Deployment Infrastructure</h2>
        <p>The platform runs on Google Cloud: private VPC, Cloud Spanner property-graph schema for TCO-KG, Pub/Sub event bus, Cloud Run orchestration, Vertex AI reasoning isolation, and customer-managed encryption via Cloud KMS. Infrastructure is designed for regulated buyers who require data residency, encryption control, and auditable execution — not a shared multi-tenant wrapper.</p>
      </article>
    </div>
  </section>
"""
        + render_closing_cta(
            "Request a technical architecture briefing.",
            body="We walk through TCO-KG schema, SRPVDAL execution traces, and DCP authorization logic — tailored to your regulatory and operational context.",
            cta_label="Schedule a Briefing",
            mail_subject="MIZOKI3%20Architecture%20Briefing",
            bg_url=arch["closing_image"],
            bg_aria=arch["closing_aria"],
        )
        + """
</main>
"""
        + render_footer()
    )


def render_blog_article(post: dict) -> str:
    content_path = OUT / "blog" / "_content" / f"{post['slug']}.html"
    body = content_path.read_text(encoding="utf-8")

    return (
        page_head(f"MIZOKI3 — {post['title']}", post["meta_description"])
        + render_nav("/blog/")
        + """
<main>
"""
        + f"""
  <article class="article-page section section--solid has-grain">
    <div class="container">
      <header class="article-header reveal">
        <p class="breadcrumb"><a href="/blog/">MIZOKI3</a> → <a href="/blog/">Insights</a> → <span>{esc(post["tag"])}</span></p>
        <p class="accent-label accent-label--gold">{esc(post["tag"])}</p>
        <h1 class="serif-headline">{esc(post["title"])}</h1>
        <p class="article-subtitle">{esc(post["subtitle"])}</p>
        <p class="article-meta">{esc(post["date"])} · {esc(post["read_time"])}</p>
      </header>

      <div class="article-body">
        <div class="article-prose">
{body}
        </div>

        <div class="article-end">
          <a href="/blog/" class="article-back">← Back to Insights</a>
          <a href="mailto:hello@mizoki3.com?subject=MIZOKI3%20Demo%20Request" class="btn-primary">Schedule a Briefing</a>
        </div>
      </div>
    </div>
  </article>
"""
        + """
</main>
"""
        + render_footer()
    )


def render_blog() -> str:
    posts_html = []
    for post in BLOG_POSTS:
        posts_html.append(
            f"""      <article class="blog-post-card reveal">
        <time class="blog-date accent-label" datetime="{esc(post["date"])}">{esc(post["date"])}</time>
        <h2><a href="{esc(post["href"])}">{esc(post["title"])}</a></h2>
        <p class="blog-excerpt">{esc(post["excerpt"])}</p>
        <a href="{esc(post["href"])}" class="blog-read">Read →</a>
      </article>"""
        )

    return (
        page_head("MIZOKI3 — Insights", "Thinking on governed intelligence from MIZOKI3.")
        + render_nav("/blog/")
        + """
<main>

  <section class="blog-hero has-grain" aria-labelledby="blog-heading">
    <div class="container">
      <div class="blog-hero-inner reveal">
        <p class="accent-label">INSIGHTS</p>
        <h1 id="blog-heading" class="serif-headline">Thinking on governed intelligence.</h1>
      </div>
    </div>
  </section>

  <section class="section section--solid">
    <div class="container">
      <div class="blog-list reveal">
"""
        + "\n".join(posts_html)
        + """
      </div>
    </div>
  </section>

</main>
"""
        + render_footer()
    )


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {path.relative_to(OUT)}")


def main() -> None:
    print("Generating MIZOKI3 subpages…")
    for slug in LENS_ORDER:
        write_file(OUT / f"{slug}.html", render_lens(slug))
    write_file(OUT / "architecture.html", render_architecture())
    write_file(OUT / "blog" / "index.html", render_blog())
    for post in BLOG_POSTS:
        write_file(OUT / "blog" / f"{post['slug']}.html", render_blog_article(post))
    print("Done.")


if __name__ == "__main__":
    main()

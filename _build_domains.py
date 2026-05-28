#!/usr/bin/env python3
"""Generate the 5 MIZOKI3 domain lens pages from a shared template."""
from pathlib import Path

OUT = Path(__file__).parent

DOMAINS = {
    "counsel": {
        "title": "Counsel",
        "subtitle": "Legal Intelligence",
        "accent": "#6b85a8",
        "mission": "Convert legal complexity into verified strategic position.",
        "intro": "Counsel turns the unstructured weight of contracts, correspondence, and litigation into a continuously updated map of obligation, leverage, and exposure — feeding every other layer of the system.",
        "consumes": [
            "Contracts", "Amendments", "Litigation filings", "Discovery",
            "Negotiation transcripts", "Regulatory communications",
            "Email correspondence", "Voice transcripts", "Fiduciary documentation",
        ],
        "produces": [
            "Legal exposure mapping", "Contradiction detection",
            "Litigation pathway analysis", "Fiduciary deviation alerts",
            "Negotiation leverage scoring", "Obligation propagation graphs",
            "Procedural risk forecasting",
        ],
        "reinforces": ["risk", "estate", "capital"],
        "platform": {
            "brain": "Maps clauses, amendments, and correspondence into obligation nodes linked to entities across the graph.",
            "pipeline": "Legal signals enter at Sense; contradictions and exposure scores propagate through Validate before any downstream lens acts.",
            "gate": "Counsel-authored boundary conditions — covenants, consent requirements, litigation holds — become hard constraints at authorization.",
        },
        "scenario": {
            "id": "AMEND-842",
            "title": "Credit Agreement Amendment Mapping",
            "verdict": "deferred",
            "verdict_label": "Mapped to graph",
            "meta": [
                ("Instrument", "Senior Credit Facility"),
                ("Clause", "COV-01 · Min liquidity $10M"),
                ("Linked entities", "Acme Holdings · 3 subsidiaries"),
                ("Downstream impact", "Capital · Estate · Risk"),
            ],
            "outcome": "Counsel ingested the amendment and propagated <strong>COV-01</strong> into shared graph memory. When Capital later proposed ACT-991, the liquidity floor was already bound — no rediscovery required.",
        },
    },
    "estate": {
        "title": "Estate",
        "subtitle": "Wealth & Fiduciary Intelligence",
        "accent": "#9a8bc4",
        "mission": "Make multi-generational wealth structures legible, simulatable, and defensible.",
        "intro": "Estate models the long-tail dynamics of trusts, ownership, and beneficiary intent — turning instruments designed to outlive their drafters into a living, queryable substrate.",
        "consumes": [
            "Trusts", "Amendments", "Tax positions", "Estate documents",
            "Ownership hierarchies", "Banking relationships",
            "Fiduciary communications", "Beneficiary records",
        ],
        "produces": [
            "Trust restructuring intelligence", "Tax exposure forecasting",
            "Succession pathway simulations", "Beneficiary conflict mapping",
            "Trustee behavior intelligence", "Liquidity forecasting",
            "Estate optimization scenarios",
        ],
        "reinforces": ["counsel", "capital", "risk"],
        "platform": {
            "brain": "Models trust hierarchies, beneficiary relationships, and cross-entity ownership as a temporal graph — not a folder tree.",
            "pipeline": "Succession and distribution proposals are simulated against tax and fiduciary constraints before Capital or Counsel surfaces them for action.",
            "gate": "Fiduciary deviation alerts and beneficiary conflict scores feed directly into Risk authorization — blocking distributions that violate trust intent.",
        },
        "scenario": {
            "id": "TRUST-118",
            "title": "Beneficiary Distribution Pathway",
            "verdict": "deferred",
            "verdict_label": "Conflict surfaced",
            "meta": [
                ("Trust", "Whitfield Family · Gen II"),
                ("Proposed action", "Q4 discretionary distribution"),
                ("Conflict", "Class A vs Class B allocation"),
                ("Counsel link", "Amendment §4.2 interpretation"),
            ],
            "outcome": "Estate surfaced a <strong>beneficiary conflict</strong> before wire initiation. The proposal was deferred to Counsel for §4.2 interpretation — with a full causal trace of why distribution would breach stated intent.",
        },
    },
    "capital": {
        "title": "Capital",
        "subtitle": "Financial Intelligence",
        "accent": "#b8956a",
        "mission": "Give the enterprise causal foresight over capital.",
        "intro": "Capital reads the language of covenants, treasury, and counterparty behavior — converting financial position into forward-looking pathways the business can actually steer.",
        "consumes": [
            "Banking relationships", "Loan agreements", "Covenant structures",
            "Treasury telemetry", "Capital stack composition",
            "Cash flow intelligence", "Financing structures",
        ],
        "produces": [
            "Covenant breach forecasting", "Liquidity stress modeling",
            "Refinancing intelligence", "Capital allocation optimization",
            "Banking relationship scoring", "Restructuring pathways",
            "Negotiation leverage models",
        ],
        "reinforces": ["estate", "counsel", "signal", "risk"],
        "platform": {
            "brain": "Treasury position, covenant structures, and counterparty exposure live as causal nodes — not spreadsheet snapshots.",
            "pipeline": "Capital proposals traverse full SRPVDAL: stress-tested liquidity paths before any distribution or allocation reaches the Gate.",
            "gate": "Every capital action is scored against Counsel-mapped covenants and Risk policy — ACT-991 is the canonical veto pattern.",
        },
        "scenario": {
            "id": "ACT-991",
            "title": "Q3 Dividend Distribution",
            "verdict": "vetoed",
            "verdict_label": "Vetoed",
            "meta": [
                ("Amount", "$5,000,000"),
                ("Post-action liquidity", "$7,000,000 projected"),
                ("Covenant floor", "COV-01 · $10M minimum"),
                ("Deficit", "$3M vs boundary"),
            ],
            "outcome": "Capital proposed the distribution. Simulation projected liquidity below the <strong>COV-01</strong> floor Counsel had already mapped. Risk vetoed execution and routed to a safe alternative — with arithmetic, not opinion.",
        },
    },
    "signal": {
        "title": "Signal",
        "subtitle": "Marketing Intelligence",
        "accent": "#a89070",
        "mission": "Replace correlation-based marketing with causal autonomous acquisition.",
        "intro": "Signal rebuilds growth on causal ground: it learns what actually moves customers, then steers spend, channel, and creative through the same governed reasoning loop the rest of the enterprise uses.",
        "consumes": [
            "Meta advertising data", "Google advertising data", "CRM systems",
            "Customer journey telemetry", "Web analytics", "Engagement signals",
            "Conversion events", "Retention data",
        ],
        "produces": [
            "Causal attribution modeling", "Churn forecasting",
            "Lifetime-value prediction", "Autonomous bid optimization",
            "Activation threshold analysis", "Budget reallocation intelligence",
            "Customer intent mapping",
        ],
        "reinforces": ["capital", "risk", "counsel"],
        "platform": {
            "brain": "Customer journeys and channel interactions become causal edges — spend is linked to verified outcomes, not platform-reported attribution.",
            "pipeline": "Budget shifts require passing Validate against Capital liquidity constraints and Risk spend-governance policy before Act.",
            "gate": "Autonomous bid and allocation changes only execute when causal confidence clears threshold — correlation alone never authorizes.",
        },
        "scenario": {
            "id": "SIG-204",
            "title": "Cross-Channel Budget Reallocation",
            "verdict": "approved",
            "verdict_label": "Authorized",
            "meta": [
                ("Shift", "$120K · Meta → Google Search"),
                ("Causal basis", "ReLU threshold exceeded"),
                ("Capital check", "Within Q4 spend envelope"),
                ("Risk check", "Policy SIG-ALLOC-01"),
            ],
            "outcome": "Signal identified a causal activation threshold on Search — not a correlation spike. Capital confirmed envelope headroom. Risk authorized the reallocation with a full audit trail of the causal chain.",
        },
    },
    "risk": {
        "title": "Risk",
        "subtitle": "Verification & Compliance Intelligence",
        "accent": "#b85c5c",
        "mission": "Serve as the conscience, verifier, and governance layer of the entire system.",
        "intro": "Risk is not beside the system. Risk governs the system. Every consequential output produced anywhere in MIZOKI3 passes through Risk before it can be authorized to act.",
        "consumes": [
            "Cross-agent proposals", "Policy libraries", "Regulatory frameworks",
            "Operational telemetry", "Authorization histories",
            "Confidence distributions", "Simulation outputs", "Adversarial signals",
        ],
        "produces": [
            "Cross-agent verification", "Hallucination detection",
            "Contradiction arbitration", "Policy enforcement",
            "Regulatory compliance scoring", "Authorization scoring",
            "Tail-risk simulation", "Confidence arbitration",
            "Operational governance",
        ],
        "reinforces": [],
        "reinforces_note": "Every layer. Authorizes every consequential action.",
        "platform": {
            "brain": "Policy libraries, regulatory frameworks, and authorization histories form the governance substrate — queryable alongside operational graph memory.",
            "pipeline": "Risk sits at Validate and Decide — no proposal reaches Act without cross-agent verification and confidence arbitration.",
            "gate": "Risk is the Gate. Veto decisions include the arithmetic, policy citation, and causal trace — not a black-box refusal.",
        },
        "scenario": {
            "id": "AUTH-991",
            "title": "Cross-Lens Authorization · ACT-991",
            "verdict": "vetoed",
            "verdict_label": "Vetoed",
            "meta": [
                ("Proposal", "Capital · Q3 dividend"),
                ("Policy", "LIQ-COV-ENFORCE-01"),
                ("Simulation", "Post-action $7M vs $10M floor"),
                ("Arbitration", "Counsel boundary · Capital proposal"),
            ],
            "outcome": "Risk arbitrated Capital's proposal against Counsel-mapped <strong>COV-01</strong> and simulation output. Execution halted with cited policy, deficit arithmetic, and a routed safe alternative — visible in the Decision Control Plane.",
        },
    },
}

LENS_ORDER = ["counsel", "signal", "capital", "risk", "estate"]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>MIZOKI3 — {title} · {subtitle}</title>
<meta name="description" content="{mission}" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/assets/css/mizoki3.css" />
<style>
  :root {{ --lens-accent: {accent}; }}
  .domain-eyebrow {{ color: var(--lens-accent); }}
  .anatomy-block .section-label {{ color: var(--lens-accent); }}
</style>
</head>
<body>

<header class="site-header" id="header">
  <div class="container header-inner">
    <a href="/" class="logo">MIZOKI3</a>
    <nav class="nav">
      <div class="lens-nav" aria-label="Domain lenses">
{lens_nav_html}
      </div>
      <a href="/#how-it-works" class="nav-link hide-mobile">How It Works</a>
      <a href="/architecture" class="nav-link hide-mobile">Architecture</a>
      <a href="/console" class="nav-link hide-mobile">Console</a>
      <a href="mailto:hello@mizoki3.com?subject=MIZOKI3%20Demo%20Request" class="btn btn-primary">Schedule a Demo</a>
    </nav>
  </div>
</header>

<main>

  <section class="domain-hero" aria-labelledby="domain-heading">
    <div class="container domain-hero-grid">
      <div class="reveal">
        <p class="domain-eyebrow">{title} · {subtitle}</p>
        <h1 id="domain-heading">{mission}</h1>
        <p class="domain-intro">{intro}</p>
        <div class="domain-actions">
          <a href="mailto:hello@mizoki3.com?subject=MIZOKI3%20{title}%20Demo" class="btn btn-primary">Request a briefing</a>
          <a href="/#lenses" class="text-link">All lenses</a>
        </div>
      </div>

      <aside class="scenario-panel reveal" aria-label="{title} decision example">
        <div class="scenario-head">
          <span>{title} · Governed output</span>
          <span class="verdict-pill {scenario_verdict}">{scenario_verdict_label}</span>
        </div>
        <div class="scenario-body">
          <p class="scenario-id">{scenario_id}</p>
          <h2 class="scenario-title">{scenario_title}</h2>
          <dl class="scenario-meta">
{scenario_meta_html}
          </dl>
          <p class="scenario-outcome">{scenario_outcome}</p>
        </div>
        <div class="scenario-foot">
          <a href="/console">View in Decision Control Plane →</a>
        </div>
      </aside>
    </div>
  </section>

  <section class="bordered" aria-labelledby="anatomy-heading">
    <div class="container">
      <div class="reveal" style="margin-bottom: 2rem;">
        <p class="section-label">Lens anatomy</p>
        <h2 id="anatomy-heading" class="section-title">What enters. What the graph gains.</h2>
      </div>
      <div class="anatomy-grid reveal">
        <div class="anatomy-block">
          <p class="section-label">Consumes</p>
          <h3>The signals that enter {title}.</h3>
          <ul class="anatomy-list">
{consumes_html}
          </ul>
        </div>
        <div class="anatomy-block">
          <p class="section-label">Produces</p>
          <h3>The intelligence {title} contributes.</h3>
          <ul class="anatomy-list">
{produces_html}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="platform-strip" aria-labelledby="platform-heading">
    <div class="container">
      <div class="reveal" style="margin-bottom: 2rem;">
        <p class="section-label">Platform integration</p>
        <h2 id="platform-heading" class="section-title">Same architecture. Domain-specific reasoning.</h2>
        <p style="max-width: 36rem; font-size: 0.9375rem;">{title} does not run in isolation. It reads and writes the shared Temporal-Causal Knowledge Graph through the same governed pipeline every lens uses.</p>
      </div>
      <div class="platform-grid reveal">
        <div class="platform-cell">
          <h4>The Brain</h4>
          <p>{platform_brain}</p>
        </div>
        <div class="platform-cell">
          <h4>The Pipeline</h4>
          <p>{platform_pipeline}</p>
        </div>
        <div class="platform-cell">
          <h4>The Gate</h4>
          <p>{platform_gate}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="cross-lens">
    <div class="container cross-lens-inner reveal">
      <div>
        <p class="section-label">Reinforces</p>
        <p>{reinforces_text}</p>
      </div>
      <div class="cross-links" aria-label="Related lenses">
{cross_links_html}
      </div>
    </div>
  </section>

  <section class="cta-wrap" aria-labelledby="cta-heading">
    <div class="container cta-inner reveal">
      <div>
        <h2 id="cta-heading" class="section-title">See {title} in your context</h2>
        <p>We walk through domain-specific scenarios — obligation mapping, covenant enforcement, causal acquisition, fiduciary governance — on your terms.</p>
      </div>
      <a href="mailto:hello@mizoki3.com?subject=MIZOKI3%20{title}%20Demo" class="btn btn-primary">Schedule a Demo</a>
    </div>
  </section>

</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <span class="logo">MIZOKI3</span>
        <p>Patented autonomous decision intelligence. Proprietary architecture — not a wrapper on third-party models.</p>
        <div class="trust-row">
          <span class="trust-pill">Patented Technology</span>
          <span class="trust-pill">Customer-Managed Encryption</span>
          <span class="trust-pill">Proprietary Engine</span>
        </div>
      </div>
      <div class="footer-col">
        <h4>Lenses</h4>
        <ul>
          <li><a href="/counsel">Counsel</a></li>
          <li><a href="/signal">Signal</a></li>
          <li><a href="/capital">Capital</a></li>
          <li><a href="/risk">Risk</a></li>
          <li><a href="/estate">Estate</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Platform</h4>
        <ul>
          <li><a href="/architecture">Architecture</a></li>
          <li><a href="/console">Console</a></li>
          <li><a href="/blog/">Blog</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:hello@mizoki3.com">hello@mizoki3.com</a></li>
          <li><a href="mailto:hello@mizoki3.com?subject=MIZOKI3%20Demo%20Request">Schedule a Demo</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="year"></span> MIZOKI3 — Patented Autonomous Decision Intelligence</span>
      <a href="/login" class="text-link" style="font-size: inherit;">Sign In</a>
    </div>
  </div>
</footer>

<script>
(function () {{
  'use strict';
  document.getElementById('year').textContent = new Date().getFullYear();
  var header = document.getElementById('header');
  window.addEventListener('scroll', function () {{
    header.classList.toggle('scrolled', window.scrollY > 16);
  }}, {{ passive: true }});
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {{
    var obs = new IntersectionObserver(function (entries) {{
      entries.forEach(function (e) {{
        if (e.isIntersecting) {{ e.target.classList.add('visible'); obs.unobserve(e.target); }}
      }});
    }}, {{ threshold: 0.08, rootMargin: '0px 0px -24px 0px' }});
    document.querySelectorAll('.reveal').forEach(function (el) {{ obs.observe(el); }});
  }} else {{
    document.querySelectorAll('.reveal').forEach(function (el) {{ el.classList.add('visible'); }});
  }}
}})();
</script>
</body>
</html>
"""


def lens_nav(slug):
    lines = []
    for s in LENS_ORDER:
        label = DOMAINS[s]["title"]
        cls = ' class="active"' if s == slug else ""
        lines.append(f'        <a href="/{s}"{cls}>{label}</a>')
    return "\n".join(lines)


def cross_links(slug):
    others = [s for s in LENS_ORDER if s != slug]
    return "\n".join(
        f'        <a href="/{s}">{DOMAINS[s]["title"]}</a>' for s in others
    )


def reinforces_text(d):
    if d.get("reinforces_note"):
        return d["reinforces_note"]
    names = [DOMAINS[s]["title"] for s in d["reinforces"]]
    if len(names) == 1:
        return f"{d['title']} strengthens {names[0]} through shared graph memory."
    joined = ", ".join(names[:-1]) + f", and {names[-1]}"
    return f"What {d['title']} learns propagates to {joined} — one intelligence, many domains."


def render(slug, d):
    sc = d["scenario"]
    scenario_meta = "\n".join(
        f"            <div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in sc["meta"]
    )
    return TEMPLATE.format(
        title=d["title"],
        subtitle=d["subtitle"],
        accent=d["accent"],
        mission=d["mission"],
        intro=d["intro"],
        consumes_html="\n".join(f"            <li>{x}</li>" for x in d["consumes"]),
        produces_html="\n".join(f"            <li>{x}</li>" for x in d["produces"]),
        platform_brain=d["platform"]["brain"],
        platform_pipeline=d["platform"]["pipeline"],
        platform_gate=d["platform"]["gate"],
        scenario_id=sc["id"],
        scenario_title=sc["title"],
        scenario_verdict=sc["verdict"],
        scenario_verdict_label=sc["verdict_label"],
        scenario_meta_html=scenario_meta,
        scenario_outcome=sc["outcome"],
        reinforces_text=reinforces_text(d),
        lens_nav_html=lens_nav(slug),
        cross_links_html=cross_links(slug),
    )


if __name__ == "__main__":
    for slug, data in DOMAINS.items():
        path = OUT / f"{slug}.html"
        path.write_text(render(slug, data))
        print(f"wrote {path.name}")

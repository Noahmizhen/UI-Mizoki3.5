# CLAUDE.md - AI Assistant Guide for MIZ OKI Website

## Project Overview

This is the marketing and platform website for **MIZ OKI 3.5** — a Verifiable Autonomous Decision Intelligence platform. The website serves multiple purposes:
- Marketing landing pages for the platform
- Technical documentation and deep-dives
- Blog content on AI/ML decision intelligence topics
- Investor and sales materials
- Platform login portal

## Core Product Concept

MIZ OKI 3.5 implements a **7-Stage Autonomous Intelligence Pipeline** called **SRDPV-DAL**:

```
SENSE → REASON → PLAN → VALIDATE → DECIDE → ACT → LEARN
```

### Key Architectural Innovations

1. **Decision Control Plane (DCP)** — Centralized authority that authorizes all autonomous agent proposals
2. **Validation & Arbitration Layer (VAL)** — Multiple agents independently verify proposals
3. **Counterfactual Simulation Engine (CSE)** — Simulates alternatives before execution
4. **Temporal-Causal Knowledge Graph (TCO-KG)** — Decision memory and audit spine

### The Core Thesis

> "Decisions verified before execution—not explained after failure."

Agents **propose**, but the Decision Control Plane **authorizes**. This separation is the fundamental architectural constraint that enables governed autonomy.

## Repository Structure

```
mizoki-website/
├── index.html                  # Homepage - main marketing landing
├── login.html                  # Platform login page (mizoki.mizoki3.com)
├── how-it-works.html           # Technical deep-dive on SRDPV-DAL pipeline
├── platform.html               # Architecture overview & four-layer stack
├── security.html               # Quantum-resistant security, compliance
├── industries.html             # Industry-specific templates
├── pricing.html                # Enterprise, Growth, Pilot tiers
├── case-studies.html           # Customer success stories
├── resources.html              # Documentation hub
├── roi.html                    # Interactive ROI calculator
├── walkthrough.html            # 12-minute demo walkthrough
├── investor.html               # Investor overview deck
├── sales-one-pager.html        # Quick sales summary
├── blogs.html                  # Redirects to blog subdomain
│
├── blog/                       # Blog posts
│   ├── index.html              # Blog listing page
│   ├── decision-control-plane.html
│   └── relu-lens-meta-algorithm.html
│
├── assets/
│   ├── css/                    # Stylesheets (currently inline)
│   ├── img/                    # Images and graphics
│   └── pdf/                    # Downloadable PDFs (whitepapers, etc.)
│
├── Dockerfile                  # nginx:alpine container
├── nginx.conf                  # Web server config with subdomain routing
├── cloudbuild.yaml             # Google Cloud Build config
├── deploy.sh                   # One-click Cloud Run deployment
├── master-deploy.sh            # Multi-service deployment
├── github-push.sh              # Git push helper
├── README.md                   # User-facing documentation
└── CLAUDE.md                   # This file
```

## Design System

### Color Palette (CSS Variables)

```css
--bg-primary: #0a0a0f;         /* Deep black background */
--bg-secondary: #12121a;       /* Card backgrounds */
--bg-tertiary: #1a1a24;        /* Elevated surfaces */
--text-primary: #f0f0f5;       /* Main text */
--text-secondary: #9090a0;     /* Secondary text */
--text-muted: #606070;         /* Muted/disabled text */
--accent-cyan: #00d4ff;        /* Primary accent (CTAs, links) */
--accent-blue: #4f8fff;        /* Secondary accent */
--accent-purple: #a855f7;      /* REASON stage color */
--accent-green: #10b981;       /* VALIDATE/success */
--accent-orange: #f59e0b;      /* SENSE stage color */
--accent-red: #ef4444;         /* ACT stage/warnings */
--accent-pink: #f472b6;        /* LEARN stage color */
--border: rgba(255,255,255,0.08);
```

### Typography

- **Headlines:** `'Instrument Serif'` — Elegant, editorial feel
- **Body:** `'DM Sans'` — Clean, readable sans-serif
- **Code/Technical:** `'JetBrains Mono'` — Monospace for code, versions, labels

### Component Patterns

1. **Navigation Bar** — Fixed, blur backdrop, contains:
   - Logo with version badge
   - Nav links (desktop only)
   - CTA buttons: "Log in" (ghost) + primary action

2. **Section Labels** — Monospace, uppercase, cyan color, small text

3. **Cards** — Dark background, subtle border, hover glow effect

4. **Buttons:**
   - `.btn-primary` — Gradient cyan→blue, used for main CTAs
   - `.btn-ghost` — Transparent with border, secondary actions

5. **Pipeline Nodes** — Color-coded by stage, hover scales with glow

## Domain Configuration

| Domain | Service | Purpose |
|--------|---------|---------|
| `mizoki3.com` | mizoki-website | Main website homepage |
| `www.mizoki3.com` | mizoki-website | Main website (www alias) |
| `mizoki.mizoki3.com` | mizoki-website | Login portal (redirects to /login.html) |
| `blog.mizoki3.com` | (external) | Blog platform |
| `miz.mizoki3.com` | mizoki-docs-portal | Documentation portal |

### Subdomain Routing (nginx.conf)

The nginx config includes a `map` directive to detect the `mizoki.` subdomain and redirect to `/login.html`:

```nginx
map $host $is_mizoki_subdomain {
    default 0;
    "~^mizoki\.mizoki3\.com$" 1;
    "~^mizoki\." 1;
}

# In server block:
if ($is_mizoki_subdomain) {
    rewrite ^/$ /login.html permanent;
}
```

## Deployment

### Google Cloud Run

The site deploys to Cloud Run using the `deploy.sh` script:

```bash
./deploy.sh
```

This will:
1. Authenticate with gcloud
2. Enable required APIs
3. Build container with Cloud Build
4. Deploy to Cloud Run (us-central1)
5. Output the live URL

### GitHub Repository

```
https://github.com/mediaintelligence/mizoki-website
```

Always push changes to main branch. The deploy script commits changes before building.

## Common Tasks

### Adding a New Page

1. Create `newpage.html` using existing page as template
2. Update navigation in ALL HTML files (nav-cta section)
3. Add to Dockerfile if in subdirectory
4. Update this CLAUDE.md file structure section
5. Commit and deploy

### Adding a Blog Post

1. Create new file in `blog/` directory
2. Use existing blog post as template
3. Update `blog/index.html` to include new post
4. Commit and deploy

### Updating Navigation

The nav is inline in each HTML file. When updating:
- Check ALL HTML files for nav-cta sections
- Keep consistent: "Log in" (ghost) + primary CTA
- Blog pages use `../` relative paths

### Adding Assets

1. Place files in `assets/css/`, `assets/img/`, or `assets/pdf/`
2. Reference with relative paths: `assets/img/example.png`
3. Commit and deploy

## Key Metrics to Highlight

These are the core value propositions used across the site:

| Metric | Value | Description |
|--------|-------|-------------|
| Decision Velocity | 50-75× faster | Compared to manual processes |
| Revenue Leakage | ↓35% | Reduction in missed opportunities |
| Operational Costs | ↓41% | Cost reduction from automation |
| Payback Period | 3.2 months | Typical time to ROI |
| Automation Coverage | 89% | Decisions handled autonomously |
| Query Latency | <100ms | Knowledge graph response time |
| Decision Cycle | <60s | End-to-end decision time |

## SEO & Meta

Each page should include:
- Unique `<title>` with "MIZ OKI 3.5" brand
- `<meta name="description">` relevant to page content
- Proper heading hierarchy (single h1, logical h2/h3)

## Security Messaging

The platform emphasizes:
- **Quantum-resistant cryptography** (CRYSTALS-Kyber, CRYSTALS-Dilithium)
- **Immutable audit logs** — Every decision is cryptographically signed
- **Human-in-the-loop controls** — Full override capability
- **Multi-tenant isolation** — Kubernetes namespace separation

## Contact & Support

- Sales: sales@mizoki.com
- Documentation: resources.html
- Demo requests: walkthrough.html

---

*This file helps AI assistants understand the project structure, conventions, and context for making effective contributions.*

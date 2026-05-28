# MIZOKI3 — Marketing Site

Production site for **mizoki3.com** — homepage, five domain lenses, architecture, blog, and Decision Control Plane console.

**Stack:** Python Flask + Gunicorn on Google Cloud Run. HTML/CSS/JS front end with a Python build step for subpages.

**Canonical repo:** [github.com/Noahmizhen/UI-Mizoki3.5](https://github.com/Noahmizhen/UI-Mizoki3.5)

---

## Quick start (local)

```bash
python3 _build_site.py
PORT=8890 python3 app.py
# http://127.0.0.1:8890
```

See **[DEPLOY.md](./DEPLOY.md)** for editing content, tests, GCP deploy, and handoff details.

---

## Structure

```
index.html              # Homepage
counsel.html …          # Domain lens pages (generated)
architecture.html       # Technical architecture (generated)
blog/                   # Insights + articles
_build_site.py          # Regenerates lens/architecture/blog HTML
_build_site_data.py     # Page content data
assets/css/homepage.css # Homepage design system
assets/css/subpages.css # Subpages + blog articles
assets/js/homepage.js   # Homepage (nav, canvas graph, scroll)
assets/js/site.js       # Subpages (nav, reveals)
mizoki3-site/console/   # /console Decision Control Plane
app.py                  # Flask server + API routes
```

Regenerate subpages after editing `_build_site_data.py` or `blog/_content/`:

```bash
python3 _build_site.py
```

---

## Deploy

- **Auto:** push to `main` → GitHub Actions → Cloud Run (`mizoki-website`, `us-central1`, project `spry-bus-425315-p6`)
- **Manual:** `./deploy.sh`

Full instructions: **[DEPLOY.md](./DEPLOY.md)**

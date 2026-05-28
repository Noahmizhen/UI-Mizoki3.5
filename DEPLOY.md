# MIZOKI3 — Deploy & Handoff

Marketing site for **mizoki3.com**, served by Flask on **Google Cloud Run**.

**Canonical repo:** [github.com/Noahmizhen/UI-Mizoki3.5](https://github.com/Noahmizhen/UI-Mizoki3.5)

**GCP project:** `spry-bus-425315-p6` (production — same project, same domain)

---

## Local preview

Flask is required for routing (blog extensionless URLs, redirects, `/console`, APIs).

```bash
python3 _build_site.py          # regenerate lens + blog pages after editing _build_site_data.py
PORT=8890 python3 app.py
# open http://127.0.0.1:8890
```

Run tests:

```bash
python3 -m py_compile app.py mizoki_runtime/runtime.py
python3 -m unittest tests.test_app tests.test_runtime
```

---

## What to edit

| Content | Edit | Then run |
|---|---|---|
| Homepage | `index.html` | — |
| Lens pages, architecture, blog index | `_build_site_data.py` | `python3 _build_site.py` |
| Blog article bodies | `blog/_content/<slug>.html` | `python3 _build_site.py` |
| Decision Control Plane UI | `mizoki3-site/console/index.html` | — |
| Login / dashboard redirects | `app.py` → `EXTERNAL_LOGIN_URL`, `EXTERNAL_DASHBOARD_URL` | — |

---

## Production deploy (GitHub Actions — recommended)

Every push to `main` runs `.github/workflows/deploy-cloudrun.yml`:

1. Builds Docker image
2. Pushes to `gcr.io/spry-bus-425315-p6/mizoki-website:<sha>`
3. Rolls out Cloud Run service **`mizoki-website`** in **`us-central1`**

### Required GitHub secrets (repo Settings → Secrets)

| Secret | Value |
|---|---|
| `GCP_PROJECT_ID` | `spry-bus-425315-p6` |
| `WIF_PROVIDER` | `projects/698171499447/locations/global/workloadIdentityPools/github-actions/providers/github` |
| `WIF_SERVICE_ACCOUNT` | `miz-oki-website-deployer@spry-bus-425315-p6.iam.gserviceaccount.com` |

Workload Identity must trust this repo:

`Noahmizhen/UI-Mizoki3.5`

---

## Manual deploy (laptop)

Requires [gcloud CLI](https://cloud.google.com/sdk/docs/install) authenticated to `spry-bus-425315-p6`:

```bash
./deploy.sh
# or explicitly:
GCP_PROJECT_ID=spry-bus-425315-p6 ./deploy.sh
```

---

## Live routes

| URL | Serves |
|---|---|
| `/` | Homepage |
| `/counsel`, `/signal`, `/capital`, `/risk`, `/estate` | Domain lenses |
| `/architecture` | Technical architecture |
| `/blog/` | Insights index + 3 articles |
| `/console` | Decision Control Plane UI |
| `/infrastructure/main.tf` | Terraform reference module |
| `/login` | Redirects to command-center login |

Legacy paths (`/platform.html`, `/1/`, `/11/`, etc.) redirect to `/` or `/blog/`.

---

## Domain

**mizoki3.com** is already mapped to Cloud Run in `spry-bus-425315-p6`. Deploying a new revision updates the live site — no DNS change needed when using the same project and service.

---

## Repo layout (essential files)

```
app.py                    # Flask routing + Boss/MCP APIs
mizoki_runtime/           # Boss agent runtime
_build_site.py            # Subpage generator
_build_site_data.py       # Content data
index.html                # Homepage
counsel.html … estate.html, architecture.html
blog/                     # Blog index + articles (+ _content/ sources)
assets/css/homepage.css   # Homepage styles
assets/css/subpages.css   # Subpage + blog article styles
assets/js/homepage.js     # Homepage interactions
assets/js/site.js         # Subpage interactions
mizoki3-site/console/     # /console UI
Dockerfile                # Gunicorn container
.github/workflows/        # Auto-deploy on push to main
```

# MIZOKI3 — Operations Console & Infrastructure

This sub-tree carries two deliverables of the MIZOKI3 stack:

1. The standalone **Decision Control Plane** operations console.
2. The **Google Cloud Terraform** that provisions the fiduciary substrate.

The public marketing website lives in the **parent directory** (`../`) and is
served by the Flask app (`../app.py`) in the same container as everything else.
This sub-tree no longer ships its own Dockerfile, nginx config, or build
pipeline — those live at the parent level.

---

## 1. Contents

```
mizoki3-site/
├── README.md                  This file
├── console/
│   └── index.html             Decision Control Plane operations console
└── infrastructure/
    └── main.tf                Google Cloud Terraform (Spanner TCKG,
                               Pub/Sub, Cloud Run, Vertex AI, KMS, VPC)
```

The console is served by the parent Flask app at **`/console/`** (see the
`/console` route in `../app.py`). The Terraform file is also served raw at
**`/infrastructure/main.tf`** for reference.

---

## 2. The Operations Console

`console/index.html` is the Decision Control Plane terminal — a standalone
self-contained page in the MIZOKI3 dark brand style, with a live self-typing
SRPVDAL loop, TCKG subgraph view, and decision queue. It is linked from the
main site (DCP section and footer) and back-links to the homepage. It deploys
automatically with the parent site; no separate steps are needed.

To preview the console locally, run the parent Flask app:

```bash
cd ..
python3 app.py     # then open http://localhost:8080/console/
```

---

## 3. The Infrastructure (Terraform)

`infrastructure/main.tf` provisions the MIZOKI3 backend on **Google Cloud**.

### 3.1 What it provisions

| Component                | Google Cloud service                          |
|--------------------------|------------------------------------------------|
| Zero-trust network       | VPC + private subnet + Serverless VPC Connector |
| TCKG substrate           | **Cloud Spanner** with GoogleSQL property-graph schema, CMEK-encrypted |
| Nexus event bus          | Cloud Pub/Sub topic + ordered subscription     |
| SRPVDAL orchestrator     | Cloud Run service (internal-LB ingress only)   |
| Reasoning isolation      | Vertex AI custom IAM role pinned to a single approved Claude publisher model |
| Fiduciary encryption     | Cloud KMS (CMEK, 30-day rotation, prevent_destroy on the master key) |

Reasoning is pinned to a single approved Claude model on Vertex AI Model
Garden via a custom IAM role + resource-name condition. **The pinned model in
`main.tf` (`claude-3-5-sonnet-v2@20241022`) is outdated — bump to a current
approved Claude model on Vertex AI Model Garden before any production apply.**

### 3.2 Prerequisites

- [Terraform](https://developer.hashicorp.com/terraform/downloads) ≥ 1.5
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) (`gcloud`)
- A GCP project with billing enabled
- These APIs enabled:

```bash
gcloud services enable \
  compute.googleapis.com \
  run.googleapis.com \
  pubsub.googleapis.com \
  spanner.googleapis.com \
  cloudkms.googleapis.com \
  aiplatform.googleapis.com \
  vpcaccess.googleapis.com \
  --project=YOUR_PROJECT_ID
```

- Application Default Credentials for Terraform:

```bash
gcloud auth application-default login
```

### 3.3 Deploy

```bash
cd infrastructure
terraform init      # download the Google provider
terraform validate  # check syntax
terraform plan -var="project_id=YOUR_PROJECT_ID"
terraform apply -var="project_id=YOUR_PROJECT_ID"
```

### 3.4 Teardown

```bash
terraform destroy -var="project_id=YOUR_PROJECT_ID"
```

The Cloud KMS master key has `prevent_destroy = true` as a fiduciary safeguard.
To tear it down, remove that `lifecycle` block first — deliberately.

---

## 4. Notes

- **Migration note (2026-05-18):** an earlier draft of `main.tf` targeted AWS
  (Bedrock, Neptune, MSK, EKS). It was replaced because the website and
  orchestration run on Cloud Run and reasoning runs on Vertex AI, not Bedrock.
- **Model pin:** the Vertex AI binding pins a specific Claude publisher model.
  Bump the constant in `main.tf` to the current approved model before any
  production apply.
- **Contact** — the marketing site's CTA points to `hello@mizoki3.com`.

---

© 2026 MIZOKI3, Inc. · Miami, FL

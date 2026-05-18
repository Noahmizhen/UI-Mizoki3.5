# ==============================================================================
# MIZOKI3: AUTONOMOUS STRATEGIC INTELLIGENCE INFRASTRUCTURE  (Google Cloud)
# Architecture: Private VPC, Spanner Graph TCKG, Pub/Sub Event Bus,
#               Cloud Run Orchestration, Vertex AI (Claude) Reasoning Isolation
# ------------------------------------------------------------------------------
# Repo:  mizoki3-core-infrastructure
# Note:  The Vertex AI publisher-model ID below is pinned. Review/bump to the
#        current approved Claude model on Vertex AI before applying to
#        Production.
# ==============================================================================

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

variable "project_id" {
  description = "GCP project hosting MIZOKI3."
  type        = string
}

variable "region" {
  description = "Primary region. Cloud Run + Vertex AI live here."
  type        = string
  default     = "us-central1"
}

provider "google" {
  project = var.project_id
  region  = var.region

  default_labels = {
    environment = "production-fiduciary"
    system      = "mizoki3-nexus"
  }
}

# ------------------------------------------------------------------------------
# 1. THE FORTRESS (Private VPC)
# All reasoning and memory occurs in strictly private subnets. Public ingress
# is constrained to the Cloud Run service via a Serverless NEG.
# ------------------------------------------------------------------------------
resource "google_compute_network" "nexus_vpc" {
  name                    = "mizoki3-nexus-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "nexus_private" {
  name                     = "mizoki3-nexus-private"
  ip_cidr_range            = "10.0.1.0/24"
  region                   = var.region
  network                  = google_compute_network.nexus_vpc.id
  private_ip_google_access = true
}

resource "google_vpc_access_connector" "nexus_connector" {
  name          = "mizoki3-nexus-connector"
  region        = var.region
  network       = google_compute_network.nexus_vpc.name
  ip_cidr_range = "10.8.0.0/28"
  min_instances = 2
  max_instances = 10
}

# ------------------------------------------------------------------------------
# 2. THE SUBSTRATE: Temporal-Causal Knowledge Graph (TCKG)
# Cloud Spanner with the GoogleSQL property-graph schema hosts entities and
# causal physics. Bi-temporal semantics live in the graph itself.
# ------------------------------------------------------------------------------
resource "google_spanner_instance" "tckg_substrate" {
  name             = "mizoki3-tckg"
  config           = "regional-${var.region}"
  display_name     = "MIZOKI3 TCKG"
  processing_units = 1000
}

resource "google_spanner_database" "tckg_graph" {
  instance                 = google_spanner_instance.tckg_substrate.name
  name                     = "tckg-graph"
  version_retention_period = "7d"
  deletion_protection      = true

  encryption_config {
    kms_key_name = google_kms_crypto_key.mizoki_kms.id
  }
}

# ------------------------------------------------------------------------------
# 3. THE NERVOUS SYSTEM: Pub/Sub Event Bus
# Cross-domain updates (e.g., Counsel updates Capital instantly).
# ------------------------------------------------------------------------------
resource "google_pubsub_topic" "nexus_event_bus" {
  name                       = "mizoki3-nexus-bus"
  message_retention_duration = "604800s" # 7 days

  message_storage_policy {
    allowed_persistence_regions = [var.region]
  }
}

resource "google_pubsub_subscription" "nexus_orchestrator_pull" {
  name                       = "mizoki3-orchestrator-pull"
  topic                      = google_pubsub_topic.nexus_event_bus.id
  ack_deadline_seconds       = 60
  message_retention_duration = "604800s"
  enable_message_ordering    = true
}

# ------------------------------------------------------------------------------
# 4. THE EXECUTION ENGINE: Cloud Run (SRPVDAL Orchestration)
# Hosts the LangGraph multi-agent framework + the public website.
# Egress routed through the VPC connector so reasoning never leaves the VPC.
# ------------------------------------------------------------------------------
resource "google_service_account" "orchestrator_sa" {
  account_id   = "mizoki3-orchestrator"
  display_name = "MIZOKI3 SRPVDAL Orchestrator"
}

resource "google_cloud_run_v2_service" "orchestrator" {
  name     = "mizoki3-srpvdal-orchestrator"
  location = var.region
  ingress  = "INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER"

  template {
    service_account = google_service_account.orchestrator_sa.email

    scaling {
      min_instance_count = 1
      max_instance_count = 10
    }

    vpc_access {
      connector = google_vpc_access_connector.nexus_connector.id
      egress    = "ALL_TRAFFIC"
    }

    containers {
      image = "gcr.io/${var.project_id}/mizoki3-orchestrator:latest"
      resources {
        limits = {
          cpu    = "2"
          memory = "4Gi"
        }
      }
    }
  }
}

# ------------------------------------------------------------------------------
# 5. REASONING ISOLATION (Vertex AI IAM)
# Limits the orchestrator strictly to an approved Claude model on Vertex AI,
# without data leaving the project.
# ------------------------------------------------------------------------------
locals {
  # NOTE: pinned model — bump before production apply.
  claude_publisher_model = "publishers/anthropic/models/claude-3-5-sonnet-v2@20241022"

  claude_model_resource = "projects/${var.project_id}/locations/${var.region}/${local.claude_publisher_model}"
}

resource "google_project_iam_custom_role" "fiduciary_ai_role" {
  role_id     = "mizoki3FiduciaryVertexInvoker"
  title       = "MIZOKI3 Fiduciary Vertex Invoker"
  description = "Allows the orchestrator to invoke an approved Claude model via Vertex AI."
  permissions = [
    "aiplatform.endpoints.predict",
    "aiplatform.endpoints.streamRawPredict",
  ]
}

resource "google_project_iam_member" "orchestrator_vertex_binding" {
  project = var.project_id
  role    = google_project_iam_custom_role.fiduciary_ai_role.id
  member  = "serviceAccount:${google_service_account.orchestrator_sa.email}"

  condition {
    title       = "Pin to approved Claude model only"
    description = "Restricts invocation to the pinned Vertex AI publisher model."
    expression  = "resource.name == \"${local.claude_model_resource}\""
  }
}

resource "google_pubsub_topic_iam_member" "orchestrator_pubsub" {
  topic  = google_pubsub_topic.nexus_event_bus.id
  role   = "roles/pubsub.publisher"
  member = "serviceAccount:${google_service_account.orchestrator_sa.email}"
}

resource "google_spanner_database_iam_member" "orchestrator_tckg" {
  instance = google_spanner_instance.tckg_substrate.name
  database = google_spanner_database.tckg_graph.name
  role     = "roles/spanner.databaseUser"
  member   = "serviceAccount:${google_service_account.orchestrator_sa.email}"
}

# ------------------------------------------------------------------------------
# 6. ENCRYPTION (Cloud KMS)
# Master fiduciary key, used by Spanner and any downstream encrypted sinks.
# ------------------------------------------------------------------------------
resource "google_kms_key_ring" "mizoki" {
  name     = "mizoki3-fiduciary"
  location = var.region
}

resource "google_kms_crypto_key" "mizoki_kms" {
  name            = "mizoki3-master"
  key_ring        = google_kms_key_ring.mizoki.id
  rotation_period = "2592000s" # 30 days

  lifecycle {
    prevent_destroy = true
  }
}

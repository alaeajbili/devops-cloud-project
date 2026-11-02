# Projet DevOps / Cloud : API sur AWS simulé (LocalStack)

API de gestion de tâches (FastAPI) conteneurisée, infrastructure AWS décrite en **Terraform** (testée sur **LocalStack**), pipeline **CI/CD GitHub Actions** avec scans de sécurité, monitoring **Prometheus / Grafana**.

## Stack

| Brique | Outil |
|---|---|
| App | FastAPI + PostgreSQL |
| Conteneurs | Docker, docker compose |
| Cloud AWS simulé | LocalStack |
| IaC | Terraform |
| CI/CD | GitHub Actions |
| Sécurité | Trivy, Checkov |
| Monitoring | Prometheus, Grafana |

## Démarrage rapide

```bash
# API + base
docker compose up -d --build
curl http://localhost:8000/health

# Tests en local
pip install -r app/requirements.txt -r app/requirements-dev.txt
cd app && pytest

# LocalStack + Terraform (à partir de la semaine 2)
docker compose --profile aws up -d localstack
cd terraform && terraform init && terraform apply
```

> **PC avec 8 Go de RAM :** ne lance pas tout en même temps. `docker compose down` entre chaque phase. Limite WSL2 à 3 Go via `C:\Users\<toi>\.wslconfig`.

## Plan : 6 semaines x 10h

- [ ] **Semaine 1 : Fondations et app.** Setup WSL2, Git, Docker, Terraform, AWS CLI. API connectée à PostgreSQL (SQLAlchemy), tests, `docker compose`.
- [ ] **Semaine 2 : CI et premier Terraform.** Workflow GitHub Actions, push vers ghcr.io, Trivy. LocalStack + S3, IAM, SQS.
- [ ] **Semaine 3 : Terraform sérieux.** VPC, sous-réseaux, security groups en modules réutilisables, state distant, workspaces dev/prod.
- [ ] **Semaine 4 : CI/CD Terraform et sécurité.** `plan` sur chaque PR, `apply` sur LocalStack, Checkov, secrets propres.
- [ ] **Semaine 5 : Monitoring.** `/metrics`, Prometheus + Grafana, dashboard, alerte qui se déclenche vraiment.
- [ ] **Semaine 6 : Finitions.** Schéma d'architecture, choix techniques, section « en vrai AWS », bonus k3d, pitch de 2 minutes.

## Architecture

_À compléter en semaine 6 (schéma + explication de chaque brique)._

## Ce que je ferais sur le vrai AWS

_À compléter : ECS Fargate, RDS, ALB, Secrets Manager, CloudWatch, OIDC GitHub, estimation des coûts._



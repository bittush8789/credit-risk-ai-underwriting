# DevOps & GitOps Architecture

## 1. CI/CD Flow
```mermaid
graph TD
    Code[Git Commit] --> CI[GitHub Actions]
    CI -->|Scan| Snyk[Snyk/Trivy]
    CI -->|Build| Docker[Docker Build]
    Docker -->|Push| Registry[Amazon ECR]
    Registry -->|Update Manifest| Git[Git Repo]
    Git -->|Detect Change| Argo[ArgoCD]
    Argo -->|Sync| EKS[AWS EKS Cluster]
```

## 2. Key Principles
- **GitOps**: All infrastructure and application states are defined in Git.
- **Immutable Artifacts**: Docker images are tagged with unique SHAs and never overwritten.
- **Automated Security**: Trivy scans images for vulnerabilities before they reach the registry.

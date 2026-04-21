# GitHub Actions: CI/CD Guide

## 1. Pipeline Overview
The `.github/workflows/mlops.yml` handles:
- **Linting**: Ensuring code quality.
- **Testing**: Running Pytest for the rule engine.
- **Docker Build**: Building the FastAPI and Trainer images.
- **Push**: Sending images to Amazon ECR.
- **Update**: Modifying the K8s manifests with the new Image Tag.

## 2. Secrets Configuration
Required secrets in GitHub:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `EKS_CLUSTER_NAME`
- `ECR_REPOSITORY`

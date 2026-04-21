# ArgoCD: GitOps Guide

## 1. Industry Use Case
ArgoCD ensures the "Desired State" in GitHub matches the "Actual State" in EKS. This prevents configuration drift and allows for one-click rollbacks.

## 2. Installation
```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## 3. Connecting the Repo
```bash
argocd repo add https://github.com/bittush8789/credit-risk-ai-underwriting.git --username ... --password ...
```

## 4. Troubleshooting
If the sync fails, check the "Events" tab in the ArgoCD UI for RBAC errors or invalid YAML syntax.

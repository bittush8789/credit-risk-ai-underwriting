# End-to-End Local Deployment Guide

## 1. Environment Preparation
```bash
kind create cluster --name credit-risk
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

## 2. Deploy Infrastructure
```bash
# Install ArgoCD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Install KServe
helm install kserve-stack ./kubernetes/charts/kserve
```

## 3. Deploy Application
```bash
kubectl apply -f argocd/local-app.yaml
```

## 4. Test the API
```bash
curl -X POST http://localhost/predict -d @tests/sample_payload.json
```

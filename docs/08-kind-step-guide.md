# Kind: Local Kubernetes Guide

## 1. Industry Use Case
Kind (Kubernetes in Docker) allows developers to test complex MLOps manifests (like KServe) locally before incurring AWS costs.

## 2. Cluster Creation
```bash
# Create cluster with Nginx Ingress support
kind create cluster --name credit-risk --config scripts/kind-config.yaml
```

## 3. Ingress Controller Setup
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

## 4. Verification
```bash
kubectl get nodes
kubectl get pods -A
```

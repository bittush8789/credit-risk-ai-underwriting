# Kubernetes Foundations Guide

## 1. Core Concepts
In this project, we use native K8s resources to manage our banking services:
- **Namespaces**: `credit-risk-prod` for environment isolation.
- **Secrets**: Encrypted storage for DB passwords and AWS keys.
- **ConfigMaps**: Application settings and model hyperparameters.

## 2. Resource Management
```bash
# Apply initial namespace and RBAC
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/rbac.yaml
```

## 3. Production Best Practices
- **Resource Limits**: Always set CPU/Memory limits to prevent one pod from crashing the node.
- **Liveness Probes**: Ensures K8s automatically restarts the FastAPI pod if it hangs.

# Amazon EKS: Managed Kubernetes Guide

## 1. Industry Use Case
AWS EKS removes the burden of managing the Kubernetes Control Plane, allowing the MLOps team to focus on model scaling and feature delivery.

## 2. Cluster Creation (Eksctl)
```bash
eksctl create cluster \
  --name credit-risk-prod \
  --region us-east-1 \
  --with-oidc \
  --nodes 3 \
  --node-type t3.medium
```

## 3. Node Scaling
We use Managed Node Groups with Cluster Autoscaler to handle surges in loan application traffic during business hours.

## 4. Resume Explanation
"Architected and deployed a production-grade EKS cluster to host KServe-based credit underwriting models, utilizing IAM Roles for Service Accounts (IRSA) to achieve least-privilege security."

# End-to-End AWS Deployment Guide

## 1. Cloud Infrastructure
```bash
cd terraform
terraform init
terraform apply -auto-approve
```

## 2. Cluster Onboarding
```bash
aws eks update-kubeconfig --name credit-risk-prod
kubectl apply -f kubernetes/alb-controller.yaml
```

## 3. GitOps Link
```bash
kubectl apply -f argocd/prod-app.yaml
```

## 4. Production Verification
1. Log in to the AWS Console.
2. Verify the Load Balancer is `Active`.
3. Check the Grafana dashboard for successful scrape targets.
4. Perform a real prediction using the ALB public DNS.

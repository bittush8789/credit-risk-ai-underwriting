# Terraform: AWS Infrastructure Guide

## 1. Why IaC?
Manual infrastructure creation is prone to errors. Terraform allows us to recreate the entire CreditRisk ecosystem (VPC, S3, EKS) in minutes.

## 2. Core Resources
- `vpc.tf`: Multi-AZ network setup.
- `eks.tf`: Managed Kubernetes cluster.
- `iam.tf`: OIDC and IRSA configuration.

## 3. Operations
```bash
cd terraform
terraform init
terraform plan -out=plan.out
terraform apply "plan.out"
```

## 4. Best Practices
- **State Locking**: Use DynamoDB for state locking in team environments.
- **Modules**: Use verified modules (e.g., `terraform-aws-modules/eks/aws`).

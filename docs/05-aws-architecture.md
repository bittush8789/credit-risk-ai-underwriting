# AWS Production Architecture

## 1. Cloud Ecosystem
```mermaid
graph TD
    User[Internet] --> ALB[AWS Load Balancer]
    ALB --> EKS[Amazon EKS Cluster]
    EKS -->|Scale| KAR[Karpenter/Autoscaler]
    EKS -->|Logs| CW[CloudWatch]
    EKS -->|Data| S3[Amazon S3]
    EKS -->|Secrets| ASM[AWS Secrets Manager]
    EKS -->|Identity| IAM[IAM Roles for Service Accounts]
```

## 2. Infrastructure as Code (Terraform)
- **VPC Module**: Configures Public/Private subnets across 3 Availability Zones.
- **EKS Module**: Manages the Managed Node Groups and OIDC provider.
- **ALB Controller**: Dynamically creates AWS Application Load Balancers for Kubernetes Ingress resources.
- **IAM (IRSA)**: Ensures Pods have specific, least-privilege access to S3 and Secrets Manager without using long-lived keys.

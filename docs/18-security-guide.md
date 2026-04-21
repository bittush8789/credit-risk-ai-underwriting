# Security & Compliance Guide

## 1. Authentication
All API requests must include a **JWT Bearer Token**. The backend validates this token against the OIDC provider before processing the loan application.

## 2. Infrastructure Security
- **Private Subnets**: All EKS worker nodes and databases reside in private subnets with no direct internet access.
- **ALB WAF**: AWS Web Application Firewall protects the public endpoint against SQL injection and DDoS attacks.

## 3. Image Scanning (Trivy)
The CI pipeline runs:
```bash
trivy image --severity HIGH,CRITICAL credit-risk-backend:v1
```
Any high-severity vulnerability will automatically fail the build.

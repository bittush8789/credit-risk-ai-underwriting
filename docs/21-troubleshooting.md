# Troubleshooting Guide

## 1. KServe Pods Pending
- **Cause**: Insufficient CPU/Memory on the Kind/EKS nodes.
- **Fix**: Check `kubectl describe node`. For Kind, increase Docker Desktop memory to 8GB+.

## 2. ArgoCD Not Syncing
- **Cause**: SSH/Personal Access Token for the Private Repo has expired.
- **Fix**: Update the repository secret in the ArgoCD UI settings.

## 3. Model Loading Failed
- **Cause**: IAM Role doesn't have `s3:GetObject` permission for the specific bucket.
- **Fix**: Verify the IRSA (IAM Role for Service Account) configuration in the `terraform/iam.tf` file.

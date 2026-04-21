# Prerequisites Guide

## 1. Hardware
- **Local Dev**: Minimum 16GB RAM, i5/i7 Processor.
- **Cloud**: AWS Account with Administrator access.

## 2. CLI Tools
| Tool | Installation Command (macOS/Linux) | Purpose |
| :--- | :--- | :--- |
| **Docker** | `brew install --cask docker` | Containerization engine |
| **Kind** | `brew install kind` | Local Kubernetes clusters |
| **Kubectl** | `brew install kubectl` | K8s CLI |
| **Helm** | `brew install helm` | K8s Package Manager |
| **Terraform**| `brew install terraform` | IaC |
| **AWS CLI** | `brew install awscli` | AWS Management |
| **Eksctl** | `brew install eksctl` | EKS Cluster CLI |

## 3. Python Environment
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# KServe: Model Serving Guide

## 1. Why KServe?
KServe provides a standardized "InferenceService" abstraction. In an enterprise setting, it handles:
- **Serverless Scaling**: Scales to zero when no loan requests are active.
- **Canary Rollouts**: Safely test Model V2 with 10% traffic.
- **Protocol Standardization**: Uses the V2 Inference Protocol.

## 2. Installation (Helm)
```bash
helm repo add kserve https://kserve.github.io/charts
helm install kserve-stack kserve/kserve-stack --namespace kserve --create-namespace
```

## 3. Deploying the Underwriting Model
```yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: credit-risk-model
spec:
  predictor:
    sklearn:
      storageUri: s3://credit-risk-bucket/v4/
```

## 4. Verification
```bash
kubectl get inferenceservice credit-risk-model
```

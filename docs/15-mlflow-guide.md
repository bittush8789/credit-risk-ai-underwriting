# MLflow: Model Registry Guide

## 1. Experiment Tracking
Every training run logs:
- **Metrics**: Accuracy, F1-Score, Default Recall.
- **Parameters**: XGBoost `eta`, `max_depth`.
- **Artifacts**: The serialized model and scaler.

## 2. Model Registry
We use the MLflow Model Registry to manage lifecycle stages:
- `Staging`: For candidate models being tested in Kind.
- `Production`: For the live model currently served by KServe in EKS.

## 3. Implementation
```python
import mlflow
with mlflow.start_run():
    mlflow.log_param("max_depth", 5)
    mlflow.log_metric("accuracy", 0.94)
    mlflow.sklearn.log_model(model, "model")
```

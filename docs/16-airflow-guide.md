# Apache Airflow: Pipeline Orchestration Guide

## 1. Why Airflow?
Complex MLOps requires more than just cron jobs. Airflow manages dependencies, retries, and monitoring for the data-to-deployment pipeline.

## 2. DAG Flow
```python
# dag_credit_risk_retrain.py
extract >> validate >> train >> evaluate >> register >> deploy
```

## 3. Retraining Trigger
The pipeline is triggered automatically if **Evidently AI** detects a feature drift score > 0.3, ensuring the model never degrades silently.

## 4. Best Practices
- **Idempotency**: Ensure that running the same DAG twice doesn't create duplicate data.
- **Dynamic DAGs**: Use templates to handle different environments (Staging/Production).

# Interview Guide: CreditRisk AI

## 1. How do you handle Model Drift in Production?
"In this project, I integrated **Evidently AI** with **Prometheus**. We monitor the feature distribution of incoming prediction requests. If the drift score exceeds a threshold, an **Airflow DAG** is triggered to retrain the model on the latest data stored in S3."

## 2. Why did you choose KServe over a simple FastAPI container?
"KServe provides built-in support for **Canary deployments**, **Auto-scaling to zero**, and standardized **V2 Inference Protocol**. In an enterprise environment, this level of abstraction is essential for reliability and scaling."

## 3. Explain the GitOps flow in this project.
"We use **ArgoCD** as our GitOps controller. Every time a new model is registered in **MLflow**, our **GitHub Actions** pipeline updates the `inference.yaml` with the new S3 URI. ArgoCD detects this change in Git and automatically syncs the EKS cluster state to deploy the new model."

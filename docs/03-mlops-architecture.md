# MLOps Architecture

## 1. Lifecycle Diagram
```mermaid
graph LR
    subgraph Development
    NB[Notebooks] --> MLF[MLflow Tracking]
    MLF --> REG[MLflow Registry]
    end
    
    subgraph Automation
    AF[Airflow DAGs] -->|Retrain| REG
    REG -->|Trigger| GHA[GitHub Actions]
    end
    
    subgraph Deployment
    GHA -->|Push| ECR[Amazon ECR]
    ECR -->|Sync| ARGO[ArgoCD]
    ARGO -->|Deploy| KSRV[KServe]
    end
```

## 2. Tool Integration
- **DVC**: Manages data versioning to ensure reproducibility.
- **MLflow**: Tracks experiments, parameters (Learning Rate, Max Depth), and versions the final model.
- **Evidently AI**: Monitors model drift in production by comparing incoming feature distributions with training data.
- **Airflow**: Orchestrates the retraining pipeline when drift exceeds a specific threshold.

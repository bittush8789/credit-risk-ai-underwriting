# Project Overview: CreditRisk AI

## 1. Vision
CreditRisk AI is an institutional-grade platform designed to automate the loan underwriting lifecycle. It moves beyond simple binary classification to provide a comprehensive risk assessment, including probability of default (PD), risk banding, and explainable logic.

## 2. Business Objectives
- **Reduce Delinquency**: By using advanced boosting algorithms (XGBoost/CatBoost).
- **Audit Compliance**: Every decision generates a PDF report and captures feature contributions.
- **Operational Efficiency**: Moving from manual reviews to sub-second automated decisions.

## 3. High-Level Stack
- **AI**: XGBoost, CatBoost, MLflow, Feast.
- **Platform**: Kubernetes, KServe, ArgoCD, AWS EKS.
- **Backend**: FastAPI, Pydantic, SQLAlchemy.

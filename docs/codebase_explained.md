# Codebase Explained

This document outlines the purpose and functionality of each core file in the repository.

## 📂 Frontend (`frontend/`)
### `index.html`
- **Purpose**: The main landing page.
- **Why?**: To provide a professional entry point for users and stakeholders.
- **Use Case**: Introduces the platform's value proposition.

### `predict.html`
- **Purpose**: The core underwriting interface.
- **Use Case**: Where the loan officer or applicant enters data for real-time analysis.

### `js/predict.js`
- **Purpose**: Handles all frontend logic.
- **What it does**: Gathers form data, sends it to the FastAPI backend, and updates the UI with the returned decision and PDF link.

## 📂 Backend (`backend/`)
### `main.py`
- **Purpose**: The API entry point.
- **Why FastAPI?**: Chosen for its high performance, async support, and automatic OpenAPI (Swagger) documentation.
- **Inputs**: JSON payload (ApplicantData).
- **Outputs**: JSON (Risk Level, Score, PDF URL).

### `model_loader.py`
- **Purpose**: Singleton class to manage ML model loading.
- **Why?**: Loading 120k-row models is expensive. This file ensures artifacts are loaded into memory exactly once at startup.

### `utils.py`
- **Purpose**: Business logic and helper functions.
- **What it does**: Handles feature engineering, calls the model for inference, and generates the final PDF report.

### `schemas.py`
- **Purpose**: Data validation using Pydantic.
- **Why?**: Ensures that the API only accepts valid financial data types, preventing runtime errors.

### `rule_engine.py`
- **Purpose**: Post-inference decision logic.
- **Business Use Case**: Enforces banking "knock-out" rules that must override ML scores for regulatory compliance.

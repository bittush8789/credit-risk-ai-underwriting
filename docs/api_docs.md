# API Documentation

The CreditRisk AI backend is a RESTful API powered by FastAPI.

## Base URL
`http://127.0.0.1:8000`

## Endpoints

### 1. Health Check
`GET /health`
- **Description**: Returns the system status and model engine version.
- **Response**: `{"status": "healthy", "engine": "V4_XGBoost_Calibrated"}`

### 2. Model Info
`GET /model-info`
- **Description**: Returns technical metadata about the trained model.
- **Response**: Includes features, training metrics, and architecture type.

### 3. Predict Underwriting
`POST /predict`
- **Description**: Performs full underwriting analysis on a loan applicant.
- **Payload**:
```json
{
  "age": 30,
  "annual_income": 75000,
  "employment_years": 5,
  "monthly_expenses": 2000,
  "savings_balance": 20000,
  "dependents": 0,
  "loan_purpose": "Home",
  "residence_type": "Owned",
  "credit_score": 720,
  "loan_amount": 15000,
  "total_debt": 5000,
  "active_loans": 1,
  "delayed_payments": 0
}
```
- **Response**: Returns risk level, approval chance, confidence score, and a link to the PDF report.

### 4. Download Report
`GET /api/v1/predict/report/{filename}`
- **Description**: Downloads the generated PDF underwriting report.

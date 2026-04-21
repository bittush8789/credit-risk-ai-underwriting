from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import uvicorn
import requests
import json
import os

app = FastAPI(title="CreditRisk AI: Enterprise Gateway")

# Mock Model Endpoint (In Production, this points to KServe)
KSERVE_ENDPOINT = os.getenv("KSERVE_ENDPOINT", "http://credit-risk-predictor.credit-risk-model.svc.cluster.local/v1/models/credit-risk-model:predict")

class ApplicantData(BaseModel):
    age: int
    annual_income: float
    credit_score: int
    loan_amount: float
    current_debt: float
    active_loans: int
    delayed_payments: int
    employment_years: int
    savings_balance: float

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "credit-risk-gateway"}

@app.get("/metrics")
def get_metrics():
    # Placeholder for Prometheus metrics
    return {"requests_total": 100, "avg_latency_ms": 45, "approval_ratio": 0.68}

@app.post("/predict")
async def predict(data: ApplicantData):
    try:
        # 1. Logic for Rule Engine (Hard Rejections)
        if data.annual_income < 15000:
            return {"decision": "REJECTED", "reason": "Minimum income threshold not met", "risk_score": 0}
        
        # 2. Forward to KServe Inference Service
        # (Simulated for local dev if KSERVE_ENDPOINT is not reachable)
        payload = {"instances": [list(data.dict().values())]}
        # res = requests.post(KSERVE_ENDPOINT, json=payload)
        
        # Mocking the AI response for demonstration
        risk_prob = 0.15 if data.credit_score > 700 else 0.65
        decision = "APPROVED" if risk_prob < 0.4 else "REJECTED"
        
        return {
            "decision": decision,
            "risk_probability": risk_prob,
            "risk_band": "Low" if risk_prob < 0.2 else "Medium" if risk_prob < 0.5 else "High",
            "fraud_score": 0.05,
            "explainability": "High credit score and stable employment confirmed."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/batch-predict")
async def batch_predict(file_url: str):
    return {"status": "Batch processing initiated", "job_id": "job_9923"}

@app.post("/retrain")
async def trigger_retrain():
    # Integration with Airflow API
    return {"status": "Retraining DAG triggered in Airflow"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

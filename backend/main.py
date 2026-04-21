import logging
import time
import uuid
import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse

from .schemas import ApplicantData
from .utils import predict_underwriting, generate_enterprise_report
from .model_loader import engine

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("CreditRiskAPI")

app = FastAPI(
    title="🏦 CreditRisk AI - Enterprise Platform",
    description="Banking-grade Credit Risk Underwriting Engine.",
    version="1.0.0"
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "healthy", "engine": "V4_XGBoost_Calibrated"}

@app.get("/model-info", tags=["System"])
def get_model_info():
    return {
        "architecture": "XGBoost Classifier",
        "calibration": "Platt Scaling / CalibratedClassifierCV",
        "features": engine.meta['features'],
        "metrics": {"accuracy": 0.942, "precision": 0.925}
    }

@app.post("/predict", tags=["Underwriting"])
async def predict_single(applicant: ApplicantData):
    """Executes the underwriting engine for a single applicant."""
    try:
        applicant_id = uuid.uuid4().hex[:4].upper()
        
        # Run inference
        results = predict_underwriting(applicant.dict())
        
        # Generate PDF
        report_name = generate_enterprise_report(applicant_id, results, applicant.dict())
        results['report_url'] = f"/api/v1/predict/report/{report_name}"
        
        return results
    except Exception as e:
        logger.error(f"Underwriting process failed: {e}")
        raise HTTPException(status_code=500, detail="Internal decision engine error")

@app.get("/api/v1/predict/report/{filename}", tags=["Underwriting"])
async def download_report(filename: str):
    """Serves the generated PDF report."""
    path = os.path.join(os.path.dirname(__file__), "..", "reports", filename)
    if os.path.exists(path):
        return FileResponse(path, media_type='application/pdf', filename=filename)
    raise HTTPException(status_code=404, detail="Report not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

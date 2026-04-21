# Execution Runbook

Follow these steps to initialize and run the CreditRisk AI platform.

## 1. Prerequisites
- Python 3.10+
- Recommended: Virtual Environment (venv)

## 2. Installation
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

## 3. Starting the Backend
```bash
# From the root directory
uvicorn backend.main:app --host 127.0.0.1 --port 8000
```
- **Verify**: Open `http://127.0.0.1:8000/health` in your browser. You should see a "healthy" status.

## 4. Running the Frontend
- Locate the `frontend/index.html` file.
- Open it in Chrome, Firefox, or Edge.
- Navigate to the **Predict** page.
- Enter sample data (e.g., use values from `data/sample_bulk_upload.csv`).
- Click **"Execute Intelligence Engine"**.

## 5. Troubleshooting
- **Model Loading Error**: Ensure all `.pkl` files are present in the `models/` directory.
- **Port Conflict**: If port 8000 is in use, run uvicorn on a different port: `--port 8080` and update `predict.js` accordingly.
- **Dependency Issues**: If `xgboost` or `pandas` fails to install, ensure your `pip` is upgraded: `python -m pip install --upgrade pip`.

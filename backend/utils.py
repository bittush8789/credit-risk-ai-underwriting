import numpy as np
import pandas as pd
import os
import logging
from fpdf import FPDF
from .rule_engine import apply_enterprise_underwriting_rules
from .model_loader import engine

logger = logging.getLogger("CreditRiskAPI")

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, "..", "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

def predict_underwriting(data: dict):
    """
    Core inference function for credit underwriting.
    Calculates financial ratios, performs ML prediction, and applies business rules.
    """
    model = engine.model
    scaler = engine.scaler
    encoder = engine.encoder
    meta = engine.meta
    
    # 1. Feature Engineering
    data['debt_to_income'] = data['total_debt'] / (data['annual_income'] + 1)
    data['loan_to_income'] = data['loan_amount'] / (data['annual_income'] + 1)
    data['expense_to_income'] = (data.get('monthly_expenses', 0) * 12) / (data['annual_income'] + 1)
    data['savings_to_loan_ratio'] = data.get('savings_balance', 0) / (data['loan_amount'] + 1)
    
    # Prep features
    X_raw = pd.DataFrame([[
        data['age'], data['annual_income'], data.get('employment_years', 0), 
        data.get('monthly_expenses', 0), data.get('savings_balance', 0),
        data['credit_score'], data.get('active_loans', 0), data.get('delayed_payments', 0), 
        data['total_debt'], data['loan_amount'], data.get('dependents', 0),
        data['debt_to_income'], data['loan_to_income'], data['expense_to_income'], 
        data['savings_to_loan_ratio']
    ]], columns=meta['features'])
    
    X_scaled = scaler.transform(X_raw)
    
    # 2. Inference
    probs = model.predict_proba(X_scaled)[0]
    pred_idx = np.argmax(probs)
    risk_class = encoder.inverse_transform([pred_idx])[0]
    confidence = round(float(np.max(probs)) * 100, 2)
    
    # Initial ML assessment
    ml_res = {
        "risk_level": risk_class,
        "approval_chance": 95.0 if risk_class == "Low Risk" else (50.0 if risk_class == "Medium Risk" else 5.0),
        "confidence_score": confidence,
        "risk_reasons": []
    }
    
    # 3. Apply Enterprise Rules (Post-Inference)
    final_res = apply_enterprise_underwriting_rules(data, ml_res)
    return final_res

def generate_enterprise_report(applicant_id, results, applicant_data):
    """
    Generates a professional PDF underwriting report for the applicant.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(190, 15, "CreditRisk AI - Enterprise Underwriting", 0, 1, 'C')
    
    pdf.ln(5)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(190, 10, f"System ID: {applicant_id} | Recommendation: {results['recommendation']}", 0, 1)
    
    # Financial Ratios Table
    pdf.ln(5)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(95, 10, "Metric", 1, 0, 'C', True)
    pdf.cell(95, 10, "Value", 1, 1, 'C', True)
    
    ratios = results.get('financial_ratios', {})
    for k, v in ratios.items():
        pdf.cell(95, 10, k, 1, 0)
        pdf.cell(95, 10, str(v), 1, 1)

    pdf.ln(10)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(190, 10, "Decision Analysis & Risk Factors:", 0, 1)
    pdf.set_font("Helvetica", "", 11)
    for reason in results['risk_reasons']:
        pdf.multi_cell(190, 8, f"- {reason}", 0, 'L')
        
    report_name = f"Enterprise_Report_{applicant_id}.pdf"
    path = os.path.join(REPORTS_DIR, report_name)
    pdf.output(path)
    return report_name

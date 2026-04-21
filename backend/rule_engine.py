import logging

logger = logging.getLogger("CreditRiskAPI")

def apply_enterprise_underwriting_rules(applicant_data: dict, ml_prediction: dict) -> dict:
    """
    V4 Enterprise Underwriting Rule Engine: 
    Injects conservative banking logic to ensure trustworthiness.
    """
    age = applicant_data.get('age')
    credit_score = applicant_data.get('credit_score')
    income = applicant_data.get('annual_income')
    debt = applicant_data.get('total_debt', 0)
    savings = applicant_data.get('savings_balance', 0)
    loans = applicant_data.get('active_loans', 0)
    late = applicant_data.get('delayed_payments', 0)
    
    dti = debt / (income + 1)
    
    risk_level = ml_prediction['risk_level']
    approval_chance = ml_prediction['approval_chance']
    reasons = ml_prediction.get('risk_reasons', [])

    # Rule 1: High Debt Burden Penalty
    if dti > 0.65:
        risk_level = "High Risk"
        approval_chance = min(approval_chance, 10.0)
        reasons.append(f"Excessive Debt-to-Income ratio ({dti:.2f}). Limit is 0.65.")

    # Rule 2: Multi-loan Stressed Profile
    if loans >= 5:
        risk_level = "High Risk" if risk_level != "Fraud Suspected" else risk_level
        approval_chance = min(approval_chance, 15.0)
        reasons.append(f"High credit fragmentation: {loans} active loans detected.")

    # Rule 3: Serious Delinquency
    if late >= 3:
        risk_level = "High Risk"
        approval_chance = 0.0
        reasons.append(f"Recent delinquency: {late} delayed payments in history.")

    # Rule 4: Thin Savings Buffer
    if savings < 5000 and dti > 0.4:
        risk_level = "High Risk" if risk_level == "Low Risk" else risk_level
        approval_chance = min(approval_chance, 30.0)
        reasons.append("Insufficient liquid savings buffer for current debt levels.")

    # Rule 5: Prime Borrower fast-track
    if credit_score > 750 and dti < 0.2 and late == 0:
        risk_level = "Low Risk"
        approval_chance = max(approval_chance, 95.0)
        reasons.append("Prime credit profile: High score with low leverage.")

    # Rule 6: Fraud - Young/High Income Anomaly
    if age < 21 and income > 140000:
        risk_level = "Fraud Suspected"
        approval_chance = 0.0
        reasons.append("Fraud Alert: Income/Age anomaly requires physical verification.")

    # Final Recommendation
    recommendation = "Reject"
    if risk_level == "Low Risk": recommendation = "Strong Approve"
    elif risk_level == "Medium Risk": recommendation = "Conditional Approve (L3 Review)"
    elif risk_level == "Fraud Suspected": recommendation = "Block - Fraud Alert"

    return {
        "risk_level": risk_level,
        "approval_chance": approval_chance,
        "fraud_warning": risk_level == "Fraud Suspected",
        "confidence_score": ml_prediction['confidence_score'],
        "risk_reasons": list(set(reasons)),
        "recommendation": recommendation,
        "financial_ratios": {
            "DTI": round(dti, 3),
            "Savings_to_Debt": round(savings/(debt+1), 3)
        }
    }

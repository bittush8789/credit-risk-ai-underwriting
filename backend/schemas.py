from pydantic import BaseModel
from typing import List, Optional

class ApplicantData(BaseModel):
    """Input schema for credit underwriting inference."""
    age: int
    annual_income: float
    employment_years: int
    monthly_expenses: float
    savings_balance: float
    dependents: int
    loan_purpose: str
    residence_type: str
    credit_score: int
    loan_amount: float
    total_debt: float
    active_loans: int
    delayed_payments: int
    repayment_history_score: Optional[int] = 85

class UnderwritingResponse(BaseModel):
    """Output schema for underwriting decision analysis."""
    risk_level: str
    approval_chance: float
    confidence_score: float
    risk_reasons: List[str]
    recommendation: str
    financial_ratios: dict
    report_url: Optional[str] = None

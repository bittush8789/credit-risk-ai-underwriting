# ML Lifecycle

CreditRisk AI followed a structured data science lifecycle to ensure production reliability.

## 1. Problem Understanding
Defining the objective: Build a system that can predict the risk level of a loan applicant with high accuracy and explainable results.

## 2. Data Acquisition
Generated a synthetic dataset of 120,000 records to cover edge cases (extremely low income, high debt, perfect credit) that are often missing in small public datasets.

## 3. Exploratory Data Analysis (EDA)
Identified that `credit_score` and `debt_to_income` have the highest correlation with default risk.

## 4. Preprocessing & Feature Engineering
- Scaled numerical features using `StandardScaler`.
- Handled categorical data (Loan Purpose, Residence Type) using One-Hot Encoding.
- Created interaction features like `savings_to_loan_ratio`.

## 5. Model Selection & Training
- Evaluated Random Forest vs. XGBoost.
- XGBoost showed 3% better recall for "High Risk" cases.
- Trained using 5-Fold Cross-Validation.

## 6. Probability Calibration
Applied Platt Scaling to ensure the `predict_proba()` outputs are reliable for banking decisions.

## 7. Hybrid Deployment
Integrated the XGBoost model with a deterministic Rule Engine in a FastAPI backend.

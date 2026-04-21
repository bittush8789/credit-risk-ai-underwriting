# Data Dictionary

This document defines every variable used in the CreditRisk AI underwriting engine.

| Variable | Description | Impact on Risk |
| :--- | :--- | :--- |
| `age` | Age of the applicant | Generally, older applicants show more stability. |
| `annual_income` | Total gross yearly income | Primary measure of repayment capacity. |
| `employment_years` | Years with current employer | High value indicates lower default probability. |
| `credit_score` | Standard creditworthiness score (300-850) | Core historical behavior indicator. |
| `total_debt` | Sum of all existing liabilities | Increases DTI; high values are risky. |
| `loan_amount` | The amount being requested | Risk increases with the size of the request relative to income. |
| `savings_balance` | Cash reserves available | Acts as a safety net in case of income loss. |
| `active_loans` | Number of current open loan accounts | Too many accounts indicate credit hunger. |
| `delayed_payments` | Count of payments 30+ days late | Extremely strong predictor of future default. |
| `debt_to_income` | (Derived) Total Debt / Annual Income | Critical institutional risk metric. |
| `savings_to_debt` | (Derived) Savings / Total Debt | Measures borrower liquidity. |

# Model Explanation

## 🤖 Algorithm Selection: XGBoost
We selected the **XGBoost (eXtreme Gradient Boosting)** algorithm for this platform due to its superior performance with tabular financial data. 

### Why XGBoost?
- **Handling Imbalance**: Built-in parameters like `scale_pos_weight` help manage the naturally imbalanced nature of credit defaults.
- **Non-Linearity**: Effectively captures complex interactions between credit score, age, and debt ratios that linear models (like Logistic Regression) might miss.
- **Speed**: Optimized for fast inference, allowing real-time underwriting.

## 🛠️ Feature Engineering
The model's power comes from derived financial ratios:
- **Debt-to-Income (DTI)**: Total Debt / Annual Income. The most critical predictor of repayment capacity.
- **Savings-to-Loan Ratio**: Savings / Loan Amount. Indicates the "cushion" the borrower has.
- **Expense Ratio**: Monthly Expenses / Monthly Income. Captures the borrower's lifestyle overhead.

## 🎯 Model Calibration: Platt Scaling
Raw ML scores are often uncalibrated. We use **CalibratedClassifierCV** with Platt Scaling to ensure that the "Approval Chance" shown to the user is a true probability. If the system shows 90%, it means historically 9 out of 10 such applicants would be successful.

## 📉 Risk Classification Logic
- **Low Risk**: High probability of repayment, minimal flags.
- **Medium Risk**: Slight over-leverage or moderate credit history. Requires scrutiny.
- **High Risk**: Multiple delayed payments or excessive debt. Recommended rejection.
- **Fraud Risk**: Extreme anomalies detected by the rule engine (e.g., massive debt with zero income).

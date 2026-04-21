# Code Walkthrough: Key Functions

A line-by-line breakdown of critical system logic.

## 1. Model Loading (`model_loader.py`)

```python
def load_v4_engine(self):
    # Line 1: Use joblib to load the serialized XGBoost model artifact
    self.model = joblib.load(os.path.join(MODEL_DIR, "best_underwriting_model.pkl"))
    
    # Line 2: Load the fitted scaler to ensure features match training distribution
    self.scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
    
    # Line 3: Load metadata to ensure feature column ordering is identical
    self.meta = joblib.load(os.path.join(MODEL_DIR, "v4_meta.pkl"))
```

## 2. Underwriting Inference (`utils.py`)

```python
def predict_underwriting(data: dict):
    # Step 1: Calculate Debt-to-Income (DTI) ratio
    # Essential for measuring if a borrower is over-leveraged.
    data['debt_to_income'] = data['total_debt'] / (data['annual_income'] + 1)
    
    # Step 2: Transform raw data using the production scaler
    X_scaled = scaler.transform(X_raw)
    
    # Step 3: Compute class probabilities
    probs = model.predict_proba(X_scaled)[0]
    
    # Step 4: Apply the deterministic Rule Engine
    # Ensures ML scores don't violate institutional risk caps.
    final_res = apply_enterprise_underwriting_rules(data, ml_res)
    return final_res
```

## 3. Post-Inference Rules (`rule_engine.py`)

```python
def apply_enterprise_underwriting_rules(data, ml_res):
    # Rule: Hard Cap on DTI
    # If a borrower spends > 65% of income on debt, reject regardless of ML score.
    if data['debt_to_income'] > 0.65:
        ml_res['risk_level'] = "High Risk"
        ml_res['recommendation'] = "REJECTED (Excessive DTI)"
```

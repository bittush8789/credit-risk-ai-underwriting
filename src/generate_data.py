import pandas as pd
import numpy as np
import os

def generate_enterprise_data(samples=10000):
    """Generates synthetic credit risk data for training."""
    np.random.seed(42)
    
    data = {
        'age': np.random.randint(18, 75, samples),
        'annual_income': np.random.randint(20000, 200000, samples),
        'credit_score': np.random.randint(300, 850, samples),
        'loan_amount': np.random.randint(5000, 50000, samples),
        'current_debt': np.random.randint(0, 30000, samples),
        'active_loans': np.random.randint(0, 10, samples),
        'delayed_payments': np.random.randint(0, 5, samples),
        'employment_years': np.random.randint(0, 40, samples),
        'savings_balance': np.random.randint(0, 100000, samples),
    }
    
    df = pd.DataFrame(data)
    
    # Simple logic for risk class (target)
    # 0: Low, 1: Medium, 2: High, 3: Fraud Review
    df['dti'] = df['current_debt'] / (df['annual_income'] + 1)
    
    conditions = [
        (df['credit_score'] > 700) & (df['dti'] < 0.3),
        (df['credit_score'] > 600) & (df['dti'] < 0.5),
        (df['credit_score'] < 500) | (df['dti'] > 0.7),
    ]
    choices = [0, 1, 2]
    df['risk_class'] = np.select(conditions, choices, default=1)
    
    # Anomalies for Fraud
    fraud_mask = (df['annual_income'] < 25000) & (df['loan_amount'] > 45000)
    df.loc[fraud_mask, 'risk_class'] = 3
    
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/final_training_data.csv', index=False)
    print(f"Generated {samples} samples in data/final_training_data.csv")

if __name__ == "__main__":
    generate_enterprise_data()

import requests
import json

def test_single_prediction():
    url = "http://127.0.0.1:8000/predict"
    payload = {
        "age": 30,
        "annual_income": 75000,
        "employment_years": 5,
        "monthly_expenses": 2000,
        "savings_balance": 20000,
        "dependents": 0,
        "loan_purpose": "Home",
        "residence_type": "Owned",
        "credit_score": 720,
        "loan_amount": 15000,
        "total_debt": 5000,
        "active_loans": 1,
        "delayed_payments": 0
    }
    
    try:
        response = requests.post(url, json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    print("🚀 Starting API Integration Test...")
    test_single_prediction()

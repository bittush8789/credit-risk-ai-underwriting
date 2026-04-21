import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report
import json
import os

def evaluate_model():
    df = pd.read_csv('data/final_training_data.csv')
    X = df.drop(['risk_class', 'dti'], axis=1)
    y = df['risk_class']
    
    # Load model and scaler
    model = joblib.load('models/credit_risk_model.pkl')
    scaler = joblib.load('models/scaler.pkl')
    
    X_scaled = scaler.transform(X)
    y_pred = model.predict(X_scaled)
    
    acc = accuracy_score(y, y_pred)
    report = classification_report(y, y_pred, output_dict=True)
    
    metrics = {
        "accuracy": acc,
        "weighted_avg_precision": report['weighted avg']['precision']
    }
    
    os.makedirs('artifacts', exist_ok=True)
    with open('artifacts/metrics.json', 'w') as f:
        json.dump(metrics, f, indent=4)
    
    print(f"Evaluation complete. Accuracy: {acc}")

if __name__ == "__main__":
    evaluate_model()

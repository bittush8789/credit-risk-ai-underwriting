import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os

def train_model():
    df = pd.read_csv('data/final_training_data.csv')
    
    X = df.drop(['risk_class', 'dti'], axis=1)
    y = df['risk_class']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    model = XGBClassifier(n_estimators=100, max_depth=5, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/credit_risk_model.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    
    print("Model and Scaler saved to models/")

if __name__ == "__main__":
    train_model()

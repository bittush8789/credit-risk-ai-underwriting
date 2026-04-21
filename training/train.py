import pandas as pd
import xgboost as xgb
import mlflow
import mlflow.sklearn
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_enterprise_model(data_path, experiment_name="CreditRisk_Underwriting"):
    mlflow.set_experiment(experiment_name)
    
    df = pd.read_csv(data_path)
    X = df.drop('risk_class', axis=1)
    y = df['risk_class']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    with mlflow.start_run():
        params = {
            "n_estimators": 100,
            "max_depth": 6,
            "learning_rate": 0.1,
            "objective": "multi:softprob",
            "num_class": 4
        }
        
        model = xgb.XGBClassifier(**params)
        model.fit(X_train, y_train)
        
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        
        # Log to MLflow
        mlflow.log_params(params)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "credit_risk_model")
        
        # Save locally
        os.makedirs("models", exist_ok=True)
        joblib.dump(model, "models/credit_risk_model.pkl")
        
        print(f"Run completed. Accuracy: {acc}")

if __name__ == "__main__":
    train_enterprise_model("data/final_training_data.csv")

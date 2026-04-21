# System Architecture

The Advanced Credit Underwriting Platform follows a decoupled client-server architecture designed for scalability and maintainability.

## 1. Data Pipeline
The system utilizes a 120,000-row synthetic dataset generated to simulate complex risk profiles, including over-leveraged applicants, fraudulent behavior, and stable prime borrowers.

## 2. Machine Learning Layer
- **Model**: XGBoost Classifier.
- **Scaling**: Standard Scaler for numerical features.
- **Calibration**: CalibratedClassifierCV ensures that "90% approval chance" actually corresponds to a 90% probability in real-world scenarios.

## 3. Underwriting Rule Engine (Hybrid AI)
To prevent "unrealistic approvals" (e.g., approving a 19-year-old with $0 income), the system applies a post-ML rule layer:
- **DTI Cap**: Strict rejection if Debt-to-Income exceeds 65%.
- **Liquidity Check**: Penalizes applicants with high debt and low savings.
- **Hard Rejection**: Automated rejection for excessive active loans or recent delayed payments.

## 4. Backend Service
Built with **FastAPI**, the backend provides:
- High-speed async inference.
- Automatic PDF report generation using FPDF.
- Pydantic data validation for all incoming applications.

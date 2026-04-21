# Testing Guide

Testing credit risk systems requires both statistical and logic-based verification.

## 1. Single Applicant Inference
Use the UI (`predict.html`) or Postman to send a single JSON payload to `/predict`.
- **Expected Outcome**: A JSON response with a risk level and a valid `report_url`.

## 2. Rule Engine Verification (Edge Cases)
The rule engine should be tested for "Knock-out" scenarios:
- **DTI Over-limit**: Input an applicant with $10k income and $8k debt.
- **Expected Outcome**: Immediate "High Risk" / "Rejected" decision regardless of credit score.

## 3. Bulk Data Testing
Use the `data/sample_bulk_upload.csv` to verify the system handles diverse profiles in sequence. (Feature available via script or planned batch API).

## 4. Stability Testing
Run the backend and check the `/health` endpoint while performing multiple predictions. Verify memory usage remains stable (singleton model loader prevents leaks).

## 5. Security Testing
- **Input Sanitization**: Pass string data into numeric fields (e.g., `"age": "invalid"`).
- **Expected Outcome**: Pydantic should return a `422 Unprocessable Entity` error, preventing backend crashes.

# Docker Implementation Guide

## 1. Why Docker?
In Banking AI, consistency is critical. Docker ensures that the same OS libraries and Python dependencies used during model training are present during production inference.

## 2. Dockerizing the Backend
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 3. Build & Run
```bash
docker build -t credit-risk-backend:v1 .
docker run -p 8000:8000 credit-risk-backend:v1
```

## 4. Verification
```bash
curl http://localhost:8000/health
```

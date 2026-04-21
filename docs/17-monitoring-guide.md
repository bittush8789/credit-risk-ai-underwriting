# Monitoring & Observability Guide

## 1. Stack Components
- **Prometheus**: Scrapes metrics from the FastAPI backend and KServe pods.
- **Grafana**: Visualizes approval rates, latency, and system health.
- **Loki**: Centralized log management for auditing prediction requests.

## 2. Key Metrics for Banking AI
- **Model Drift Score**: Measures changes in input data distribution.
- **Request Latency (P99)**: Ensures decisions are fast enough for real-time mobile apps.
- **Approval/Rejection Ratio**: Detects potential bias or model logic failures.

## 3. Alerting
Alertmanager is configured to notify the MLOps Slack channel if the `High Risk` prediction volume spikes by > 50% in one hour.

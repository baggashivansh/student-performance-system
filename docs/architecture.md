# System Architecture

## Overview

The Student Performance Analytics System is designed to analyze academic performance data and identify at-risk students using interactive dashboards and predictive analytics.

---

## Technologies Used

- FastAPI
- SQLite
- Streamlit
- Plotly
- Pandas
- Scikit Learn
- SQLAlchemy

---

## Architecture Flow

CSV Dataset
↓
Data Cleaning
↓
SQLite Database
↓
FastAPI Backend APIs
↓
Streamlit Dashboard
↓
ML Risk Prediction

---

## Backend Components

### Database Layer
Stores:
- students
- performance
- risk_predictions

### API Layer
Provides:
- CRUD APIs
- analytics APIs
- risk prediction APIs

### ML Layer
Uses RandomForestClassifier for student risk prediction.

### Dashboard Layer
Provides:
- charts
- filters
- analytics
- risk visualization
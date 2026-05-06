from fastapi import FastAPI
from backend.database import engine
from backend.models import Base
from backend.schemas import StudentInput

import joblib
import numpy as np

# =========================
# FASTAPI APP
# =========================

app = FastAPI(
    title="Student Performance Prediction API",
    version="1.0"
)

# =========================
# CREATE DATABASE TABLES
# =========================

Base.metadata.create_all(bind=engine)

# =========================
# LOAD ML MODEL
# =========================

model = joblib.load("ml/model.pkl")

# =========================
# HOME ROUTE
# =========================

@app.get("/")
def home():
    return {
        "message": "Student Performance Prediction API Running"
    }

# =========================
# PREDICTION ROUTE
# =========================

@app.post("/predict")
def predict(data: StudentInput):

    features = np.array([[
        data.attendance,
        data.marks,
        data.gpa
    ]])

    prediction = model.predict(features)[0]

    return {
        "prediction": str(prediction)
    }
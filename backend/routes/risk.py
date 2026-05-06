from fastapi import APIRouter
from pydantic import BaseModel

import pandas as pd
import joblib

router = APIRouter()

# =========================
# LOAD MODEL
# =========================

model = joblib.load("../ml/model.pkl")

# =========================
# REQUEST MODEL
# =========================

class RiskInput(BaseModel):
    attendance: float
    marks: float
    gpa: float


# =========================
# PREDICT ROUTE
# =========================

@router.post("/risk/predict")
def predict_risk(data: RiskInput):

    input_data = pd.DataFrame({
        "attendance": [data.attendance],
        "marks": [data.marks],
        "gpa": [data.gpa]
    })

    prediction = model.predict(input_data)

    return {
        "predicted_risk": prediction[0]
    }
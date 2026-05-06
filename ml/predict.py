import joblib
import pandas as pd

# =========================
# LOAD MODEL
# =========================

model = joblib.load("ml/student_risk_model.pkl")

# =========================
# SAMPLE INPUT
# =========================

sample_data = pd.DataFrame({
    "attendance": [65],
    "marks": [58],
    "gpa": [5.8]
})

# =========================
# PREDICTION
# =========================

prediction = model.predict(sample_data)

print("Predicted Risk:", prediction[0])
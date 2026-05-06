import pandas as pd
from sqlalchemy import create_engine

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import joblib

# =========================
# DATABASE CONNECTION
# =========================

engine = create_engine("sqlite:///../backend/students.db")

# =========================
# LOAD DATA
# =========================

query = """
SELECT
    attendance,
    marks,
    gpa
FROM performance
"""

df = pd.read_sql(query, engine)

# =========================
# CREATE RISK LABELS
# =========================

def create_risk(row):

    if row["gpa"] < 6 or row["attendance"] < 70:
        return "High Risk"

    elif row["gpa"] < 7.5:
        return "Medium Risk"

    else:
        return "Low Risk"


df["risk_level"] = df.apply(
    create_risk,
    axis=1
)

# =========================
# FEATURES & TARGET
# =========================

X = df[
    [
        "attendance",
        "marks",
        "gpa"
    ]
]

y = df["risk_level"]

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# MODEL
# =========================

model = RandomForestClassifier()

model.fit(X_train, y_train)

# =========================
# EVALUATION
# =========================

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"Model Accuracy: {accuracy}")

# =========================
# SAVE MODEL
# =========================

joblib.dump(
    model,
    "model.pkl"
)

print("Model Saved Successfully")
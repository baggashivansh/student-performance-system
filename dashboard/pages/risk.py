import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# =========================
# DATABASE CONNECTION
# =========================

engine = create_engine("sqlite:///../backend/students.db")

# =========================
# LOAD DATA
# =========================

query = """
SELECT
    s.name,
    s.department,
    p.attendance,
    p.gpa,
    p.marks
FROM students s
JOIN performance p
ON s.id = p.student_id
"""

df = pd.read_sql(query, engine)

# =========================
# RISK LOGIC
# =========================

def calculate_risk(row):

    if row["gpa"] < 6 or row["attendance"] < 70:
        return "High Risk"

    elif row["gpa"] < 7.5:
        return "Medium Risk"

    else:
        return "Low Risk"


df["risk_level"] = df.apply(
    calculate_risk,
    axis=1
)

# =========================
# PAGE TITLE
# =========================

st.title("Risk Analytics Dashboard")

# =========================
# RISK COUNTS
# =========================

risk_counts = df["risk_level"].value_counts()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Low Risk",
    risk_counts.get("Low Risk", 0)
)

col2.metric(
    "Medium Risk",
    risk_counts.get("Medium Risk", 0)
)

col3.metric(
    "High Risk",
    risk_counts.get("High Risk", 0)
)

# =========================
# PIE CHART
# =========================

st.subheader("Risk Distribution")

pie_fig = px.pie(
    names=risk_counts.index,
    values=risk_counts.values,
    title="Student Risk Distribution"
)

st.plotly_chart(
    pie_fig,
    use_container_width=True
)

# =========================
# RISK TABLE
# =========================

st.subheader("Student Risk Details")

st.dataframe(df[
    [
        "name",
        "department",
        "attendance",
        "gpa",
        "risk_level"
    ]
])
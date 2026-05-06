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
    s.semester,
    p.subject,
    p.marks,
    p.attendance,
    p.gpa
FROM students s
JOIN performance p
ON s.id = p.student_id
"""

df = pd.read_sql(query, engine)

# =========================
# PAGE TITLE
# =========================

st.title("Overview Dashboard")

# =========================
# METRICS
# =========================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Students",
    df["name"].nunique()
)

col2.metric(
    "Average GPA",
    round(df["gpa"].mean(), 2)
)

col3.metric(
    "Average Attendance",
    round(df["attendance"].mean(), 2)
)

# =========================
# GPA DISTRIBUTION
# =========================

st.subheader("GPA Distribution")

fig = px.histogram(
    df,
    x="gpa",
    nbins=10,
    title="GPA Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# ATTENDANCE VS MARKS
# =========================

st.subheader("Attendance vs Marks")

scatter_fig = px.scatter(
    df,
    x="attendance",
    y="marks",
    color="department",
    hover_data=["name"],
    title="Attendance vs Marks Correlation"
)

st.plotly_chart(
    scatter_fig,
    use_container_width=True
)
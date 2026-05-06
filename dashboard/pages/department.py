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
    s.department,
    s.semester,
    p.gpa,
    p.marks
FROM students s
JOIN performance p
ON s.id = p.student_id
"""

df = pd.read_sql(query, engine)

# =========================
# PAGE TITLE
# =========================

st.title("Department Analytics")

# =========================
# FILTERS
# =========================

department_filter = st.sidebar.selectbox(
    "Select Department",
    ["All"] + list(df["department"].unique())
)

if department_filter != "All":
    df = df[df["department"] == department_filter]

# =========================
# DEPARTMENT GPA CHART
# =========================

st.subheader("Department Average GPA")

dept_gpa = df.groupby(
    "department"
)["gpa"].mean().reset_index()

fig = px.bar(
    dept_gpa,
    x="department",
    y="gpa",
    title="Department GPA Comparison"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# SEMESTER PERFORMANCE
# =========================

st.subheader("Semester Performance Trend")

semester_fig = px.line(
    df,
    x="semester",
    y="marks",
    color="department",
    markers=True,
    title="Semester Performance Trend"
)

st.plotly_chart(
    semester_fig,
    use_container_width=True
)
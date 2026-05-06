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

st.title("Subject Analytics")

# =========================
# SUBJECT FILTER
# =========================

subject_filter = st.sidebar.selectbox(
    "Select Subject",
    ["All"] + list(df["subject"].unique())
)

if subject_filter != "All":
    df = df[df["subject"] == subject_filter]

# =========================
# SUBJECT MARKS CHART
# =========================

st.subheader("Subject Wise Marks")

marks_fig = px.bar(
    df,
    x="subject",
    y="marks",
    color="department",
    title="Subject Performance"
)

st.plotly_chart(
    marks_fig,
    use_container_width=True
)

# =========================
# ATTENDANCE CORRELATION
# =========================

st.subheader("Attendance vs GPA")

scatter_fig = px.scatter(
    df,
    x="attendance",
    y="gpa",
    color="subject",
    hover_data=["name"],
    title="Attendance vs GPA"
)

st.plotly_chart(
    scatter_fig,
    use_container_width=True
)

# =========================
# HEATMAP
# =========================

st.subheader("Department vs Subject Heatmap")

heatmap_data = df.pivot_table(
    values="marks",
    index="department",
    columns="subject",
    aggfunc="mean"
)

heatmap_fig = px.imshow(
    heatmap_data,
    text_auto=True,
    title="Department Subject Performance Heatmap"
)

st.plotly_chart(
    heatmap_fig,
    use_container_width=True
)
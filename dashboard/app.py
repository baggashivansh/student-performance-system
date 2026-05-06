import streamlit as st

st.set_page_config(
    page_title="Student Performance Dashboard",
    layout="wide"
)

st.title("Student Performance Analytics System")

st.markdown("""
Welcome to the Student Performance Analytics Dashboard.

Use the sidebar to navigate between pages.
""")

st.sidebar.success("Select a page above")
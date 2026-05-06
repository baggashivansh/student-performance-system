# User Guide

## Running Backend

Go to backend folder:

```bash
python3 -m uvicorn main:app --reload
```

Backend URL:

http://127.0.0.1:8000/docs

---

## Running Dashboard

Go to dashboard folder:

```bash
python3 -m streamlit run app.py
```

Dashboard URL:

http://localhost:8501

---

## Features

- Student CRUD operations
- Academic analytics
- Department analytics
- Subject analytics
- Risk prediction
- Interactive visualizations
- Filtering system

---

## Filters

Available filters:
- Department
- Subject
- Semester

---

## Risk Prediction

Users can predict risk level based on:
- attendance
- marks
- GPA
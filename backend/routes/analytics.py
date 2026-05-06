from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import SessionLocal
import models

router = APIRouter()


# =========================
# DATABASE SESSION
# =========================

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# =========================
# OVERVIEW ANALYTICS
# =========================

@router.get("/analytics/overview")
def overview_analytics(
    db: Session = Depends(get_db)
):

    total_students = db.query(
        models.Student
    ).count()

    avg_gpa = db.query(
        func.avg(models.Performance.gpa)
    ).scalar()

    avg_attendance = db.query(
        func.avg(models.Performance.attendance)
    ).scalar()

    return {
        "total_students": total_students,
        "average_gpa": round(avg_gpa, 2),
        "average_attendance": round(avg_attendance, 2)
    }


# =========================
# DEPARTMENT ANALYTICS
# =========================

@router.get("/analytics/department")
def department_analytics(
    db: Session = Depends(get_db)
):

    data = db.query(
        models.Student.department,
        func.avg(models.Performance.gpa)
    ).join(
        models.Performance,
        models.Student.id == models.Performance.student_id
    ).group_by(
        models.Student.department
    ).all()

    return data


# =========================
# SUBJECT ANALYTICS
# =========================

@router.get("/analytics/subjects")
def subject_analytics(
    db: Session = Depends(get_db)
):

    data = db.query(
        models.Performance.subject,
        func.avg(models.Performance.marks)
    ).group_by(
        models.Performance.subject
    ).all()

    return data
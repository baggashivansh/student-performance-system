from sqlalchemy.orm import Session

import models
import schemas


# =========================
# STUDENT CRUD
# =========================

def get_students(db: Session):
    return db.query(models.Student).all()


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()


def create_student(
    db: Session,
    student: schemas.StudentCreate
):
    db_student = models.Student(
        name=student.name,
        gender=student.gender,
        department=student.department,
        semester=student.semester
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def update_student(
    db: Session,
    student_id: int,
    updated_student: schemas.StudentCreate
):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if student:
        student.name = updated_student.name
        student.gender = updated_student.gender
        student.department = updated_student.department
        student.semester = updated_student.semester

        db.commit()
        db.refresh(student)

    return student


def delete_student(db: Session, student_id: int):

    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if student:
        db.delete(student)
        db.commit()

    return student


# =========================
# PERFORMANCE CRUD
# =========================

def create_performance(
    db: Session,
    performance: schemas.PerformanceCreate
):
    db_performance = models.Performance(
        student_id=performance.student_id,
        subject=performance.subject,
        marks=performance.marks,
        attendance=performance.attendance,
        gpa=performance.gpa
    )

    db.add(db_performance)
    db.commit()
    db.refresh(db_performance)

    return db_performance


def get_all_performance(db: Session):
    return db.query(models.Performance).all()
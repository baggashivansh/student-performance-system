from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import schemas

from database import SessionLocal

router = APIRouter()


# =========================
# DATABASE CONNECTION
# =========================

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# =========================
# STUDENT ROUTES
# =========================

@router.get("/students")
def read_students(
    db: Session = Depends(get_db)
):
    return crud.get_students(db)


@router.get("/students/{student_id}")
def read_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_student(db, student_id)


@router.post("/students")
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_student(db, student)


@router.put("/students/{student_id}")
def update_student(
    student_id: int,
    updated_student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    return crud.update_student(
        db,
        student_id,
        updated_student
    )


@router.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_student(db, student_id)
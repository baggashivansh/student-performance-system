from database import SessionLocal
from models import Student, Performance

db = SessionLocal()

# =========================
# SAMPLE STUDENTS
# =========================

students = [
    Student(
        name="Aman",
        gender="Male",
        department="CSE",
        semester=5
    ),

    Student(
        name="Priya",
        gender="Female",
        department="IT",
        semester=4
    ),

    Student(
        name="Rahul",
        gender="Male",
        department="ECE",
        semester=6
    )
]

db.add_all(students)
db.commit()

# =========================
# SAMPLE PERFORMANCE
# =========================

performance_data = [

    Performance(
        student_id=1,
        subject="DBMS",
        marks=85,
        attendance=90,
        gpa=8.5
    ),

    Performance(
        student_id=2,
        subject="Python",
        marks=78,
        attendance=80,
        gpa=7.8
    ),

    Performance(
        student_id=3,
        subject="Networks",
        marks=60,
        attendance=65,
        gpa=6.2
    )
]

db.add_all(performance_data)
db.commit()

print("Sample Data Inserted Successfully")
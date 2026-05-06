from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from backend.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    gender = Column(String)
    department = Column(String)
    semester = Column(Integer)

    performances = relationship(
        "Performance",
        back_populates="student"
    )


class Performance(Base):
    __tablename__ = "performance"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id")
    )

    subject = Column(String)
    marks = Column(Float)
    attendance = Column(Float)
    gpa = Column(Float)

    student = relationship(
        "Student",
        back_populates="performances"
    )


class RiskPrediction(Base):
    __tablename__ = "risk_predictions"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(Integer)
    risk_level = Column(String)
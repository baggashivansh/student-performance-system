from pydantic import BaseModel


# =========================
# STUDENT SCHEMAS
# =========================

class StudentBase(BaseModel):
    name: str
    gender: str
    department: str
    semester: int


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True


# =========================
# PERFORMANCE SCHEMAS
# =========================

class PerformanceBase(BaseModel):
    student_id: int
    subject: str
    marks: float
    attendance: float
    gpa: float


class PerformanceCreate(PerformanceBase):
    pass


class Performance(PerformanceBase):
    id: int

    class Config:
        from_attributes = True


# =========================
# RISK SCHEMAS
# =========================

class RiskPredictionBase(BaseModel):
    student_id: int
    risk_level: str


class RiskPredictionCreate(RiskPredictionBase):
    pass


class RiskPrediction(RiskPredictionBase):
    id: int

    class Config:
        from_attributes = True


# =========================
# ML PREDICTION INPUT
# =========================

class StudentInput(BaseModel):
    attendance: float
    marks: float
    gpa: float
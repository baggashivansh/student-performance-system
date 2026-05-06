# API Documentation

## Student APIs

### GET /students
Returns all students.

### GET /students/{id}
Returns a specific student.

### POST /students
Creates a new student.

### PUT /students/{id}
Updates student details.

### DELETE /students/{id}
Deletes student.

---

## Analytics APIs

### GET /analytics/overview
Returns:
- total students
- average GPA
- average attendance

### GET /analytics/department
Returns department-wise GPA analytics.

### GET /analytics/subjects
Returns subject-wise marks analytics.

---

## Risk Prediction API

### POST /risk/predict

Input:

```json
{
  "attendance": 70,
  "marks": 60,
  "gpa": 6.5
}
```

Output:

```json
{
  "predicted_risk": "Medium Risk"
}
```
import pandas as pd

# =========================
# LOAD RAW DATA
# =========================

df = pd.read_csv("raw/student_data.csv")

# =========================
# REMOVE DUPLICATES
# =========================

df.drop_duplicates(inplace=True)

# =========================
# HANDLE MISSING VALUES
# =========================

df.fillna({
    "marks": 0,
    "attendance": 0,
    "gpa": 0
}, inplace=True)

# =========================
# STANDARDIZE DEPARTMENTS
# =========================

df["department"] = df["department"].str.upper()

# =========================
# REMOVE INVALID MARKS
# =========================

df = df[
    (df["marks"] >= 0) &
    (df["marks"] <= 100)
]

# =========================
# SAVE CLEAN DATA
# =========================

df.to_csv(
    "processed/clean_data.csv",
    index=False
)

print("Data Cleaned Successfully")
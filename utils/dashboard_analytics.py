import matplotlib.pyplot as plt

categories = [
    "High Attendance",
    "Low Attendance",
    "High GPA",
    "At Risk"
]

values = [120, 35, 90, 18]

plt.figure(figsize=(10,6))

bars = plt.bar(categories, values)

plt.title("Student Performance Dashboard Analytics")
plt.xlabel("Analytics Categories")
plt.ylabel("Number of Students")

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + 0.2, yval + 1, yval)

plt.tight_layout()
plt.show()
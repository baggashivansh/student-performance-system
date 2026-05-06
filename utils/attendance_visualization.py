import matplotlib.pyplot as plt

students = ["Aman", "Riya", "Kunal", "Sneha", "Rahul"]
attendance = [92, 85, 78, 96, 88]

plt.figure(figsize=(10,6))
bars = plt.bar(students, attendance)

plt.title("Student Attendance Analysis")
plt.xlabel("Students")
plt.ylabel("Attendance Percentage")
plt.ylim(0, 100)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + 0.25, yval + 1, yval)

plt.tight_layout()
plt.show()
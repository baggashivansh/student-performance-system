import matplotlib.pyplot as plt

semesters = ["Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5"]
gpa = [7.2, 7.8, 8.1, 8.5, 8.9]

plt.figure(figsize=(10,6))

plt.plot(semesters, gpa, marker='o')

plt.title("Student GPA Progression")
plt.xlabel("Semester")
plt.ylabel("GPA")
plt.ylim(0, 10)

for i, value in enumerate(gpa):
    plt.text(i, value + 0.1, str(value))

plt.tight_layout()
plt.show()
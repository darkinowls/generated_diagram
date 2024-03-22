import matplotlib.pyplot as plt

# Назви студентів
students = ['Студент 1', 'Студент 2', 'Студент 3', 'Студент 4', 'Студент 5', 'Студент 6', 'Студент 7', 'Студент 8']

# Успішність кожного студента
grades = [80, 85, 70, 75, 90, 95, 65, 60]

plt.figure(figsize=(10, 6))
plt.bar(students, grades, color='skyblue')
plt.title('Успішність студентів у серпні')
plt.xlabel('Студент')
plt.ylabel('Успішність')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Позначення двох студентів, які обігнали інших
top_students = [4, 5]
for i in top_students:
    plt.annotate('Степендіат', xy=(i, grades[i]), xytext=(i, grades[i] + 5),
                 ha='center', arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()
plt.savefig('d12.png')
plt.show()



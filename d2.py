import matplotlib.pyplot as plt

# Дані про зарплати співробітників (припустимо, що це випадкові дані)
salaries = [12000, 13000, 14000, 11000, 12500, 11500, 13500, 12500, 14500, 12000, 11000, 13000, 11500, 14000, 13000, 11000, 12500, 13500, 14000, 12000]

plt.figure(figsize=(8, 6))
plt.hist(salaries, bins=5, color='skyblue', edgecolor='black')
plt.title('Розподіл зарплат співробітників')
plt.xlabel('Зарплата, грн')
plt.ylabel('Частота')
plt.grid(True)
plt.tight_layout()
plt.savefig('d2.png')
plt.show()



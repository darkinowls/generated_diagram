import matplotlib.pyplot as plt

# Доходи і зарплата працівників
incomes = [30000, 40000, 50000, 60000, 70000, 80000, 90000]
salaries = [20000, 25000, 30000, 35000, 40000, 45000, 50000]

plt.figure(figsize=(8, 6))
plt.scatter(incomes, salaries, color='blue')
plt.title("Зв'язок між доходами і зарплатою")
plt.xlabel("Доходи, грн")
plt.ylabel("Зарплата, грн")
plt.grid(True)
plt.tight_layout()

plt.savefig('d11.png')
plt.show()



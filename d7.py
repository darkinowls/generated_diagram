import matplotlib.pyplot as plt

# Вікові групи
age_groups = ['18-25', '25-30', '30-35', '35-40', '40-45']

# Рівень плинності кадрів у торік
turnover_last_year = [8, 10, 15, 12, 9]  # Припустимо, що рівень плинності кадрів - відсотки

plt.figure(figsize=(8, 6))
plt.bar(age_groups, turnover_last_year, color='lightgreen')
plt.title('Плинність кадрів у торік за віковими групами')
plt.xlabel('Вікова група')
plt.ylabel('Рівень плинності кадрів, %')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('d7.png')
plt.show()



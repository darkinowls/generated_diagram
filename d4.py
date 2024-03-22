import matplotlib.pyplot as plt

# Назви підрозділів
departments = ['Підрозділ 1', 'Підрозділ 2', 'Підрозділ 3', 'Підрозділ 4', 'Підрозділ 5', 'Підрозділ 6']

# Рівень плинності кадрів у вересні
turnover_rate = [15, 18, 16, 17, 16, 15]  # Приблизно однаковий

plt.figure(figsize=(10, 6))
plt.bar(departments, turnover_rate, color='skyblue')
plt.title('Рівень плинності кадрів у вересні')
plt.xlabel('Підрозділ')
plt.ylabel('Рівень плинності кадрів')
plt.ylim(0, max(turnover_rate) + 2)  # Додамо додатковий простір над стовпчиками
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('d4.png')
plt.show()



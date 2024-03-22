import matplotlib.pyplot as plt

# Роки
years = list(range(2021, 2031))

# Прибутковість акцій у початковому стані
initial_profitability = 100  # Припустимо, що прибутковість акцій починалася з 100%

# Зменшення прибутковості акцій на 10% щороку
profitability = [initial_profitability]
for year in range(2022, 2031):
    initial_profitability -= initial_profitability * 0.1  # Зменшення на 10%
    profitability.append(initial_profitability)

plt.figure(figsize=(10, 6))
plt.plot(years, profitability, marker='o', linestyle='-')
plt.title('Зміна прибутковості акцій компанії')
plt.xlabel('Рік')
plt.ylabel('Прибутковість акцій')
plt.grid(True)
plt.xticks(years)
plt.tight_layout()
plt.savefig('d9.png')
plt.show()



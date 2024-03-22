import matplotlib.pyplot as plt

# Роки
years = list(range(2025, 2035))

# Прогнозована кількість навчальних закладів для кожного року
school_counts = [1000, 960, 940, 870, 860, 750, 700, 670, 630, 600]

plt.figure(figsize=(10, 6))
plt.plot(years, school_counts, marker='o', linestyle='-')
plt.title('Прогноз зменшення кількості навчальних закладів наступних 10 років')
plt.xlabel('Рік')
plt.ylabel('Кількість навчальних закладів')
plt.grid(True)
plt.xticks(years)
plt.tight_layout()
plt.savefig('d1.png')
plt.show()



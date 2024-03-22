import matplotlib.pyplot as plt

# Назви регіонів
regions = ['Західний', 'Північний', 'Східний', 'Південний', 'Центральний']

# Частки народжуваності у різних регіонах (припустимо, що сума часток - 100%)
birth_rates = [20, 15, 25, 30, 10]

plt.figure(figsize=(8, 8))
plt.pie(birth_rates, labels=regions, autopct='%1.1f%%', startangle=140)
plt.title('Частки народжуваності у різних регіонах')
plt.axis('equal')  # Забезпечимо колоїдність кругової діаграми
plt.tight_layout()
plt.savefig('d8.png')
plt.show()



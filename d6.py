import matplotlib.pyplot as plt

# Категорії трудового стажу
tenure_categories = ['До 1 року', '1-3 роки', '3-5 років', '5-10 років', '10 і більше років']

# Розмір надбавки до заплати (припустимо, що розмір надбавки є однаковим для всіх категорій трудового стажу)
bonus = 1000

# Створення списку розмірів надбавок, що відповідають кожній категорії трудового стажу
bonus_list = [bonus] * len(tenure_categories)

plt.figure(figsize=(8, 6))
plt.bar(tenure_categories, bonus_list, color='skyblue')
plt.title('Розмір надбавки до заплати за категоріями трудового стажу')
plt.xlabel('Категорія трудового стажу')
plt.ylabel('Розмір надбавки, грн')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('d6.png')
plt.show()



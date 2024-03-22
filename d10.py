import matplotlib.pyplot as plt

# Назви галузей
sectors = ['Виробництво', 'Торгівля', 'Фінанси', 'Транспорт', 'Інші']

# Частки фондів у різних галузях (припустимо, що сума часток - 100%)
fund_shares = [40, 20, 15, 10, 15]

plt.figure(figsize=(8, 8))
plt.pie(fund_shares, labels=sectors, autopct='%1.1f%%', startangle=140)
plt.title('Частка фондів, задіяна у виробництві та інших галузях')
plt.axis('equal')  # Забезпечимо колоїдність кругової діаграми
plt.tight_layout()

plt.savefig('d10.png')
plt.show()



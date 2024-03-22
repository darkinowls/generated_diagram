import matplotlib.pyplot as plt

# Сорти бензину
time = [2020, 2021, 2022, 2023]
# Ціни на бензин
prices = [50, 65, 70, 75]
# Якість бензину (від 1 до 10, де 10 - найвища якість)
quality = [8, 8, 7, 6]

plt.figure(figsize=(10, 5))

# Побудова графіків
plt.subplot(1, 2, 1)
plt.plot(time, prices, marker='o', linestyle='-', color='b')
plt.title('Ціни на бензин')
plt.xlabel('Рік')
plt.ylabel('Ціна, грн')

plt.subplot(1, 2, 2)
plt.plot(time, quality, marker='o', linestyle='-', color='r')
plt.title('Якість бензину')
plt.xlabel('Рік')
plt.ylabel('Якість')

plt.tight_layout()
plt.savefig('d3.png')
plt.show()



import matplotlib.pyplot as plt

# Данные для простого графика
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Построение графика
plt.plot(x, y, label='Квадрат чисел')

# Добавление заголовка и подписей осей
plt.title('Пример графика')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# Отображение легенды
plt.legend()

# Показать график
print('смотрим первый график')
plt.show()

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
print('смотрим второй график')
plt.show()                           # Show the figure.
###############
###############
###############
print('смотрим третий график')
import numpy as np
# import matplotlib.pyplot as plt

# Создаем данные для оси X (углы от 0 до 20π)
theta = np.linspace(0, 20 * np.pi, 1000)

# Радиус в зависимости от угла theta (уменьшаем амплитуду, чтобы получилась спираль)
r = np.linspace(0, 5, 1000)

# Вычисляем X и Y координаты для спирали синусоиды
x = r * np.cos(theta)
y = r * np.sin(theta)

# Цвет синусоиды будет зависеть от угла
colors = theta

# Создаем график
plt.figure(figsize=(6, 6))  # Устанавливаем квадратное окно

plt.scatter(x, y, c=colors, cmap='hsv', s=1)  # Рисуем точки с градиентом цвета

# Добавляем заголовок
plt.title("Спираль синусоиды с цветовым градиентом", fontsize=16)

# Настройки осей
plt.axis('equal')  # Ось X и Y имеют одинаковый масштаб
plt.grid(True)  # Включаем сетку

# Отображаем график
plt.show()


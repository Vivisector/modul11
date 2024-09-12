import numpy as np

random_numbers = np.random.rand(5)  # Массив из 5 случайных чисел от 0 до 1
print(random_numbers)

random_integers = np.random.randint(1, 10, (5, 5))
print(random_integers)

# Создание одномерного массива
a = np.array([1, 2, 3, 4, 5])
print(a)

# Создание двумерного массива
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# Выполнение операций с массивами
print(a + 5)  # Добавить 5 ко всем элементам
print('----- SRC -----')
print(b)
print('----- SQ -----')
print(b ** 2)  # возвести все элементы в квадрат

b3 = np.array([[[1, 2], [4, 5]], [[1, 2], [4, 5]]])
print('-------------')
print(b3)

b4 = np.array([[[[1, 2], [4, 5]], [[1, 2], [4, 5]]], [[[1, 2], [4, 5]], [[1, 2], [4, 5]]]])
print('------4x-------')
print(b4)

# b44 = np.array([[[1, 2], [4, 5]], [[1, 2], [4, 5]], [[1, 2], [4, 5]], [[1, 2], [4, 5]]])
b444 = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]])

print('------444x-------')
print(b444)
print(b444.ndim)
print(b444.shape)  # Форма массива
print('------flattened-------')
print(b444.flatten())
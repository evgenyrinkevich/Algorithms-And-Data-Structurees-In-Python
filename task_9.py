# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint

matrix = [[randint(1, 100) for i in range(10)] for j in range(12)]  # создаем матрицу
min_el = matrix[0]  # элементы 1го ряда назначаем минимальными
for row in matrix:
    min_el = map(lambda x, y: min(x, y), min_el, row)  # сравниваем элементы каждого ряда с min_el
    # если меньше - заносим в min_el

print(f'{max(min_el)} - максимальный элемент среди минимальных элементов столбцов матрицы')

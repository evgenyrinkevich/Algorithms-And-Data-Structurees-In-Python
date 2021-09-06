# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

ROWS = 4
COLUMNS = 5
matrix = []
try:
    for i in range(ROWS):
        temp = []
        print(f'Для {i + 1} строки:')
        for j in range(COLUMNS - 1):
            el = int(input(f'Введите {j + 1} элемент: '))
            temp.append(el)
        temp.append(sum(temp))  # в последней ячейку сумма предыдущих
        matrix.append(temp)  # добавляем строку в матрицу
    print('Полученная матрица:')
    for row in matrix:
        print(row)
except ValueError:
    print('Неверные данные')

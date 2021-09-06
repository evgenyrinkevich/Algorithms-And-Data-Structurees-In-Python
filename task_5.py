# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

array = [1, 2, 4, 1, -3, 0, -1]
max_neg_el = None
for i, val in enumerate(sorted(array, reverse=True)):
    if val < 0:
        max_neg_el = val
        break
if max_neg_el:
    print(f'максимальный отрицательный элемент {max_neg_el} на {array.index(max_neg_el) + 1} позиции')
else:
    print('Нет отрицательного элемента')


# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

array = [1, 2, 3, 4, 5, 6, -1]
min1 = min(array)
array.remove(min(array))
min2 = min(array)
print(f'{min1}, {min2} - минимальные')

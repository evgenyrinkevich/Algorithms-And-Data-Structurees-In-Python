# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.

from random import choice, randint
from statistics import median


def median_search(arr: list, k):
    if len(arr) == 1:
        return arr[0]
    pivot = choice(arr)
    less = [el for el in arr if el < pivot]
    if len(less) > k:
        return median_search(less, k)
    else:
        k -= len(less)
    if arr.count(pivot) > k:
        return pivot
    else:
        k -= arr.count(pivot)
    more = [el for el in arr if el > pivot]
    return median_search(more, k)


m = 5000
flag = True
for _ in range(100):
    array = [randint(-10000, 10000) for _ in range(2 * m + 1)]
    if median_search(array, len(array) // 2) != median(array):
        flag = False
print('Test OK' if flag else 'Test Failed')

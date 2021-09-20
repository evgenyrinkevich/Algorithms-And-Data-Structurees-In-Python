# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
from random import random


def merge(left: list, right: list):
    """Combines two sorted lists into one"""
    res_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res_array.append(left[i])
            i += 1
        else:
            res_array.append(right[j])
            j += 1
    res_array.extend(left[i:]) if i < len(left) else res_array.extend(right[j:])
    return res_array


def merge_sort(arr):
    """Sorts a list using merge sorting algorithm"""
    if len(arr) <= 1:
        return
    middle = len(arr) // 2
    left, right = arr[:middle], arr[middle:]
    merge_sort(left)
    merge_sort(right)
    res = merge(left, right)
    for i in range(len(res)):
        arr[i] = res[i]


array = [random() * 50 for _ in range(5)]
print('Initial array: ', array)
merge_sort(array)
print('Sorted array: ', array)
# # Результат выполнения программы:
# Initial array:  [30.4217400302513, 43.85000230223115, 12.223107768563729, 26.21989214238153, 21.778204047544087]
# Sorted array:  [12.223107768563729, 21.778204047544087, 26.21989214238153, 30.4217400302513, 43.85000230223115]

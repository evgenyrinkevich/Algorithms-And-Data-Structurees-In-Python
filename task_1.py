# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint
import time
import functools


def timefunc(func):  # взял декоратор из предыдущей домашки
    """timefunc's doc"""

    @functools.wraps(func)
    def time_closure(*args, **kwargs):
        """time_wrapper's doc string"""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        time_elapsed = time.perf_counter() - start
        print(f"Function: {func.__name__}, Execution Time: {time_elapsed}")
        return result

    return time_closure


@timefunc
def bubble(arr):
    """Сортировка 'пузырьком'"""
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


@timefunc
def bubble_modified(arr):
    """Оптимизированная сортировка пузырьком"""
    for i in range(len(arr) - 1):
        flag = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:  # Если за весь проход не поменяли ни одной пары - массив уже отсортирован
            break
    return arr


def test_sort(func):
    print('test Ok' if [-10, 1, 2, 3, 4, 5, 6] == func([3, 2, 1, -10, 4, 6, 5]) else 'test failed')
    print('test Ok' if [2, 3, 3, 4, 4, 4, 5] == func([3, 2, 3, 4, 4, 4, 5]) else 'test failed')
    print('test Ok' if [-10, 1] == func([1, -10]) else 'test failed')


# test_sort(bubble_modified)
if __name__ == '__main__':
    for length in (100, 1000, 10000):
        array = [randint(-100, 99) for _ in range(length)]
        print(f'Array length = {length}, ')
        bubble(array)
        bubble_modified(array)
# Результат выполнения программы:
# Array length = 100,
# Function: bubble, Execution Time: 0.0009088839999999987
# Function: bubble_modified, Execution Time: 1.1607000000000284e-05
# Array length = 1000,
# Function: bubble, Execution Time: 0.110286945
# Function: bubble_modified, Execution Time: 0.00013857000000000452
# Array length = 10000,
# Function: bubble, Execution Time: 11.170633185
# Function: bubble_modified, Execution Time: 0.001266827000000248
# Удивительно большая разница между алгоритмами

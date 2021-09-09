# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов

# Определить, какое число в массиве встречается чаще всего.
from random import randint
from collections import Counter
import time
import functools


def timefunc(func):
    """timefunc's doc"""

    @functools.wraps(func)
    def time_closure(*args, **kwargs):
        """time_wrapper's doc string"""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        time_elapsed = time.perf_counter() - start
        print(f"Function: {func.__name__}, Time: {time_elapsed}")
        return result

    return time_closure


@timefunc
def max_count_el_1(arr):
    max_num = None
    max_count = 0
    for el in arr:
        if max_count < arr.count(el):
            max_count = arr.count(el)
            max_num = el
    return max_num, max_count
# Тут проходим по списку из n элементов, каждый сравниваем с list.count(element), который стоит O(n)
# В итоге получаем сложность O(n**2)


@timefunc
def max_count_el_2(arr):
    counter = Counter(arr)
    return counter.most_common(1)
# Почитал документацию- инициализация Counter стоит O(n), Counter.most_common(1) - тоже O(n),
# (сложность возрастает если ищем не 1, а больше элементов)
#  В итоге общая сложность алгоритма - O(n)


@timefunc
def max_count_el_3(arr):
    dict_count = {el: 0 for el in arr}
    for el in arr:
        dict_count[el] += 1
    return max(dict_count, key=dict_count.get)
# В этом алгоритме сложность O(n), так как тут проходим по массиву и добавляем счетчик в словарь


for i in (100, 1000, 10000):
    array = [randint(1, 100000) for _ in range(i)]
    max_count_el_1(array)
    max_count_el_2(array)
    max_count_el_3(array)

# Результаты выполнения программы:
# Function: max_count_el_1, Time: 0.00014107699999999987
# Function: max_count_el_2, Time: 5.589500000000025e-05
# Function: max_count_el_3, Time: 2.672599999999775e-05
# Function: max_count_el_1, Time: 0.014352967000000001
# Function: max_count_el_2, Time: 0.00018277099999999824
# Function: max_count_el_3, Time: 0.00021467800000000287
# Function: max_count_el_1, Time: 1.4290003439999999
# Function: max_count_el_2, Time: 0.0016276710000000527
# Function: max_count_el_3, Time: 0.002409243999999866



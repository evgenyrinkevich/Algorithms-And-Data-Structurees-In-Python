# 1. Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
from collections import Counter
from sys import getsizeof

# Тут пришлось каждой функции возвращать locals(), не знаю как достать локальные переменные вне функции(наверно никак)


def show_size(var):
    """
    Считает объем памяти, выделенной под переменную
    :param var: имя переменной
    :return: размер памяти
    """
    size = getsizeof(var)
    if hasattr(var, '__iter__'):
        if hasattr(var, 'items'):
            for key, value in var.items():
                size += show_size(key)
                size += show_size(value)
        elif not isinstance(var, str):
            for item in var:
                size += show_size(item)

    return size


def get_size(variables):
    """
    Выводит на экран инфо о памяти, выделенной под переменные функции
    :param variables: словарь локальных переменных вызываемой функции
    """
    total_size = 0
    for k, val in variables.items():
        if k != 'total_size':
            print(f'Переменная {k} типа {str(type(val))[8:-2]}, размер {show_size(val)} байт')
            total_size += show_size(val)
        else:
            continue
    print(f'Общий рамер = {total_size} байт')


# Определить, какое число в массиве встречается чаще всего.
def max_count_el_1(arr):
    max_num = None
    max_count = 0
    for el in arr:
        if max_count < arr.count(el):  # насколько я понял gc съест arr.count(el) т.е. не надо учитывать
            max_count = arr.count(el)
            max_num = el
    print(max_num, max_count)
    return locals()


def max_count_el_2(arr):
    counter = Counter(arr)
    print(counter.most_common(1))
    return locals()


def max_count_el_3(arr):
    dict_count = {el: 0 for el in arr}
    for el in arr:
        dict_count[el] += 1
    print(max(dict_count, key=dict_count.get))
    return locals()


get_size(max_count_el_1([1, 2, 3, 4]))
get_size(max_count_el_2([1, 2, 3, 4]))
get_size(max_count_el_3([1, 2, 3, 4]))

# Результат выполнения программы:
# Переменная arr типа list, размер 232 байт
# Переменная max_num типа int, размер 28 байт
# Переменная max_count типа int, размер 28 байт
# Переменная el типа int, размер 28 байт
# Общий рамер = 316 байт
# Переменная arr типа list, размер 232 байт
# Переменная counter типа collections.Counter, размер 472 байт
# Общий рамер = 704 байт
# Переменная arr типа list, размер 232 байт
# Переменная dict_count типа dict, размер 456 байт
# Переменная el типа int, размер 28 байт
# Общий рамер = 716 байт
# Сложность 1го алгоритма O(n**2), 2го и 3го - O(n). Получается меньше используем памяти - медленнее скорость
# Версия Python 3.9, разрядность системы 64

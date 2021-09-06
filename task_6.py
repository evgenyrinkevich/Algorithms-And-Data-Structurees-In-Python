# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

def sum_min_max(array):
    min_idx = array.index(min(array))
    max_idx = array.index(max(array))
    if min_idx < max_idx:
        return sum(array[min_idx + 1: max_idx])
    elif max_idx < min_idx:
        return sum(array[max_idx + 1: min_idx])
    else:
        return 'минимальный и максимальный элементы равны'


print(sum_min_max([8, 4, 5, 3, 8, 7, 1, 5]))

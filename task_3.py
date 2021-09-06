# 3.В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


def min_max_swap(arr):
    min_val_idx = arr.index(min(arr))
    max_val_idx = arr.index(max(arr))
    arr[min_val_idx],  arr[max_val_idx] = arr[max_val_idx], arr[min_val_idx]
    return arr


array = [2, 3, 5, 12, 3, 2, 4]
print(min_max_swap(array))

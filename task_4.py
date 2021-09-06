# 4.Определить, какое число в массиве встречается чаще всего.

def max_count_el(arr):
    max_num = None
    max_count = 0
    for el in arr:
        if max_count < arr.count(el):
            max_count = arr.count(el)
            max_num = el
    return max_num, max_count


array = [2, 3, 5, 12, 3, 4, 4, 4]
print(f'{max_count_el(array)[0]} встречается чаще всего ({max_count_el(array)[1]} раз(а))')

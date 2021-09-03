# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
from random import randint


def max_sum_digits(array):
    """
    В списке функция находит максимальное по сумме цифр
    :param array: список натуральных чисел
    :return: max_num - искомое число, max_sum - сумма его цифр
    """
    max_sum = 0
    max_num = array[0]
    for number in array:
        sum_of_digits = 0
        for digit in str(number):
            sum_of_digits += int(digit)
        if sum_of_digits > max_sum:
            max_sum = sum_of_digits
            max_num = number
    return max_num, max_sum


arr = []
for i in range(100):
    arr.append(randint(1, 10000))
print(f'Число {max_sum_digits(arr)[0]} наибольшее по сумме цифр - {max_sum_digits(arr)[1]}')

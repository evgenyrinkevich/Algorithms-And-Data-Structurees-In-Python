# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque
HEX_TO_DEC = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}
DEC_TO_HEX = {val: k for k, val in HEX_TO_DEC.items()}
HEX_BASE = 16


def hex_sum(hex_1, hex_2):
    """
    Function returns sum of 2 hex numbers
    :param hex_1: hex number1 as list of chars, ex: ['A', '2']
    :param hex_2: hex number1 as list of chars
    :return: hex number as list of chars
    """
    hex_1, hex_2 = deque(hex_1), deque(hex_2)
    res = deque()
    add = 0
    if len(hex_1) < len(hex_2):
        hex_1.extendleft('0' for _ in range(len(hex_2) - len(hex_1)))
    else:
        hex_2.extendleft('0' for _ in range(len(hex_1) - len(hex_2)))

    for digit in hex_1.copy():
        dig_a = HEX_TO_DEC[hex_1.pop()]
        dig_b = HEX_TO_DEC[hex_2.pop()]

        if dig_a + dig_b + add < HEX_BASE:
            res.appendleft(dig_a + dig_b + add)
            add = 0
        else:
            res.appendleft((dig_a + dig_b + add) % HEX_BASE)
            add = 1
    if add != 0:
        res.appendleft(add)
    res_list = []
    for digit in res:
        res_list.append(DEC_TO_HEX[digit])
    return res_list


def hex_multiply(hex_1, hex_2):
    """
    Multiplies 2 hex numbers
    :param hex_1: hex number1 as list of chars, ex: ['A', '2']
    :param hex_2: hex number1 as list of chars
    :return: hex number as list of chars
    """
    multiply = deque()
    for i in range(len(hex_2) - 1, -1, -1):
        add = 0
        multiply_i = deque()
        dec_2 = HEX_TO_DEC[hex_2[i]]

        for j in range(len(hex_1) - 1, -1, -1):
            dec_1 = HEX_TO_DEC[hex_1[j]]
            multiply_dec = dec_2 * dec_1 + add
            multiply_i.appendleft(DEC_TO_HEX[multiply_dec % HEX_BASE])
            add = multiply_dec // HEX_BASE
        if add != 0:
            multiply_i.appendleft(DEC_TO_HEX[add])

        for j in range(len(hex_2) - 1 - i):
            multiply_i.append('0')
        multiply = hex_sum(multiply_i, multiply)

    return multiply


a = list(input('Введите 1ое 16ное число: ').upper())
b = list(input('Введите 2ое 16ное число: ').upper())
print(hex_sum(a, b))
print(hex_multiply(a, b))
# Результат выполнения программы:
# Введите 1ое 16ное число: 4a6
# Введите 2ое 16ное число: c12b
# ['C', '5', 'D', '1']
# ['3', '8', '1', 'E', 'D', 'E', '2']


# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

num1 = int(input('Введите 1ое число: '))
num2 = int(input('Введите 2ое число: '))
num3 = int(input('Введите 3ое число: '))

mid_num = None
if num1 <= num2:
    if num1 <= num3:
        if num2 <= num3:
            mid_num = num2
        else:
            mid_num = num3
    else:
        mid_num = num1
else:
    if num1 <= num3:
        mid_num = num1
    else:
        if num2 <= num3:
            mid_num = num3
        else:
            mid_num = num2


print(f'Среднее число - {mid_num}')

# 2ой вариант решения

mid_num = num1 + num2 + num3 - min(num1, num2, num3) - max(num1, num2, num3)
print(f'Среднее число - {mid_num}')

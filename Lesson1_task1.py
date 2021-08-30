# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input('Введите трехзначное число: '))

if 99 < number < 1000:
    digit_1 = number % 10
    digit_2 = (number // 10) % 10
    digit_3 = number // 100
    print(f'Сумма цифр равна {digit_1 + digit_2 + digit_3}\n Произведение цифр равно {digit_1 * digit_2 * digit_3}')
else:
    print('Ошибка')



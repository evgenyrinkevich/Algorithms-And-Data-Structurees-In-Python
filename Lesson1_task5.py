# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

letter_1 = ord(input('Введите 1ую букву от "a" до "z": '))
letter_2 = ord(input('Введите 2ую букву от "a" до "z": '))

min_letter, max_letter = ord('a') - 1, ord('z') + 1

if min_letter < letter_1 < max_letter and min_letter < letter_2 < max_letter:
    if letter_1 != letter_2:
        print(f'"{chr(letter_1)}" находится на {letter_1 - min_letter} месте алфавита, ')
        print(f'"{chr(letter_2)}" на {letter_2 - min_letter} месте')
        print(f'Между ними {abs(letter_1 - letter_2) - 1} букв(ы)')
    else:
        print(f'"{chr(letter_1)}" находится на {letter_1 - min_letter} месте алфавита')

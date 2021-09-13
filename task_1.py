# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
import collections
from random import randint

NUM_OF_COMPANIES = int(input('Введите кол-во предприятий: '))
income_info = {}
for i in range(NUM_OF_COMPANIES):
    name = input(f'Введите название {i + 1} компании: ')
    income_info[name] = collections.defaultdict(int)  # инициализуруем словари,
    # для каждого предприятия во вложенном словаре хранится поквартальная прибыль
avg_income = 0

for name in income_info:
    yearly_income = 0
    for i in (1, 2, 3, 4):
        income_info[name][i] = randint(800, 1200)  # генерируем прибыль случайно
        yearly_income += income_info[name][i]  # считаем прибыль предприятия за год
    income_info[name]['yearly_income'] = yearly_income
    avg_income += yearly_income
avg_income /= NUM_OF_COMPANIES
print(f'Средняя прибыль равна {avg_income}\n---------------------------')
for name in income_info:
    print(f"Прибыль {name} на {income_info[name]['yearly_income'] - avg_income} выше средней"
          if avg_income <= income_info[name]['yearly_income'] else
          f"Прибыль {name} на {avg_income - income_info[name]['yearly_income']} ниже средней")

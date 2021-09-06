# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
START = 2
FINISH = 99
min_num = 2
max_num = 9
print(f'В диапазоне от {START} до {FINISH}')
for i in range(min_num, max_num + 1):
    counter = 0
    for j in range(START, FINISH + 1):
        if j % i == 0:
            counter += 1
    print(f'На {i} делятся {counter} чисел')

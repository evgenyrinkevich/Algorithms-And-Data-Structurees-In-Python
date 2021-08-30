# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки

print('Введите координаты 1ой точки')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

print('Введите координаты 2ой точки')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

if x1 == x2:
    print('Уравнение прямой: x = ', x1)
else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    print(f'Уравнение прямой: y = {k}x + {b}')

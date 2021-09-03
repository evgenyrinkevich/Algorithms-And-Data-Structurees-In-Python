# 7. Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

def check_equation(n):
    if isinstance(n, int) and n > 0:
        return sum(range(1, n + 1)) == int(n * (n + 1) / 2)
    else:
        pass


print(check_equation(5))

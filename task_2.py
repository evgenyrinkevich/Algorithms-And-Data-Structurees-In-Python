# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов
import time
import functools


def timefunc(func):
    """timefunc's doc"""

    @functools.wraps(func)
    def time_closure(*args, **kwargs):
        """time_wrapper's doc string"""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        time_elapsed = time.perf_counter() - start
        print(f"Function: {func.__name__}, Time: {time_elapsed}")
        return result

    return time_closure


@timefunc
def trial_division(num):
    primes = []
    for number in range(2, num + 1):
        i = 2
        j = 0
        while i * i <= number and j != 1:  # здесь кв. корень выполнений цикла
            if number % i == 0:
                j = 1
            i += 1
        if j != 1:
            primes.append(number)
    return primes


# Алгоритм перебора делителей для каждого числа будет искать делители кв. корень из этого числа раз
# Поэтому сложность алгоритма будет O(n* sqrt(n))

@timefunc
def eratosthenes(num):  # этот алгоритм из методички
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(num):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < num:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < num:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b


# Этот алгоритм имеет сложность O(n*log(log(n)))


for n in (10000, 100000, 1000000):
    trial_division(n)
    eratosthenes(n)

# Результаты выполнения программы:
# Function: trial_division, Time: 0.020637972999999997
# Function: eratosthenes, Time: 0.004730252999999997
# Function: trial_division, Time: 0.49863207
# Function: eratosthenes, Time: 0.05480699900000008
# Function: trial_division, Time: 11.312962279999999
# Function: eratosthenes, Time: 0.5778850200000001

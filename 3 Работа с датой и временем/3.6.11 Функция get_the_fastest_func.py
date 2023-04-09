# Функция get_the_fastest_func()
# Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:
#
# funcs — список произвольных функций
# arg — произвольный объект
# Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая затратила на вычисление значения
# при вызове с аргументом arg наименьшее количество времени.

import time


def get_the_fastest_func(funcs, arg):
    dct = {}
    for f in funcs:
        start_time = time.perf_counter()
        f(arg)
        end_time = time.perf_counter()
        dct[end_time - start_time] = f
    return dct[min(dct.keys())]

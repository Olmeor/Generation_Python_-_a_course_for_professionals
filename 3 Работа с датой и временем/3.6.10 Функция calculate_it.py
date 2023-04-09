# Функция calculate_it()
# Реализуйте функцию calculate_it(), которая принимает один или более аргументов в следующем порядке:
#
# func — произвольная функция
# *args — переменное количество позиционных аргументов, каждый из которых является произвольным объектом
# Функция должна возвращать кортеж, первым элементом которого является возвращаемое значение функции func при вызове с
# аргументами *args, а вторым — примерное время (в секундах), затраченное на вычисление этого значения.

import time


def calculate_it(func, *args):
    start_time = time.perf_counter()
    res = func(*args)
    end_time = time.perf_counter()
    return res, end_time - start_time


def add(a, b, c):
    time.sleep(3)
    return a + b + c


print(calculate_it(add, 1, 2, 3))
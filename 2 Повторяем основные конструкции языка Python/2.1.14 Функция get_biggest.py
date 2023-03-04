# Функция get_biggest() 🌶️🌶️
# Реализуйте функцию get_biggest(), которая принимает один аргумент:
#
# numbers — список целых неотрицательных чисел
# Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers. Если список numbers
# пуст, функция должна вернуть число −1.

from functools import reduce


def get_biggest(numbers):
    if len(numbers) == 0:
        return -1
    nums = sorted(numbers, key=lambda x: str(x) * max(numbers), reverse=True)
    res = int(reduce(lambda r, e: r + str(e), nums, ''))
    return res

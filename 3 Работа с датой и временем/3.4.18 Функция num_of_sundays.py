# Функция num_of_sundays()
# Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:
# year — натуральное число, год
# Функция должна возвращать количество воскресений в году year.

from datetime import datetime


def num_of_sundays(y):
    return datetime(y, 12, 31).strftime('%U')

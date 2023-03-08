# Функция is_correct()
# Реализуйте функцию is_correct(), которая принимает три аргумента в следующем порядке:
#
# day — натуральное число, день
# month — натуральное число, месяц
# year — натуральное число, год
# Функция должна возвращать True, если дата с компонентами day, month и year является корректной, или False в противном
# случае.

from datetime import date


def is_correct(day, month, year):
    try:
        my_date = date(year, month, day)
        return True
    except:
        return False

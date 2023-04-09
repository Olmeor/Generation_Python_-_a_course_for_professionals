# Функция get_all_mondays()
# Реализуйте функцию get_all_mondays(), которая принимает один аргумент:
#
# year — натуральное число
# Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year, выпадающих на
# понедельник.

import calendar
from datetime import date, timedelta


def get_all_mondays(y):
    dt = date(y, 1, 1)
    res = []
    while dt < date(y + 1, 1, 1):
        if calendar.weekday(dt.year, dt.month, dt.day) == 0:
            res.append(dt)
        dt += timedelta(days=1)
    return res

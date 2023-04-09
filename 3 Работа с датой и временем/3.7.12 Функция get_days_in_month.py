# Функция get_days_in_month()
# Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем порядке:
#
# year — натуральное число
# month — полное название месяца на английском
# Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month и года year.

import calendar
from datetime import date


def get_days_in_month(y, m):
    m = list(calendar.month_name).index(m)
    count_day = calendar.monthrange(int(y), m)[1]
    arr = [date(y, m, i) for i in range(1, count_day + 1)]
    return arr

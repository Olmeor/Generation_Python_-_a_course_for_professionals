# Функция get_date_range()
# Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:
#
# start — начальная дата, тип date
# end — конечная дата, тип date
# Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start до end включительно. Если
# start > end, функция должна вернуть пустой список.

from datetime import date


def get_date_range(start, end):
    d = start
    res = []
    while d <= end:
        res.append(d)
        d = date.fromordinal(d.toordinal() + 1)
    return res


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')

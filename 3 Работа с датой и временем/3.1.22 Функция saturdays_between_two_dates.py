# Функция saturdays_between_two_dates()
# Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:
#
# start — начальная дата, тип date
# end — конечная дата, тип date
# Функция должна возвращать количество суббот между датами start и end включительно.

from datetime import date


def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start
    d = start
    count = 0
    while d <= end:
        if d.weekday() == 5:
            count += 1
        d = date.fromordinal(d.toordinal() + 1)
    return count


date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))

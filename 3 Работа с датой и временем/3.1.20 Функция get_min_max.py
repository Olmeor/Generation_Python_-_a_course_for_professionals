# Функция get_min_max()
# Реализуйте функцию get_min_max(), которая принимает один аргумент:
#
# dates — список дат (тип date)
# Функция должна возвращать кортеж, первым элементом которого является минимальная дата из списка dates, вторым —
# максимальная дата из списка dates. Если список dates пуст, функция должна вернуть пустой кортеж.

from datetime import date


def get_min_max(d):
    if not d:
        return tuple()
    else:
        return min(d), max(d)


dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]

print(get_min_max(dates))

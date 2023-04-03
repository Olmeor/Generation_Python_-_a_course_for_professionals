# Функция fill_up_missing_dates()
# Реализуйте функцию fill_up_missing_dates(), которая принимает на вход один аргумент:
# dates — список строковых дат в формате DD.MM.YYYY
# Функция должна возвращать список, в котором содержатся все даты из списка dates, расположенные в порядке возрастания,
# а также все недостающие промежуточные даты.

from datetime import datetime, timedelta


def fill_up_missing_dates(dates_list):
    dates_list = list(map(lambda d: datetime.strptime(d, '%d.%m.%Y'), dates_list))
    min_d = min(dates_list)
    max_d = max(dates_list)
    res = []
    while min_d <= max_d:
        res.append(datetime.strftime(min_d, '%d.%m.%Y'))
        min_d += timedelta(days=1)
    return res

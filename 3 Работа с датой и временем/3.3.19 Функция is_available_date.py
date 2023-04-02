# Функция is_available_date() 🌶️
# Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна ли та или иная дата для
# бронирования номера.
#
# Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:
#
# booked_dates — список строковых дат, недоступных для бронирования. Элементом списка является либо одиночная дата,
# либо период (две даты через дефис). Например:
# ['04.11.2021', '05.11.2021-09.11.2021']
# date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает забронировать
# номер. Например:
# '01.11.2021' или '01.11.2021-04.11.2021'
# Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступна для
# бронирования. В противном случае функция должна возвращать False.

from datetime import datetime


def get_timestamp(d):
    return datetime.strptime(d, '%d.%m.%Y').toordinal()


def get_range(r):
    r = r.split('-')
    return set(range(int(get_timestamp(r[0])), int(get_timestamp(r[1]) + 1)))


def is_available_date(booked_dates, date_for_booking):
    bd = set()
    for day in booked_dates:
        bd |= get_range(day) if '-' in day and len(set(day.split('-'))) != 1 else {get_timestamp(day.split('-')[0])}
    sd = set()
    sd |= get_range(date_for_booking) if '-' in date_for_booking else {get_timestamp(date_for_booking)}
    return bd - sd == bd

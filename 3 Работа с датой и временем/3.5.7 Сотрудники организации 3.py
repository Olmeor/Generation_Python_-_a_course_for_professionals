# Сотрудники организации 😔
# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. Напишите программу, которая
# определяет самого молодого сотрудника, празднующего свой день рождения в течение ближайших семи дней от текущей даты.

from datetime import date, datetime, timedelta


def get_td(td):
    md = date(int(date.strftime(td, '%Y')), 1, 1)
    return (td - md).days


pattern = '%d.%m.%Y'
b = datetime.strptime(input(), pattern).date()
arr = [get_td(b + timedelta(days=i)) for i in range(1, 8)]
dct = {}
for _ in range(int(input())):
    n, f, dt = input().split()
    dct[datetime.strptime(dt, pattern).date()] = n + ' ' + f

dct = dict(sorted(dct.items(), reverse=True))
for d in dct.keys():
    if get_td(d) in arr:
        print(dct[d])
        break
else:
    print('Дни рождения не планируются')

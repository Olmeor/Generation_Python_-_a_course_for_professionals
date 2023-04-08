# Сотрудники организации 😄
# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. Напишите программу, которая
# определяет самого старшего сотрудника из данного списка.

from datetime import date, datetime

dct = {}
count = {}
for _ in range(int(input())):
    n, f, d = input().split()
    d = datetime.strptime(d, '%d.%m.%Y').date()
    dct[n + ' ' + f] = d
    count[d] = count.get(d, 0) + 1

dct = dict(sorted(dct.items(), key=lambda e: e[1]))
n, d = list(dct.items())[0]
if count[d] == 1:
    print(date.strftime(d, '%d.%m.%Y'), n)
else:
    print(date.strftime(d, '%d.%m.%Y'), count[d])

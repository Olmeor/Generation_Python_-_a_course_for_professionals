# Сотрудники организации 🙂
# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. Напишите программу, которая
# определяет, в какую из дат родилось больше всего сотрудников.

from datetime import date, datetime

count = {}
for _ in range(int(input())):
    *n, d = input().split()
    d = datetime.strptime(d, '%d.%m.%Y').date()
    count[d] = count.get(d, 0) + 1

count = dict(sorted(count.items(), key=lambda e: e[1], reverse=True))
m = list(count.values())[0]
for d, v in sorted(count.items()):
    if v == m:
        print(date.strftime(d, '%d.%m.%Y'))

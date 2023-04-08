# Самое понятное условие
# Даны две даты — левая и правая границы диапазона соответственно. Напишите программу, которая из этого диапазона,
# включая границы, выводит, начиная с даты, у которой сумма дня и месяца нечетная, каждую третью дату, только если она
# не понедельник и не четверг.

from datetime import datetime, timedelta

start, end = [datetime.strptime(input(), '%d.%m.%Y') for _ in '__']
td = timedelta(days=1)
count = 1
while start <= end:
    d = int(datetime.strftime(start, '%d'))
    m = int(datetime.strftime(start, '%m'))
    w = start.date().weekday()
    if (d + m) % 2 and count == 1:
        if w != 0 and w != 3:
            print(datetime.strftime(start, '%d.%m.%Y'))
        count = 3
    elif count == 3 and w != 0 and w != 3:
        print(datetime.strftime(start, '%d.%m.%Y'))
    start += timedelta(days=count)

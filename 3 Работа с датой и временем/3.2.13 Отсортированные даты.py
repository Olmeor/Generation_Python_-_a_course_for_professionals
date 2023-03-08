# Отсортированные даты
# Напишите программу, которая принимает на вход последовательность дат и выводит их в порядке неубывания.

from datetime import date

dates = sorted([date.fromisoformat(input()) for _ in range(int(input()))])

for d in dates:
    print(d.strftime('%d/%m/%Y'))

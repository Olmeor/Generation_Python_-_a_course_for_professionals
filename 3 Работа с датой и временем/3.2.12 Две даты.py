# Две даты
# Напишите программу, которая принимает на вход две даты и выводит ту, что меньше.

from datetime import date

date1 = date.fromisoformat(input())
date2 = date.fromisoformat(input())
min_date = min(date1, date2)
print(min_date.strftime('%d-%m (%Y)'))

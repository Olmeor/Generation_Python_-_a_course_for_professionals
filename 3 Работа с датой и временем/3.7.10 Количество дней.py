# Количество дней 😉
# Напишите программу, которая определяет количество дней в заданном месяце.

import calendar

y, m = map(int, input().split())
count = calendar.monthrange(y, m)[1]
print(count)

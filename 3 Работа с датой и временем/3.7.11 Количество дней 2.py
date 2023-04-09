# Количество дней 😎
# Напишите программу, которая определяет количество дней в заданном месяце.

import calendar

y, m = input().split()
count = calendar.monthrange(int(y), list(calendar.month_name).index(m))[1]
print(count)

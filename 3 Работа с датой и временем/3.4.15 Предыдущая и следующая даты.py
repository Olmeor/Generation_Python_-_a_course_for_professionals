# Предыдущая и следующая даты
# Напишите программу, которая принимает на вход дату и выводит предыдущую и следующую даты.

from datetime import datetime, timedelta

pattern = '%d.%m.%Y'
delta = timedelta(days=1)
dt = datetime.strptime(input(), pattern)
print((dt - delta).strftime(pattern))
print((dt + delta).strftime(pattern))

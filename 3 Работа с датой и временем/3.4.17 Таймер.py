# Таймер
# Часы показывают время в формате HH:MM:SS. На этих часах запустили таймер, который прозвенит через n секунд. Напишите
# программу, которое определит, какое время будет на часах, когда прозвенит таймер.

from datetime import datetime, timedelta

pattern = '%H:%M:%S'
t = datetime.strptime(input(), pattern)
n = timedelta(seconds=int(input()))
print((t + n).strftime(pattern))

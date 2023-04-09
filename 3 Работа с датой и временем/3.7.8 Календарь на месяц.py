# Календарь на месяц
# Напишите программу, которая выводит календарь на заданные год и месяц.

from calendar import prmonth
from datetime import datetime

dt = datetime.strptime(input(), '%Y %b')

prmonth(dt.year, dt.month)

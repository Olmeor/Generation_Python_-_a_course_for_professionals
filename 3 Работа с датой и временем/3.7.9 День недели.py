# День недели
# Напишите программу, которая определяет день недели, соответствующий заданной дате.

import calendar
from datetime import datetime

dt = datetime.fromisoformat(input())

print(list(calendar.day_name)[dt.weekday()])

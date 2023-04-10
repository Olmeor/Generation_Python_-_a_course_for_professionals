# Размах данных
# Дана последовательность дат. Напишите программу, которая выводит количество дней между максимальной и минимальной
# датами данной последовательности.

# put your python code here
import sys
from datetime import datetime, timedelta

arr = [datetime.fromisoformat(line.strip('\n')) for line in sys.stdin]
print((max(arr) - min(arr)).days)

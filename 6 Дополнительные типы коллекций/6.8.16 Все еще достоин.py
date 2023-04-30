# Все еще достоин
# Дан список имен учеников и их оценок за экзамен. Напишите программу, которая определяет второго по счету ученика,
# имеющего самую низкую оценку.

# put your python code here
from collections import Counter
import sys

counter = Counter(dict([tuple(line.split()) for line in sys.stdin]))
print(sorted(counter.items(), key=lambda e: int(e[1]))[1][0])

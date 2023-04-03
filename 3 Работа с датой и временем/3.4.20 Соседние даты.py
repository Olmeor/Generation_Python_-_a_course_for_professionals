# Соседние даты
# Дана последовательность дат. Напишите программу, которая создает и выводит список, элементами которого являются
# неотрицательные целые числа — количество дней между двумя соседними датами последовательности.

from datetime import datetime

dates = [datetime.strptime(dt, '%d.%m.%Y') for dt in input().split()]
deltas = [abs(dates[i] - dates[i - 1]).days for i in range(1, len(dates))]

print(deltas)

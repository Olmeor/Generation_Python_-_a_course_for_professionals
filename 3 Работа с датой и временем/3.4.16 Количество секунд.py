# Количество секунд
# Напишите программу, которая принимает на вход время и выводит целое количество секунд, прошедшее с начала суток.

from datetime import timedelta

hours, minutes, seconds = map(int, input().split(':'))
print(int(timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()))

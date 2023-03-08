# Корректные даты
# Напишите программу, которая принимает на вход последовательность дат и проверяет каждую из них на корректность.

# put your python code here
from datetime import date


def is_correct(args):
    try:
        day, month, year = args
        my_date = date(year, month, day)
        return 'Корректная'
    except:
        return 'Некорректная'


lst = []
while True:
    d = input()
    if d == 'end':
        break
    lst.append(is_correct(map(int, d.split('.'))))

print(*lst, lst.count('Корректная'), sep='\n')

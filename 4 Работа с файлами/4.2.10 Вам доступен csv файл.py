# Вам доступен csv файл grades.csv, имеющий следующее содержание:
#
# name;grade
# Timur;100
# Ruslan;97
# Ниже представлена программа, которая должна открывать данный файл и выводить содержимое каждой строки в виде списка.
# В программе допущена ошибка, поэтому она выводит:
#
# ['n']
# ['a']
# ['m']
# ['e']
# ['', '']
# ['g']
# ['r']
# ['a']
# ['d']
# ['e']
# []
# ['T']
# ...
# Найдите и исправьте ее, чтобы результатом работы программы были строки:
#
# ['name', 'grade']
# ['Timur', '100']
# ['Ruslan', '97']

import csv

with open('grades.csv', encoding='utf-8') as csv_file:
    rows = csv.reader(csv_file, delimiter=';')
    for row in rows:
        print(row)

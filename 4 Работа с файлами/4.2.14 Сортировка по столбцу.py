# Сортировка по столбцу
# Вам доступен файл deniro.csv, каждый столбец которого содержит либо только числа, либо только слова:
#
# Machete,2010,72
# Marvin's Room,1996,80
# Raging Bull,1980,97
# ...
#
# Напишите программу, которая сортирует содержимое данного файла по указанному столбцу. Причем данные должны быть
# отсортированы в порядке возрастания чисел, если столбец содержит числа, и в лексикографическом порядке слов, если
# столбец содержит слова.

import csv

with open('deniro.csv', encoding='utf-8') as file:
    data = csv.reader(file)
    table = [row for row in data]
    column = int(input()) - 1
    table.sort(key=lambda e: int(e[column]) if column else e[column])
    print(*[','.join(row) for row in table], sep="\n")

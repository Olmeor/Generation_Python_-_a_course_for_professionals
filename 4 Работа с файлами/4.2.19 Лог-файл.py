# Лог-файл
# Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя. В первом столбце записано
# измененное имя пользователя, во втором — адрес электронной почты, в третьем — дата и время изменения. При этом email
# пользователь менять не может, только имя:
#
# username,email,dtime
# rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
# busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
# ...
#
# Напишите программу, которая отбирает из файла name_log.csv только самые свежие записи для каждого пользователя и
# записывает их в файл new_name_log.csv. В файле new_name_log.csv первой строкой должны быть заголовки столбцов такие
# же, как в файле name_log.csv. Логи в итоговом файле должны быть расположены в лексикографическом порядке названий
# электронных ящиков пользователей.

import csv
from datetime import datetime

dct = {}
with open('name_log.csv', encoding='utf-8') as file_in:
    data = csv.reader(file_in)
    columns = next(data)
    for row in data:
        if dct.get(row[1]) == None or datetime.strptime(dct[row[1]][2], "%d/%m/%Y %H:%M") < datetime.strptime(row[2], "%d/%m/%Y %H:%M"):
            dct[row[1]] = row

dct = dict(sorted(dct.items(), key=lambda e: e[0]))

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file_out:
    writer = csv.writer(file_out)
    writer.writerow(columns)
    for row in dct.values():
        writer.writerow(row)

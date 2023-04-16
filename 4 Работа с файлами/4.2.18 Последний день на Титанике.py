# Последний день на Титанике
# Вам доступен файл titanic.csv, который содержит данные о пассажирах, присутствовавших на борту парохода Титаник. В
# первом столбце указана единица, если пассажир выжил, и ноль в противном случае, во втором столбце записано полное имя
# пассажира, в третьем — пол, в четвертом — возраст:
#
# survived;name;sex;age
# 0;Mr. Owen Harris Braund;male;22
# 1;Mrs. John Bradley (Florence Briggs Thayer) Cumings;female;38
# ...
# Напишите программу, которая выводит имена выживших пассажиров, которым было менее 18 лет, каждое на отдельной строке.
# Причем сначала должны быть расположены имена всех пассажиров мужского пола, а затем — женского, имена же
# непосредственно в мужском и женском списках должны быть расположены в своем исходном порядке.

import csv

lst = []
with open('titanic.csv', encoding='utf-8') as file_in:
    data = csv.reader(file_in, delimiter=';', quotechar='"')
    next(data)
    for row in data:
        if int(row[0]) == 1 and float(row[3]) < 18:
            lst.append([row[1], row[2]])
    lst.sort(key=lambda e: e[1], reverse=True)

print(*[e[0] for e in lst], sep="\n")

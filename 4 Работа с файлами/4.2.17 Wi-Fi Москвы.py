# Wi-Fi Москвы
# Вам доступен файл wifi.csv, который содержит данные о городском Wi-Fi Москвы. В первом столбце записано название
# округа, во втором — название района, в третьем — адрес, в четвертом — количество точек доступа по этому адресу:
#
# adm_area;district;location;number_of_access_points
# Центральный административный округ;район Якиманка;город Москва, улица Серафимовича, дом 5/16;5
# Центральный административный округ;район Якиманка;город Москва, Болотная набережная, дом 11, строение 1;2
# ...
# Напишите программу, которая определяет количество точек доступа в каждом районе Москвы и выводит названия всех
# районов, для каждого указывая соответствующее количество точек доступа, каждое на отдельной строке, в следующем формате:
#
# <название района>: <количество точек доступа>
# Названия районов должны быть расположены в порядке убывания количества точек доступа, при совпадении количества точек
# доступа — в лексикографическом порядке.

import csv

dct = {}
with open('wifi.csv', encoding='utf-8') as file_in:
    data = csv.reader(file_in, delimiter=';')
    next(data)
    for row in data:
        dct[row[1]] = dct.get(row[1], 0) + int(row[3])
    dct = dict(sorted(dct.items(), key=lambda e: (-int(e[1]), e[0])))

print(*[f"{i}: {v}" for i, v in dct.items()], sep="\n")

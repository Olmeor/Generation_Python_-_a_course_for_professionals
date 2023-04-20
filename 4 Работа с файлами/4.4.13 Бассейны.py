# Бассейны
# Тимур планирует пойти в бассейн. Среди всех бассейнов ему подходят те, которые открыты в понедельник в период с 10:00
# до 12:00. Также ему нравится плавать по длинным дорожкам, поэтому из всех работающих в это время бассейнов нужно
# выбрать бассейн с наибольшей длиной дорожки, при равных значениях — c наибольшей шириной.
#
# Вам доступен файл pools.json, содержащий список JSON-объектов, которые представляют данные о крытых плавательных
# бассейнах:
#
# [
#    {
#       "ObjectName": "Физкультурно-оздоровительный комплекс с бассейном «ГБУ «СШОР № 82» Москомспорта»",
#       "AdmArea": "Северо-Восточный административный округ",
#       "District": "Алтуфьевский район",
#       "Address": "Инженерная улица, дом 5, корпус 1",
#       "WorkingHoursSummer": {
#          "Понедельник": "10:00-11:00",
#          "Вторник": "10:00-11:00",
#          "Среда": "10:00-11:00",
#          "Четверг": "10:00-11:00",
#          "Пятница": "10:00-11:00",
#          "Суббота": "10:00-11:00",
#          "Воскресенье": "09:00-15:00",
#       },
#       "DimensionsSummer": {
#          "Square": 350,
#          "Length": 25,
#          "Width": 14,
#          "Depth": 1.8
#       }
#    },
#    ...
# ]
# Под «бассейном» будем подразумевать один JSON-объект из этого списка. У бассейна имеются следующие атрибуты:
#
# ObjectName — название, будь то фитнес клуб или спортивный комплекс
# AdmArea — административный округ
# District — название района
# Address — адрес
# WorkingHoursSummer — график работы, время начала и закрытия указываются в формате HH:MM
# DimensionsSummer — размеры бассейна, где Square — площадь, Length — длина, Width — ширина, Depth — глубина
# Напишите программу, которая определяет бассейн, подходящий Тимуру. Программа должна вывести его размеры и адрес в
# следующем формате:
#
# <длина>x<ширина>
# <адрес>

import json
from datetime import time

with open('pools.json', encoding='utf-8') as file_in:
    pools = json.load(file_in)
    lst = []
    for pool in pools:
        t = pool['WorkingHoursSummer']['Понедельник']
        if time(int(t[:2])) <= time(10) and time(int(t[6:8])) >= time(12):
            lst.append([pool['DimensionsSummer']['Length'], pool['DimensionsSummer']['Width'], pool['Address']])
    lst.sort(key=lambda x: (x[0], x[1]), reverse=True)
    print(f"{lst[0][0]}x{lst[0][1]}", lst[0][2], sep="\n")

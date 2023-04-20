# Общественное питание 😥
# Вам доступен файл food_services.json, содержащий список JSON-объектов, которые представляют данные о заведениях
# общественного питания:
#
# [
#    {
#       "Name": "СМЕТАНА",
#       "IsNetObject": "нет",
#       "OperatingCompany": "",
#       "TypeObject": "кафе",
#       "AdmArea": "Северо-Восточный административный округ",
#       "District": "Ярославский район",
#       "Address": "город Москва, улица Егора Абакумова, дом 9",
#       "SeatsCount": 48
#    },
#    ...
# ]
# Под «заведением» будем подразумевать один JSON-объект из этого списка. У заведения имеются следующие атрибуты:
#
# Name — название
# IsNetObject — да\нет в зависимости от того, является ли заведение сетевым
# OperatingCompany — название сети
# TypeObject — вид (кафе, столовая, ресторан и т.д.)
# AdmArea — административная зона
# District — район
# Address — полный адрес
# SeatsCount — количество мест
# Напишите программу, которая:
#
# определяет район Москвы, в котором находится больше всего заведений, и выводит название этого района и количество
# заведений в нем
# определяет сеть с самым большим числом заведений и выводит название этой сети и количество заведений этой сети
# Полученные значения программа должна вывести в следующем формате:
#
# <район>: <количество заведений>
# <название сети>: <количество заведений>

import json

with open('food_services.json', encoding='UTF-8') as file_in:
    data = json.load(file_in)
    dist = {}
    comp = {}
    for row in data:
        dist[row['District']] = dist.get(row['District'], 0) + 1
        if row['OperatingCompany']:
            comp[row['OperatingCompany']] = comp.get(row['OperatingCompany'], 0) + 1
    print(*max(dist.items(), key=lambda x: int(x[1])), sep=": ")
    print(*max(comp.items(), key=lambda x: int(x[1])), sep=": ")

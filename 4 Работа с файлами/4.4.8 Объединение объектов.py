# Объединение объектов
# Вам доступны два файла data1.json и data2.json, каждый из которых содержит по единственному JSON-объекту:
#
# {
#    "Holly-Anne": [
#       33,
#       "failed"
#    ],
#    "Caty": [
#       36,
#       "failed"
#    ],
#    ...
# }
# Напишите программу, которая объединяет два данных JSON-объекта в один JSON-объект, причем если пары из первого и
# второго объектов имеют совпадающие ключи, то значение следует взять из второго объекта. Полученный JSON-объект
# программа должна записать в файл data_merge.json.

import json

with open('data1.json') as file1, open('data2.json') as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)
    data_merge = data1 | data2

with open('data_merge.json', 'w', encoding='utf8') as file_out:
    file_out.write(json.dumps(data_merge, indent=3))

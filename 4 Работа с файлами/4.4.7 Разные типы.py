# Разные типы
# Вам доступен файл data.json, содержащий список различных объектов:
#
# [
#    "nwkWXma",
#    null,
#    {
#       "ISgHT": "dIUbf"
#    },
#    "Pzt",
#    "BXcbGVTE",
#    ...
# ]
# Напишите программу, которая создает список, элементами которого являются объекты из списка, содержащегося в файле
# data.json, измененные по следующим правилам:
#
# если объект является строкой, в его конец добавляется восклицательный знак
# если объект является числом, он увеличивается на единицу
# если объект является логическое значением, он инвертируется
# если объект является списком, он удваивается
# если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
# если объект является пустым значением (null), он не добавляется
# Полученный список программа должна записать в файл updated_data.json.

import json

with open('data.json') as file_in, open('updated_data.json', 'w', encoding='utf8') as file_out:
    data_json = json.load(file_in)
    updated_data = []

    for e in data_json:
        if isinstance(e, str):
            updated_data.append(e + '!')
        elif isinstance(e, bool):
            updated_data.append(not e)
        elif isinstance(e, int):
            updated_data.append(e + 1)
        elif isinstance(e, list):
            updated_data.append(e + e)
        elif isinstance(e, dict):
            e["newkey"] = None
            updated_data.append(e)
        else:
            continue

    file_out.write(json.dumps(updated_data))

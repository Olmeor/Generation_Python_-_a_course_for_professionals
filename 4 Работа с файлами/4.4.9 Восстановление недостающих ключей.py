# Восстановление недостающих ключей
# Вам доступен файл people.json, содержащий список JSON-объектов. Причем у различных объектов может быть различное
# количество ключей:
#
# [
#    {
#       "age": 33,
#       "country": "Lesotho",
#       "phone": "(927) 316-2249",
#       "family_status": "married",
#       "email": "neonatus@outlook.com"
#    },
#    {
#       "age": 25,
#       "country": "Guinea",
#       "name": "Dorey",
#       "children": "yes",
#       "email": "ismail@gmail.com",
#       "university": "Khalifa University",
#       "family_status": "married"
#    },
#    ...
# ]
# Напишите программу, которая добавляет в каждый JSON-объект из данного списка все недостающие ключи, присваивая этим
# ключам значение null. Ключ считается недостающим, если он присутствует в каком-либо другом объекте, но отсутствует в
# данном. Программа должна создать список с обновленными JSON-объектами и записать его в файл updated_people.json.

import json

with open('people.json') as file_in, open('updated_people.json', 'w', encoding='utf8') as file_out:
    data_json = json.load(file_in)
    pattern = dict.fromkeys(max(data_json, key=len).keys())
    updated_people = [pattern | d for d in data_json]
    file_out.write(json.dumps(updated_people, indent=3))

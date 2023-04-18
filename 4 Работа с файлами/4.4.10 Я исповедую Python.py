# Я исповедую Python, а ты?
# Вам доступен файл countries.json, содержащий список JSON-объектов c информацией о странах и исповедуемых в них
# религиях:
#
# [
#    {
#       "country": "Afghanistan",
#       "religion": "Islam"
#    },
#    {
#       "country": "Albania",
#       "religion": "Islam"
#    },
#    ...
# ]
# Каждый объект из этого списка содержит два атрибута:
#
# country — страна
# religion — исповедуемая религия
# Напишите программу, которая создает единственный JSON-объект, имеющий в качестве ключа название религии, а в качестве
# значения — список стран, в которых исповедуется данная религия. Полученный JSON-объект программа должна записать в
# файл religion.json.

import json

with open('countries.json') as file_in, open('religion.json', 'w', encoding='utf8') as file_out:
    data_json = json.load(file_in)
    religion = {}
    for country in data_json:
        religion.setdefault(country['religion'], []).append(country['country'])
    file_out.write(json.dumps(religion, indent=3))

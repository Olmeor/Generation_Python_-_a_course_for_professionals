# Спортивные площадки
# Вам доступен файл playgrounds.csv с информацией о спортивных площадках Москвы. В первом столбце записан тип площадки,
# во втором — административный округ, в третьем — название района, в четвертом — адрес:
#
# ObjectName;AdmArea;District;Address
# Парк, озелененная городская территория «Лианозовский парк культуры и отдыха»;Северо-Восточный административный округ;
# район Лианозово;Угличская улица, дом 13
# ...
# Напишите программу, создающую JSON-объект, ключом в котором является административный округ, а значением —
# JSON-объект, в котором, в свою очередь, ключом является название района, относящийся к этому административному
# округу, а значением — список адресов всех площадок в этом районе. Полученный JSON-объект программа должна записать в
# файл addresses.json.

import json
import csv

with open('playgrounds.csv', encoding='utf-8') as file_in, open('addresses.json', 'w', encoding='utf8') as file_out:
    data = csv.reader(file_in, delimiter=';', quotechar='"')
    addresses = {}
    next(data)
    for obj in data:
        addresses.setdefault(obj[1], {})
        addresses[obj[1]].setdefault(obj[2], [])
        addresses[obj[1]][obj[2]].append(obj[3])
    file_out.write(json.dumps(addresses, indent=3, ensure_ascii=False))

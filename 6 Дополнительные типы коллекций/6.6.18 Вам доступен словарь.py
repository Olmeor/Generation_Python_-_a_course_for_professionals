# Вам доступен словарь data с четным количеством элементов. Дополните приведенный ниже код, чтобы он вывел данный
# словарь, расположив его элементы по следующему правилу: первый, последний, второй, предпоследний, третий, и так далее.

from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

new_data = OrderedDict()
rule = False
for key in list(data):
    name, grade = data.popitem(last=rule)
    new_data[name] = grade
    rule = not rule

print(new_data)

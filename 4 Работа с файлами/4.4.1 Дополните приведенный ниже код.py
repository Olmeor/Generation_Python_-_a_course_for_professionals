# Дополните приведенный ниже код, чтобы он вывел содержимое словаря countries, расположив его элементы в
# лексикографическом порядке ключей, указав в качестве разделителя пар ключ-значение строку   -  (пробел дефис пробел),
# а в качестве отступов — три пробела.

import json

countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
             'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
             'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
             'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

json_countries = json.dumps(countries, indent=3, separators=(',', ' - '), sort_keys=True)

print(json_countries)

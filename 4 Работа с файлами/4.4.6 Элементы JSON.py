# Элементы JSON
# Напишите программу, которая принимает на вход описание одного объекта в формате JSON и выводит все пары ключ-значение
# этого объекта.

import json
import sys

json_data = sys.stdin.read()
data_json = json.loads(json_data)
for k, v in data_json.items():
    if type(v) == list:
        print(f"{k}: {', '.join(map(str, v))}")
    elif type(k) == int:
        print(f"{int(k)}: {v}")
    else:
        print(f"{k}: {v}")

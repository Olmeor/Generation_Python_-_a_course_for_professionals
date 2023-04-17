# Функция is_correct_json()
# Реализуйте функцию is_correct_json(), которая принимает один аргумент:
#
# string — произвольная строка
# Функция должна возвращать True, если строка string удовлетворяет формату JSON, или False в противном случае.

import json


def is_correct_json(string):
    try:
        data_json = json.loads(string)
        return True
    except:
        return False

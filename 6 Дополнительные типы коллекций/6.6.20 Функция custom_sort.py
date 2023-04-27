# Функция custom_sort() 🌶️
# Реализуйте функцию custom_sort(), которая принимает два аргумента в следующем порядке:
#
# ordered_dict — словарь OrderedDict
# by_values — булево значение, по умолчанию имеет значение False
# Функция должна сортировать словарь ordered_dict:
#
# по ключам, если by_values имеет значение False
# по значениям, если by_values имеет значение True

from collections import OrderedDict


def custom_sort(orderd_dict, by_values=False):
    for key, value in sorted(orderd_dict.items(), key=lambda x: x[by_values]):
        orderd_dict.move_to_end(key)

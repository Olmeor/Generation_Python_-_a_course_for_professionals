# Функция print_bar_chart()
# Реализуйте функцию print_bar_chart(), которая принимает два аргумента в следующем порядке:
#
# data — строка или список строк
# mark — одиночный символ
# Функция должна определять:
#
# сколько раз встречается каждый символ в строке, если data является строкой
# сколько раз встречается каждая строка в списке, если data является списком
# Затем функция должна выводить результат в виде столбчатой диаграммы, указывая каждый символ (строку) и его
# количество. Количество отображается как повторение символа mark соответствующее число раз, например, если mark='+',
# то количество, равное четырем, будет отображено как ++++. Символы (строки) в диаграмме должны быть расположены в
# порядке уменьшения количества, при равных количествах — в своем исходном порядке, каждая на отдельной строке, в
# следующем формате:
#
# <символ или строка> |<количество>

# put your python code here
from collections import Counter


def print_bar_chart(data, mark):
    if type(data) == str:
        data = list(data)
    counter = Counter(data)
    length = len(max(data, key=len))
    print(*[f"{k.ljust(length)} |{mark * v}" for k, v in sorted(counter.items(), key= lambda e: e[1], reverse=True)], sep="\n")

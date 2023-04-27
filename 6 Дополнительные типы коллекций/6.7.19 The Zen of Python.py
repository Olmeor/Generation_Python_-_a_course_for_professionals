# The Zen of Python
# Вам доступен текстовый файл pythonzen.txt, содержащий текст на английском языке:
#
# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# ...
# Напишите программу, которая определяет, сколько раз встречается каждая буква в этом тексте. Буквы и их количество
# должны выводиться в лексикографическом порядке, каждая на отдельной строке, в следующем формате:
#
# <буква>: <количество>

from collections import Counter

with open('pythonzen.txt', 'r', encoding='UTF-8') as file_in:
    pythonzen = file_in.read()
    text = [ch.lower() for ch in pythonzen if ch.isalpha()]
    counter_dct = dict(sorted(Counter(text).items(), key=lambda x: x))
    print(*[f"{key}: {value}" for key, value in counter_dct.items()], sep="\n")

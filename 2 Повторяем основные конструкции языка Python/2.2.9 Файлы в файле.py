# Файлы в файле 🌶️🌶️
# Вам доступен текстовый файл files.txt, содержащий информацию о файлах. Каждая строка файла содержит три значения,
# разделенные символом пробела — имя файла, его размер (целое число) и единицы измерения:
#
# cant-help-myself.mp3 7 MB
# keep-yourself-alive.mp3 6 MB
# bones.mp3 5 MB
# ...
# Напишите программу, которая группирует данные файлы по расширению, определяя общий объем файлов каждой группы, и
# выводит полученные группы файлов, указывая для каждой ее общий объем. Группы должны быть расположены в
# лексикографическом порядке названий расширений, файлы в группах — в лексикографическом порядке их имен.

with open('files.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

size = {
    'B': 1,
    'KB': 1024,
    'MB': 1024 ** 2,
    'GB': 1024 ** 3,
}


def get_size(num):
    if 1024 <= num < 1024 ** 2:
        return str(round(num / 1024)), 'KB'
    elif 1024 ** 2 <= num < 1024 ** 3:
        return str(round(num / 1024 ** 2)), 'MB'
    elif num >= 1024 ** 3:
        return str(round(num / 1024 ** 3)), 'GB'
    else:
        return str(round(num)), 'B'


lst = []
for line in lines:
    lst.append(line[:-1].replace('.', ' ').split())
lst.sort()
lst.sort(key=lambda e: e[1])

sz = 0
for i, v in enumerate(lst):
    if i + 1 < len(lst) and v[1] == lst[i + 1][1]:
        sz += int(v[2]) * size[v[3]]
        print(f"{v[0]}.{v[1]}")
    else:
        sz += int(v[2]) * size[v[3]]
        print(f"{v[0]}.{v[1]}")
        print("----------")
        a, b = get_size(sz)
        print(f"Summary: {a} {b}")
        sz = 0
        if i < len(lst) - 1:
            print()

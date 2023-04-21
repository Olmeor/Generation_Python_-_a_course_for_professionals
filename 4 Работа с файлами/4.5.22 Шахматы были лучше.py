# Шахматы были лучше 🌶️
# Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько JSON файлов, каждый из
# которых содержит информацию о каком-либо футболисте:
#
# {
#    "first_name": "Gary",
#    "last_name": "Cahill",
#    "team": "Chelsea",
#    "position": "Defender"
# }
# У футболиста имеются следующие атрибуты:
#
# first_name — имя
# last_name — фамилия
# team — название футбольного клуба
# position — игровая позиция
# Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов, выступающих
# за футбольный клуб Arsenal. Футболисты должны быть расположены в лексикографическом порядке имен, а при совпадении —
# в лексикографическом порядке фамилий, каждый на отдельной строке.

from zipfile import ZipFile
import json

with ZipFile('data.zip') as zip_file:
    info = zip_file.infolist()
    lst = []
    for file in info:
        file_name = file.filename[file.filename.rfind('/') + 1:]
        if not file.is_dir() and file_name[file_name.rfind('.') + 1:] == 'json':
            with zip_file.open(file.filename) as json_file:
                try:
                    data_json = json.loads(json_file.read().decode('utf-8'))
                    if data_json['team'] == 'Arsenal':
                        lst.append(f"{data_json['first_name']} {data_json['last_name']}")
                except:
                    continue
    print(*sorted(lst), sep="\n")

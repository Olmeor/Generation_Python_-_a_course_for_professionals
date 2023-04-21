# Избранные
# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит названия
# файлов из этого архива, которые были созданы или изменены позднее 2021-11-30 14:22:00. Названия файлов должны быть
# расположены в лексикографическом порядке, каждое на отдельной строке.

from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    lst = []
    dt = datetime.strptime('2021-11-30 14:22:00', '%Y-%m-%d %H:%M:%S')
    for file in info:
        if not file.is_dir() and datetime(*file.date_time) > dt:
            lst.append(file.filename[file.filename.rfind('/') + 1:])
    print(*sorted(lst), sep="\n")

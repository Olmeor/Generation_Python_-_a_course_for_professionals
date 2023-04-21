# Количество файлов
# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит единственное
# число — количество файлов в этом архиве.

from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    print(sum(not file.is_dir() for file in info))

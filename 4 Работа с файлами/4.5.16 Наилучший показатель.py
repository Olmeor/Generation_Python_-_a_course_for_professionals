# Наилучший показатель
# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит название
# файла из этого архива, который имеет наилучший показатель степени сжатия.

from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    lst = []
    for file in info:
        if not file.is_dir():
            file_name = file.filename[file.filename.rfind('/') + 1:]
            compress = file.compress_size / file.file_size
            lst.append((file_name, compress))
    print(min(lst, key=lambda x: x[1])[0])

# Структура архива 🌶️🌶️
# Вам доступен архив desktop.zip, содержащий различные папки и файлы. Напишите программу, которая выводит его файловую
# структуру и объем каждого файла.

from zipfile import ZipFile


def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f' {size} B'
    elif 1000 <= size < 1000000:
        return f' {round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f' {round(size / 1048576)} MB'
    else:
        return f' {round(size / 1073741824)} GB'


with ZipFile('desktop.zip') as zip_file:
    info = zip_file.infolist()
    for file in info:
        file_name = file.filename.strip('/').split('/')
        print('  ' * (len(file_name) - 1) + file_name[-1] + ('' if file.is_dir() else convert_bytes(file.file_size)))

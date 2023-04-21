# Функция extract_this()
# Реализуйте функцию extract_this(), которая принимает один или более аргументов в следующем порядке:
#
# zip_name — название zip архива, например, data.zip
# *args — переменное количество позиционных аргументов, каждый из которых является названием некоторого файла
# Функция должна извлекать файлы *args из архива zip_name в папку с программой. Если в функцию не передано ни одного
# названия файла для извлечения, то функция должна извлечь все файлы из архива.

from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        zip_file.extractall(members=args or None)

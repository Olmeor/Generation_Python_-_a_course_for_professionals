# Вам доступен набор различных файлов, названия которых представлены в списке file_names. Также вам доступен архив
# files.zip. Дополните приведенный ниже код, чтобы он добавил в архив files.zip только те файлы из списка file_names,
# объем которых не превышает 100 байт.

from zipfile import ZipFile
import os.path

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

with ZipFile('files.zip', mode='a') as zip_file:
    [zip_file.write(file) for file in file_names if os.path.getsize(file) <= 100]

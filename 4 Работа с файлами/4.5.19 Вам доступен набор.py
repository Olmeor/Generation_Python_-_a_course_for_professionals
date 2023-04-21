# Вам доступен набор различных файлов, названия которых представлены в списке file_names. Дополните приведенный ниже
# код, чтобы он создал архив files.zip и добавил в него все файлы из данного списка.

from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

with ZipFile('files.zip', mode='w') as zip_file:
    [zip_file.write(file) for file in file_names]

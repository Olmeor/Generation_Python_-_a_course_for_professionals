# Форматированный вывод
# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит названия
# всех файлов из этого архива в лексикографическом порядке, указывая для каждого его дату изменения, а также объем до и
# после сжатия, в следующем формате:
#
# <название файла>
#   Дата модификации файла: <дата изменения>
#   Объем исходного файла: <объем до сжатия> байт(а)
#   Объем сжатого файла: <объем после сжатия> байт(а)
# Между данными о двух файлах должна располагаться пустая строка.

from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    dct = {}
    for file in info:
        if not file.is_dir():
            filename = file.filename[file.filename.rfind('/') + 1:]
            value = [datetime(*file.date_time), file.file_size, file.compress_size]
            dct[filename] = value

for filename in sorted(dct.keys()):
    print(f"""{filename}
  Дата модификации файла: {dct[filename][0]}
  Объем исходного файла: {dct[filename][1]} байт(а)
  Объем сжатого файла: {dct[filename][2]} байт(а)\n""")

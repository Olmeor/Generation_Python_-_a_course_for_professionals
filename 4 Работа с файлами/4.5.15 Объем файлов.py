# Объем файлов
# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит суммарный
# объем файлов этого архива в сжатом и не сжатом видах в байтах, в следующем формате:
#
# Объем исходных файлов: <объем до сжатия> байт(а)
# Объем сжатых файлов: <объем после сжатия> байт(а)

from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    file_size = []
    compress_size = []
    for file in info:
        if not file.is_dir():
            file_size.append(file.file_size)
            compress_size.append(file.compress_size)
    print(f"Объем исходных файлов: {sum(file_size)} байт(а)", f"Объем сжатых файлов: {sum(compress_size)} байт(а)", sep="\n")

# Функция csv_columns()
# Реализуйте функцию csv_columns(), которая принимает один аргумент:
#
# filename — название csv файла, например, data.csv
# Функция должна возвращать словарь, в котором ключом является название столбца файла filename, а значением — список
# элементов этого столбца.

# import csv
#
# def csv_columns(filename):
#     with open(filename, encoding='utf-8') as file:
#         data = csv.reader(file)
#         return {key: value for key, *value in zip(*data)}

def csv_columns(filename):
    with open(filename, encoding='utf-8') as file:
        data = file.read()
        table = [row.split(',') for row in data.splitlines()]
        dct = {}
        for row in table[1:]:
            for i, col in enumerate(table[0]):
                dct.setdefault(col, []).append(row[i])
        return dct

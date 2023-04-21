# Ты не пройдешь
# Реализуйте функцию filter_dump(), которая принимает три аргумента в следующем порядке:
#
# filename — название pickle файла, например, data.pkl
# objects — список произвольных объектов
# typename — тип данных
# Функция должна создавать pickle файл с названием filename, который содержит сериализованный список только тех
# объектов из списка objects, тип которых равен typename.

import pickle

def filter_dump(filename, objects, typename):
    with open(filename, 'wb') as file:
        lst = [obj for obj in objects if type(obj) == typename]
        pickle.dump(lst, file)

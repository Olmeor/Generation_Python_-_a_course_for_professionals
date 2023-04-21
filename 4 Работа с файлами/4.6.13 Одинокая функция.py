# Одинокая функция
# Дан pickle файл, содержащий единственную сериализованную функцию. Напишите программу, которая вызывает данную функцию
# с заданными аргументами и выводит возвращаемое значение функции.

import pickle
import sys

name, *args = [line.strip() for line in sys.stdin]

with open(name, 'rb') as file_in:
    new_func = pickle.load(file_in)

print(new_func(*args))

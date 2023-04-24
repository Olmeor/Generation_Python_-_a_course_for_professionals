# Дополните приведенный ниже код, чтобы он создал именованный кортеж Fruit с полями name, color и vitamins.

from collections import namedtuple

Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])

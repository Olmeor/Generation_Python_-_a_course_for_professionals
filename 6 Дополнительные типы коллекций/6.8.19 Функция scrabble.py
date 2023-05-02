# Функция scrabble()
# Реализуйте функцию scrabble(), которая принимает два аргумента в следующем порядке:
#
# symbols — набор символов
# word — слово
# Функция должна возвращать True, если из набора символов symbols можно составить слово word, или False в противном
# случае.

from collections import Counter


def scrabble(symbols, word):
    return Counter(symbols.lower()) >= Counter(word.lower())

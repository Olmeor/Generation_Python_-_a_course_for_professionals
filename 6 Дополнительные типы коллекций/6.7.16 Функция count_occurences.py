# Функция count_occurences()
# Реализуйте функцию count_occurences(), которая принимает два аргумента в следующем порядке:
#
# word — слово
# words — последовательность слов, разделенных пробелом
# Функция должна определять, сколько раз слово word встречается в последовательности words, и возвращать полученный
# результат.

from collections import Counter


def count_occurences(word, words):
    words_counter = Counter(words.lower().split())
    return words_counter[word.lower()]

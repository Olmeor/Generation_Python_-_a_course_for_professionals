# Функция spell()
# Реализуйте функцию spell(), которая принимает произвольное количество позиционных аргументов-слов и возвращает
# словарь, ключи которого — первые буквы слов, а значения — максимальные длины слов на эту букву.

def spell(*args):
    result = {}
    for word in args:
        if result.get(word[0].lower(), 0) < len(word):
            result[word[0].lower()] = len(word)
    return result

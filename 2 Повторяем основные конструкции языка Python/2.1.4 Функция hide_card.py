# Функция hide_card()
# Реализуйте функцию hide_card(), которая принимает один аргумент:
#
# card_number — строка, представляющая собой корректный номер банковской карты из 16 цифр, между которыми могут
# присутствовать символы пробела
# Функция должна заменять первые 12 цифр в строке card_number на символ * и возвращать полученный результат. Если между
# цифрами в номере имелись символы пробела, их следует удалить.

def hide_card(card):
    return '*' * 12 + card.replace(' ', '')[-4:]

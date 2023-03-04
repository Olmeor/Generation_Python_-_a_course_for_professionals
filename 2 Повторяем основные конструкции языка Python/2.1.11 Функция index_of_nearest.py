# Функция index_of_nearest()
# Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:
#
# numbers — список целых чисел
# number — целое число
# Функция должна находить в списке numbers ближайшее по значению число к числу number и возвращать его индекс. Если
# список numbers пуст, функция должна вернуть число −1.

def index_of_nearest(numbers, number):
    if len(numbers) == 0:
        return -1
    lst = list(map(lambda x: abs(x - number), numbers))
    return lst.index(min(lst))

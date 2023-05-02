# Вам доступна переменная data, содержащая Counter словарь. Дополните приведенный ниже код, чтобы он добавил этому
# словарю два атрибута:
#
# min_values() — функция, которая возвращает список элементов, имеющих наименьшее значение
# max_values() — функция, которая возвращает список элементов, имеющих наибольшее значение
# Обе функции не должны принимать никаких аргументов.

from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.__dict__['min_values'] = lambda: list(filter(lambda e: e[1] == data.most_common()[-1][1], data.items()))
data.__dict__['max_values'] = lambda: list(filter(lambda e: e[1] == data.most_common()[0][1], data.items()))

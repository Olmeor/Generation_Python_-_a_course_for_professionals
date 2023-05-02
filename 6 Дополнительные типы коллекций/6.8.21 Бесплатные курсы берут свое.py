# Бесплатные курсы берут свое 😢
# Для дополнительного заработка Тимур решил заняться продажей овощей. У него имеются данные о продажах за год,
# разделенные на четыре файла по кварталам: quarter1.csv, quarter2.csv, quarter3.csv и quarter4.csv. В каждом файле в
# первом столбце указывается название продукта, а в последующих — количество проданного продукта в килограммах за
# определенный месяц:
#
# продукт,январь,февраль,март
# Картофель,39,61,3
# Дайкон,51,96,83
# ...
# Также присутствует файл prices.json, содержащий словарь, в котором ключом является название продукта, а значением —
# цена за килограмм в рублях:
#
# {
#    "Картофель": 53,
#    "Дайкон": 55,
# ...
# }
# Напишите программу, которая выводит единственное число — сумму, заработанную Тимуром за год на продаже овощей.

from collections import Counter
import csv
import json

with open('prices.json', encoding='utf-8') as file_in:
    prices = json.load(file_in)

products = Counter()
for i in range(1, 5):
    with open(f'quarter{i}.csv', encoding='utf-8') as file_in:
        data = csv.reader(file_in)
        next(data)
        counter = Counter(dict(map(lambda e: (e[0], sum(map(int, e[1:])) * prices[e[0]]), list(data))))
        products += counter

print(products.total())

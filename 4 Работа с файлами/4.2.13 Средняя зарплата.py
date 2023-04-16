# Средняя зарплата
# Вам доступен файл salary_data.csv, который содержит анонимную информацию о зарплатах сотрудников в различных
# компаниях. В первом столбце записано название компании, а во втором — зарплата очередного сотрудника:
#
# company_name;salary
# Atos;135000
# ХайТэк;24400
# Philax;128600
# Инлайн Груп;43900
# IBS;70600
# Oracle;131600
# Atos;91000
# ...
#
# Напишите программу, которая упорядочивает компании по возрастанию средней зарплаты ее сотрудников и выводит их
# названия, каждое на отдельной строке. Если две компании имеют одинаковые средние зарплаты, они должны быть
# расположены в лексикографическом порядке их названий.

import csv

with open('salary_data.csv', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=';')
    next(data)
    dct = {}
    [dct.setdefault(company_name, []).append(int(salary)) for company_name, salary in data]
    for company_name, salary in dct.items():
        dct[company_name] = sum(salary) / len(salary)
    dct = dict(sorted(dct.items(), key=lambda e: e[1]))
    print(*[company_name for company_name, s in dct.items()], sep='\n')

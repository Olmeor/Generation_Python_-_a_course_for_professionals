# Популярные домены
# Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса. В первом
# столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты:
#
# first_name,surname,email
# John,Wilson,johnwilson@outlook.com
# Mary,Wilson,marywilson@list.ru
# ...
# Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:
#
# domain,count
# rambler.ru,24
# iCloud.com,29
# ...
# где в первом столбце записано название почтового домена, а во втором — количество пользователей, использующих данный
# домен. Домены в файле должны быть расположены в порядке возрастания количества их использований, при совпадении
# количества использований — в лексикографическом порядке.

import csv

dct = {}
with open('data.csv', encoding='utf-8') as file_in:
    data = csv.reader(file_in)
    next(data)
    for row in data:
        domain = row[2][row[2].index('@') + 1:]
        dct[domain] = dct.get(domain, 0) + 1
    dct = dict(sorted(dct.items(), key=lambda e: (e[1], e[0])))

data = dct.items()
columns = ['domain', 'count']

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file_out:
    writer = csv.writer(file_out)
    writer.writerow(columns)
    for row in data:
        writer.writerow(row)

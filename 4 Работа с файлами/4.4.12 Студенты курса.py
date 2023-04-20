# Студенты курса
# Вам доступен файл students.json, содержащий список JSON-объектов, которые представляют данные о студентах некоторого
# курса:
#
# [
#    {
#       "name": "Holly-Anne",
#       "city": "Abilene",
#       "age": 29,
#       "progress": 85,
#       "phone": "(802) 983-9126"
#    },
#    ...
# ]
# Под «студентом» мы будем подразумевать один JSON-объект из этого списка. У студента имеются следующие атрибуты:
#
# name — имя
# city — город проживания
# age — возраст
# progress — прогресс по курсу в процентах
# phone— контактный номер
# Напишите программу, которая определяет студентов, удовлетворяющих следующим условиям:
#
# возраст 18 лет или более
# прогресс по курсу 75% или более
# Программа должна создать файл data.csv с двумя столбцами — name (имя) и phone (номер), и записать в него данные
# выбранных студентов, расположив их в лексикографическом порядке имён. В качестве разделителя в файле data.csv должна
# быть использована запятая.

import json
import csv

with open('students.json', encoding='UTF-8') as file_in, open('data.csv', 'w', encoding='UTF-8', newline='') as file_out:
    students = json.load(file_in)
    students = sorted(students, key=lambda s: s['name'])
    data = csv.writer(file_out)
    data.writerow(['name', 'phone'])
    for s in students:
        if s['age'] >= 18 and s['progress'] >= 75:
            data.writerow([s['name'], s['phone']])

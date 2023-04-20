# Результаты экзамена 🌶️
# Вам доступен файл exam_results.csv, который содержит информацию о прошедшем экзамене в некотором учебном заведении. В
# первом столбце записано имя студента, во втором — фамилия, в третьем — оценка за экзамен, в четвертом — дата и время
# сдачи в формате YYYY-MM-DD HH:MM:SS, в пятом — адрес электронной почты:
#
# name,surname,score,date_and_time,email
# Jayson,Edwards,2,2021-11-10 10:00:00,sonnen@yahoo.com
# April,Sims,3,2021-11-01 11:00:00,retoh@outlook.com
# ...
# Каждый студент имеет право пересдать экзамен два раза, поэтому он может встречаться в исходном файле до трёх раз с
# различной оценкой и различными датой и временем сдачи.
#
# Напишите программу, которая для каждого студента определяет его максимальную оценку, а также дату и время ее
# получения. Программа должна создать список словарей, каждый из которых содержит следующие пары ключ-значение:
#
# name — имя студента
# surname — фамилия студента
# best_score — максимальная оценка за экзамен
# date_and_time — дата и время получения максимальной оценки в исходном формате
# email — адрес электронной почты
# Полученный список программа должна записать в файл best_scores.json, причем словари в списке должны быть расположены
# в лексикографическом порядке названий электронных почт.

import json
import csv
from datetime import datetime


def get_dt(string):
    return datetime.strptime(string, '%Y-%m-%d %H:%M:%S')


with open('exam_results.csv', encoding='utf-8') as file_in, open('best_scores.json', 'w', encoding='utf8') as file_out:
    res = csv.reader(file_in)
    columns = next(res)
    columns[2] = 'best_score'
    scores = {}
    for row in res:
        eml = row[-1]
        row[2] = int(row[2])
        if any([eml in scores and scores[eml][2] < row[2], eml in scores and scores[eml][2] == row[2] and get_dt(scores[eml][3]) < get_dt(row[3]), eml not in scores]):
            scores[eml] = row

    scores = sorted(scores.values(), key=lambda e: e[-1])
    best_scores = [dict(zip(columns, student)) for student in scores]
    file_out.write(json.dumps(best_scores, indent=3, ensure_ascii=False))

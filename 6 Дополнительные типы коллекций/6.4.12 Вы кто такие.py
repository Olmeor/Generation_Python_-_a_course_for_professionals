# Вы кто такие? Я вас не звал
# У Тимура имеется немало друзей из других городов или стран, которые часто приезжают к нему в гости с целью увидеться
# и развлечься. Чтобы не забыть ни об одной встрече, Тимур записывает имена и фамилии друзей в csv файл, дополнительно
# указывая для каждого дату и время встречи. Вам доступен этот файл, имеющий название meetings.csv, в котором в первом
# столбце записана фамилия, во втором — имя, в третьем — дата в формате DD.MM.YYYY , в четвертом — время в формате
# HH:MM:
#
# surname,name,meeting_date,meeting_time
# Харисов,Артур,15.07.2022,17:00
# Геор,Гагиев,14.12.2022,18:00
# ...
# Напишите программу, которая выводит фамилии и имена друзей Тимура, предварительно отсортировав их по дате и времени
# встречи от самой ранней до самой поздней. Фамилии и имена должны быть расположены каждые на отдельной строке.

from collections import namedtuple
import csv
from datetime import datetime


def sort_dt(d, t):
    return datetime.strptime(f"{d} {t}", "%d.%m.%Y %H:%M")


with open('meetings.csv', encoding='UTF-8') as file_in:
    data_meetings = csv.reader(file_in)
    Meetings = namedtuple('Meetings', next(data_meetings))
    meetings = [Meetings._make(meeting) for meeting in data_meetings]
    meetings.sort(key=lambda friend: sort_dt(friend.meeting_date, friend.meeting_time))
    print(*[f"{friend.surname} {friend.name}" for friend in meetings], sep="\n")

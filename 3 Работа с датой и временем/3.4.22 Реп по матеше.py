# Реп по матеше
# Репетитор по математике проводит занятия по 45 минут с перерывами по 10 минут. Репетитор обозначает время начала
# рабочего дня и время окончания рабочего дня. Напишите программу, которая генерирует и выводит расписание занятий.

from datetime import datetime, timedelta

pattern = '%H:%M'
start = datetime.strptime(input(), pattern)
end = datetime.strptime(input(), pattern)
lesson = timedelta(minutes=45)
turn = timedelta(minutes=10)
while start <= end - lesson:
    print(datetime.strftime(start, pattern), end=' - ')
    start += lesson
    print(datetime.strftime(start, pattern))
    start += turn

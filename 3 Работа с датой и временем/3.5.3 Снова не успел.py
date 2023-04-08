# Снова не успел
# Дан режим работы магазина:
#
# Понедельник	9:00 - 21:00
# Вторник	9:00 - 21:00
# Среда	9:00 - 21:00
# Четверг	9:00 - 21:00
# Пятница	9:00 - 21:00
# Суббота	10:00 - 18:00
# Воскресенье	10:00 - 18:00
# Напишите программу, которая принимает на вход текущие дату и время и определяет количество минут, оставшееся до
# закрытия магазина.

from datetime import datetime, timedelta

dt = datetime.strptime(input(), '%d.%m.%Y %H:%M')
td = timedelta(hours=dt.hour, minutes=dt.minute)

if dt.weekday() < 5 and timedelta(hours=9) <= td < timedelta(hours=21):
    print(int((timedelta(hours=21) - td).total_seconds() // 60))
elif dt.weekday() > 4 and timedelta(hours=10) <= td < timedelta(hours=18):
    print(int((timedelta(hours=18) - td).total_seconds() // 60))
else:
    print('Магазин не работает')

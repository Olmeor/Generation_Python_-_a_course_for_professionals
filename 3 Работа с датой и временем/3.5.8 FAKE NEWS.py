# FAKE NEWS 🌶️
# Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00. Напишите программу, которая принимает
# на вход текущие дату и время и определяет, сколько времени осталось до выхода курса.

from datetime import datetime


def choose_plural(amount, declensions):
    plural_dict = {'d': ("день", "дня", "дней"), 'h': ("час", "часа", "часов"), 'm': ("минута", "минуты", "минут")}
    end_num = 2
    if amount % 10 == 1 and amount % 100 != 11:
        end_num = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        end_num = 1
    return f"{amount} {plural_dict[declensions][end_num]}"


dt = datetime.strptime(input(), '%d.%m.%Y %H:%M')
event = datetime.strptime('08.11.2022 12:00', '%d.%m.%Y %H:%M')
if dt >= event:
    print('Курс уже вышел!')
else:
    td = event - dt
    d = td.days
    h = td.seconds // 3600
    m = (td.seconds // 60) % 60
    if d == 0 and h == 0:
        print(f"До выхода курса осталось: {choose_plural(m, 'm')}")
    elif d == 0:
        if m == 0:
            print(f"До выхода курса осталось: {choose_plural(h, 'h')}")
        else:
            print(f"До выхода курса осталось: {choose_plural(h, 'h')} и {choose_plural(m, 'm')}")
    elif h == 0:
        print(f"До выхода курса осталось: {choose_plural(d, 'd')}")
    else:
        print(f"До выхода курса осталось: {choose_plural(d, 'd')} и {choose_plural(h, 'h')}")

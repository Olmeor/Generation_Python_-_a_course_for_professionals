# Корпоративная почта 🌶️
# В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, которая формируется как <имя-фамилия>@beegeek.bzz,
# например, timyr-guev@beegeek.bzz. При таком подходе существует проблема тёзок. Для решения такой проблемы было решено
# приписывать справа номер.
#
# Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера), второй — timyr-guev1@beegeek.bzz, третий —
# timyr-guev2@beegeek.bzz, и так далее.
#
# Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых сотрудников в заранее подготовленном виде
# (латиницей с символом - между ними). Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы.

existings = [input() for _ in range(int(input()))]
news = [input() for _ in range(int(input()))]

for i, v in enumerate(news):
    j = 0
    while True:
        if v + ("" if j == 0 else str(j)) + "@beegeek.bzz" in existings:
            j += 1
        else:
            s = v + ("" if j == 0 else str(j)) + "@beegeek.bzz"
            existings.append(s)
            print(s)
            break

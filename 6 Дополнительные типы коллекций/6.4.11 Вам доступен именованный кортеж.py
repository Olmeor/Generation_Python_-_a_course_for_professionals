# Вам доступен именованный кортеж User, который содержит данные о пользователе некоторого ресурса. Первым элементом
# именованного кортежа является имя пользователя, вторым — фамилия, третьим — адрес электронной почты, четвертым —
# статус оформленной подписки. Также доступен список users, содержащий эти кортежи.
#
# Дополните приведенный ниже код, чтобы он вывел данные о каждом пользователе из этого списка, предварительно
# отсортировав их по статусу подписки от дорогой к дешевой, а при совпадении статусов — в лексикографическом порядке
# адресов электронных почт. Данные о каждом пользователе должны быть указаны в следующем формате:
#
# <имя> <фамилия>
#   Email: <адрес электронной почты>
#   Plan: <статус подписки>
# Между данными двух разных пользователей должна располагаться пустая строка.

from collections import namedtuple


def sort_plan(plan):
    return {'Gold': 0, 'Silver': 1, 'Bronze': 2, 'Basic': 3}[plan]


User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

users.sort(key=lambda user: (sort_plan(user.plan), user.email))
for user in users:
    print(f"{user.name} {user.surname}", f"  Email: {user.email}", f"  Plan: {user.plan}", "", sep="\n")

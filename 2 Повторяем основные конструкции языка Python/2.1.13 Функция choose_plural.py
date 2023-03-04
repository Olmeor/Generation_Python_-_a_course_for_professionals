# Функция choose_plural() 🌶️🌶️
# Реализуйте функцию choose_plural(), которая принимает два аргумента в следующем порядке:
#
# amount — натуральное число, количество
# declensions — кортеж из трех вариантов склонения существительного
# Функция должна возвращать строку, полученную путем объединения подходящего существительного из кортежа declensions и
# количества amount, в следующем формате:
#
# <количество> <существительное>

def choose_plural(amount, declensions):
    end_num = 2
    if amount % 10 == 1 and amount % 100 != 11:
        end_num = 0
    elif 2 <= amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        end_num = 1
    return f"{amount} {declensions[end_num]}"

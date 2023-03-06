# Схожие слова
# Напишите программу, которая находит все схожие слова для заданного слова. Слова называются схожими, если имеют
# одинаковое количество и расположение гласных букв. При этом сами гласные могут различаться.

vov = 'а, у, о, ы, и, э, я, ю, ё, е'.replace(', ', '')

def replace_char(word):
    res = ""
    for c in word:
        if c in vov:
            res += '1'
        else:
            res += '0'
    return res[:res.rfind('1') + 1]


s = replace_char(input())
lst = [input() for _ in range(int(input()))]
dct = {}
for w in lst:
    dct[w] = replace_char(w)

for k, v in dct.items():
    if s == v:
        print(k)

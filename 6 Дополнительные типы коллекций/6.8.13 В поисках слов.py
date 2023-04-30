# В поисках слов 😋
# Дана последовательность слов. Напишите программу, которая выводит наименее часто встречаемое слово в этой
# последовательности. Если таких слов несколько, программа должна вывести их все.

# put your python code here
from collections import Counter

words = input().lower().split()
counter = Counter(words)
min_words = sorted(map(lambda e: e[0], filter(lambda e: e[1] == counter.most_common()[-1][1], counter.items())))
print(', '.join(min_words))

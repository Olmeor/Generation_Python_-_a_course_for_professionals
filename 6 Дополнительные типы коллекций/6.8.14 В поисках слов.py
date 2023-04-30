# В поисках слов 🥳
# Дана последовательность слов. Напишите программу, которая выводит наиболее часто встречаемое слово в этой
# последовательности. Если таких слов несколько, программа должна вывести то, которое больше в лексикографическом
# сравнении.

# put your python code here
from collections import Counter

words = input().lower().split()
counter = Counter(words)
min_words = max(map(lambda e: e[0], filter(lambda e: e[1] == counter.most_common()[0][1], counter.items())))
print(min_words)

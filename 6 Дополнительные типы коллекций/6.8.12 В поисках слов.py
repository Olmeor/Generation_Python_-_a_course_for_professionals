# В поисках слов 😇
# Дана последовательность слов. Напишите программу, которая выводит наиболее часто встречаемое слово в этой
# последовательности.

# put your python code here
from collections import Counter

words = Counter(input().lower().split())
print(words.most_common()[0][0])

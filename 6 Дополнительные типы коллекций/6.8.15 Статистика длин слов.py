# Статистика длин слов
# Дана последовательность слов. Напишите программу, которая группирует слова из этой последовательности по их длине и
# определяет количество слов в каждой полученной группе.

# put your python code here
from collections import Counter

words = map(lambda x: len(x), input().split())
counter = sorted(Counter(words).items(), key=lambda e: e[1])
print(*[f"Слов длины {k}: {v}" for k, v in counter], sep="\n")

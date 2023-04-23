# put your python code here
import string

chrs, text = input(), input()
dct = dict(zip(string.ascii_lowercase, chrs))
# print(*[dct[c] if c in dct else c for c in text.lower()], sep="")  # Вариант 1
print(text.lower().translate(text.lower().maketrans(dct)))  # Вариант 2

# Без комментариев
# Дан блок кода на языке Python. Напишите программу, которая удаляет все строки в данном коде, которые содержат в себе
# только комментарии. Если в строке помимо комментария имеется что-то еще, то такую строку учитывать не нужно.

# put your python code here
import sys

for line in sys.stdin:
    if line.lstrip().startswith('#'):
        continue
    else:
        sys.stdout.write(line)

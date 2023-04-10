# Это точно Python?
# Дана последовательность дат. Напишите программу, которая определяет, в каком порядке расположены даты в данной
# последовательности.

# put your python code here
import sys
from datetime import datetime

data = [datetime.strptime(line.strip('\n'), '%d.%m.%Y') for line in sys.stdin]
if data == sorted(list(set(data))):
    print('ASC')
elif data == sorted(list(set(data)), reverse=True):
    print('DESC')
else:
    print('MIX')

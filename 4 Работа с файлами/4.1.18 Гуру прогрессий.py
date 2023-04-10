# Гуру прогрессий
# Дана последовательность целых чисел. Напишите программу, которая определяет, является ли данная последовательность
# прогрессией, и если да, то определяет её вид.

# put your python code here
import sys

data = [int(line.strip()) for line in sys.stdin]
delta_a = data[1] - data[0]
delta_g = int(data[1] / data[0])
data_a = []
data_g = []
for i in range(len(data)):
    data_a.append(data[0] + delta_a * i)
    data_g.append(data[0] * delta_g ** i)

if len(data) != len(set(data)):
    print('Не прогрессия')
elif data == data_a:
    print('Арифметическая прогрессия')
elif data == data_g:
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')

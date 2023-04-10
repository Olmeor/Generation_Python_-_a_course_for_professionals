# Лемма о трёх носках
# Анри и Дима, имея на руках ящик с бесконечным количеством носков, решили сыграть в игру. Ребята по очереди достают из
# ящика произвольное количество носков, и после неопределенного числа ходов игра заканчивается. Если тот, кто сделал
# последний ход, вытащил четное количество носков — он побеждает, в противном случае проигрывает.
#
# Напишите программу, которая определяет победителя в данной игре, если первый ход делает Анри.

# put your python code here
import sys

arr = [int(line.strip('\n').strip(' — ')) for line in sys.stdin]
print('Анри' if (len(arr)) % 2 != 0 and arr[-1] % 2 == 0 or (len(arr)) % 2 == 0 and arr[-1] % 2 != 0 else 'Дима')

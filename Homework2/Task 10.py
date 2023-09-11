"""Задача 10: На столе лежат n монеток. Некоторые из них лежат 
вверх решкой, а некоторые – гербом. Определите минимальное число 
монеток, которые нужно перевернуть, чтобы все монетки были повернуты
вверх одной и той же стороной. Выведите минимальное количество монет,
которые нужно перевернуть"""
import random
count = [int(i) for i in input('Введите 1 или 0 через пробел: ').split()]
numb_heads1 = 0
numb_tails0 = 0
for i in range(0, len(count)):
    if count[i] == 1:
        numb_heads1 +=1
    if count[i] == 0:
        numb_tails0 +=1
min = 0
if numb_heads1 > numb_tails0:
    min = numb_tails0
if numb_heads1 < numb_tails0:
    min = numb_heads1
print(min)
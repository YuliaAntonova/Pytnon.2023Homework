"""Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки"""
import random
bush = int(input("Введите кол-во кустов: "))
small_fruit = [random.randint(1, 10) for _ in range(bush)] # 1-что мы добавляем(рандомное число), 2- идя по генерации последовательности 10 раз
print(small_fruit)
ai_list=[] #новый пустой список
for bush1 in range(bush): # выдать все значения из диапазона bush 
    bush2 = (bush1 - 1) % bush
    bush3 = (bush1 + 1) % bush
    sum_bush = small_fruit[bush1] + small_fruit[bush2] + small_fruit[bush3]
    ai_list.append(sum_bush)
print(max(ai_list))


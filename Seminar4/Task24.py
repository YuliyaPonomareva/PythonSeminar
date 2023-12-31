# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число
# ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из
# управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input("Введите количество кустов на грядке: "))
# garden_bed = range(1, n + 1)
garden_bed = []

for j in range(n):
    bush = int(input())
    garden_bed.append(bush)
print('Урожайность кустов: ')
print(garden_bed)
# [5, 2, 9, 4, 3, 8, 0] - количество ягод с куста
max_berries = 0
for i in range(len(garden_bed)):
    if i == 0:
        berries = garden_bed[n-1] + garden_bed[i] + garden_bed[i + 1]
    elif i == n-1:
        berries = garden_bed[i-1] + garden_bed[i] + garden_bed[0]
    else:
        berries = garden_bed[i - 1] + garden_bed[i] + garden_bed[i + 1]
    print(berries, end=' ')
    print()
    if berries > max_berries:
        max_berries = berries
print()
print(f'За один заход модуль может собрать максимальное число ягод, равное {max_berries}.')

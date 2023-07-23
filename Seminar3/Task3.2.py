"""
Требуется найти в массиве list_1 самый близкий по величине элемент
к заданному числу k и вывести его.
"""

list_1 = [1, 12, 6, 7, 8, 15]
k = 11
# 5
list2 =[]
for i in range(len(list_1)):
    list2.append((abs(k - list_1[i]), list_1[i]))
res = min(list2)
print(res[1])

# Эталонное решение
# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)
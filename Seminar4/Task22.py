# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

res1 = set()
res2 = set()

for i in range(n):
    p = int(input())
    res1.add(p)
print()
for j in range(m):
    b = int(input())
    res2.add(b)
print(res1)
print(res2)

res = res1.intersection(res2)
print(res)

while len(res) != 0:
    print(min(res), end=' ')
    res.discard(min(res))
print(" - числа, которые встречаются в обоих множествах.")


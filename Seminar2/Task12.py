"""
Задача 12: Петя и Катя – брат и сестра.
Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""
# Натуральные числа - это числа, которые используются при подсчете, т.е. положительные и не равны 0
input("Задумай два числа от 1 до 1001. Задумал? Нажми ENTER.")
s = int(input('Сумма этих чисел = '))
p = int(input('Произведение этих чисел = '))
x = 1
for i in range(s):
    y = s - x
    if x <= y and x * y == p:
        print(f'x = {x}, y = {y}')
    x += 1

# x = int((S - ((S) ** 2 - 4 * P) ** 0.5) / 2)
# y = int((S + ((S) ** 2 - 4 * P) ** 0.5) / 2)
# print(f'x = {x}, y = {y}')
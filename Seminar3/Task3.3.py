"""В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.

А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
либо только русские буквы."""


k = 'ноутбук'
print(k)
# 12

a1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
a2 = ['D', 'G']
a3 = ['B', 'C', 'M', 'P']
a4 = ['F', 'H', 'V', 'W', 'Y']
a5 = ['K']
a8 = ['J', 'X']
a10 = ['Q', 'Z']

r1 =['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
r2 = ['Д', 'К', 'Л', 'М', 'П', 'У']
r3 = ['Б', 'Г', 'Ё', 'Ь', 'Я']
r4 = ['Й', 'Ы']
r5 = ['Ж', 'З', 'Х', 'Ц', 'Ч']
r8 = ['Ш', 'Э', 'Ю']
r10 = ['Ф', 'Щ', 'Ъ']
l = k.upper()
print(l)
s = 0
for i in l:
    print(i)
    if i in a1 or i in r1:
        s += 1
    elif i in a2 or i in r2:
        s += 2
    elif i in a3 or i in r3:
        s += 3
    elif i in a4 or i in r4:
        s += 4
    elif i in a5 or i in r5:
        s += 5
    elif i in a8 or i in r8:
        s += 8
    elif i in a10 or i in r10:
        s += 10
print(s)

# Эталонное решение
# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)






















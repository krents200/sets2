﻿print("введите до 100 000 чисел в первый список")
print('Когда чисел будет достаточно, напишите "нет"')
N = set()
k = str()
while k != 'нет' and len(N)!=100000:
    print('Введите число:')
    N.add(int(input()))
    print('Продолжить?')
    k = input()
print("введите до 100 000 чисел во второй список")
print('Когда чисел будет достаточно, напишите "нет"')
k  = 'да' #Ну нужно же как-то обнулить эту переменную!
E = set()
while k != 'нет' and len(E)!=100000:
    print('Введите число:')
    E.add(int(input()))
    print('Продолжить?')
    k = input()
print('Итог объединения:')
print(N and E)
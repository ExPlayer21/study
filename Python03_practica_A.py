from random import randint

a = [randint(-10, 10) for x in range(20)]

a.sort(reverse=False)

print('Массив А (все числа):')

print(a)

a1=[i for i in a if i<0]

print('Массив B(все четные отрицательные числа):')

print(a1)
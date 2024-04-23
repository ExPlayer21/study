from sympy import isprime

from random import randint

a = [randint(0, 100) for x in range(20)]

a.sort(reverse=False)

print('Массив А (все числа от 0 до 100):')

print(a)

a1=[i for i in a if isprime(i)]

print('Массив B(все простые числа):')

print(a1)
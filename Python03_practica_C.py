#Откровенно говоря, не уверен, что код работает правильно, т.к. 
#пример логической функции которая определяет, является ли 
#переданное ей число числом Фибоначчи взял из интернета

from random import randint

a = [randint(0, 100) for x in range(30)]

a.sort(reverse=False)

print('Массив А (все числа от 0 до 10):')

print(a)

def is_fibonacci(n):
    if n == 0:
        return True
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

fibonacci_numbers = [num for num in a if is_fibonacci(num)]
print("Числа Фибоначчи из массива случайных чисел:", fibonacci_numbers)
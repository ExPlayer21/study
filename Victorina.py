from colorama import Fore, Back, Style
from colorama import init
import os
init()
 
print(Style.BRIGHT) # цвет в терминале
ls = [
    ("Верно ли утверждение: два плюс два умножить на два = 8", "нет"),
    ("Благодаря грибам-плесени был создан Пенициллин?", "да"),
    ("Дональд Трамп снимался в фильме Один дома 2?", "да"),
    ("Гарри Поттера играл Питер Паркер?", "нет"),
    ("Колокол часов Вестминстерского дворца в Лондоне называется Джордж Тауер?", "нет"),
    ("Telegramm это язык программирования?", "нет"),
    ("В 1кг 1000г, верно?", "да"),
    ("Андуриан это страна?", "нет"),
    ("В одной минуте 60 секунд?", "да"),
    ("В одной секунде 60 миллисекунд?", "нет")
]
print(Back.RESET) # цвет в терминале
answers_counter = [0,0] # счетчик ответов
print(Fore.GREEN) # цвет в терминале RED - красный, YELLOW - желтый и т.д.
for q, a in ls:
    print(q, '[да/нет]' + Style.BRIGHT) # цвет в терминале
    answer = input().strip().lower()
    if answer == a:
        print("правильный ответ")
        answers_counter[0] += 1 # счетчик
        answers_counter[1] += 1 # счетчик
    else:
        print("неправильный ответ")
        answers_counter[0] += 1 # счетчик
print(Style.RESET_ALL) # цвет в терминале
rsltfile=open('Результат_Викторины.txt','w')
rsltfile.write("Дано ответов: {}, Верных ответов: {}".format(answers_counter[0], answers_counter[1]))
rsltfile.close()

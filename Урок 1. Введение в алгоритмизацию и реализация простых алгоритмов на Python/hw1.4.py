"""
Написать программу, которая генерирует в указанных пользователем границах:

случайное целое число;
случайное вещественное число;
случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import random

while True:
    print("Введите границы для целого числа")
    try:
        minn = int(input("Первая граница: "))
        maxx = int(input("Вторая граница: "))
        if maxx > minn:
            print(random.randint(minn, maxx))
        else:
            print(random.randint(maxx, minn))
        break
    except ValueError as err:
        print("Необходимо ввести числа! Повторите попытку.\n")

while True:
    print("Введите границы для вещественного числа")
    try:
        minn = float(input("Минимальная граница: "))
        maxx = float(input("Максимальная граница: "))
        print(random.uniform(minn, maxx))
        break
    except ValueError as err:
        print("Необходимо ввести числа! Повторите попытку.\n")

while True:
    print("Введите границы для символа")
    try:
        minn = ord(input("Минимальная граница: "))
        maxx = ord(input("Максимальная граница: "))
        if 97 <= minn <= 122 and 97 <= maxx <= 122:
            if maxx > minn:
                print(chr(random.randint(minn, maxx)))
            else:
                print(chr(random.randint(maxx, minn)))
            break
        else:
            print("Необходимо ввести буквы английского алфавита\n")
    except TypeError as er:
        print("Необходимо ввести символ!\n")

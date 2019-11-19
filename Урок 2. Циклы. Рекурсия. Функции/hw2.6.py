"""
В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число.
"""
import random

while True:
    number = random.randint(0, 100)
    trying = 10
    while trying > 0:
        try:
            answer = int(input("Какое число от 0 до 100 я загадал?"))
            if (answer > 100) or (answer < 0):
                print("Вы вышли за границу!")
                continue
            else:
                if answer == number:
                    print("Коррррект!")
                    exit()
                elif answer != number:
                    trying -= 1
                    print(f"Неа. Осталось {trying} попыток.\n")
        except ValueError as err:
            print("Необходимо ввести число!")
    else:
        print("Вы не смогли угадали\n")

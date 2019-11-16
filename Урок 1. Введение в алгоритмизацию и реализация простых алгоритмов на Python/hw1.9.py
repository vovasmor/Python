"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)
"""
while True:
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        num3 = int(input("Введите третье число: "))

        if ((num1 > num2) and (num1 < num3)) or ((num1 < num2) and (num1 > num3)):
            print(f"{num1} среднее число")
        elif ((num2 > num1) and (num2 < num3)) or ((num2 < num1) and (num2 > num3)):
            print(f"{num2} среднее число")
        elif ((num3 > num2) and (num3 < num1)) or ((num2 < num1) and (num2 > num3)):
            print(f"{num3} среднее число")
        else:
            print("Необходимо ввести три разных числа!\n")
        break
    except ValueError as er:
        print("Необходимо ввести число! Повторите попытку.\n")

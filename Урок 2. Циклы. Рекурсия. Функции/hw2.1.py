"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""

while True:

    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

    except ValueError as er:
        print("Упс...\nЧто-то пошло не так. Повторите попытку.\n")
        continue

    op = input("Введите знак операции или 0 для завершения: ")

    if op == "+":
        print(f"{num1} + {num2} = {int(num1) + int(num2)}\n")
    elif op == "-":
        print(f"{num1} - {num2} = {int(num1) - int(num2)}\n")
    elif op == "*":
        print(f"{num1} * {num2} = {int(num1) * int(num2)}\n")
    elif op == "/":
        try:
            print(f"{num1} / {num2} = {float(num1) / float(num2)}\n")

        except ZeroDivisionError as er:
            print(
                'Вы только что поделили на ноль. К сожалению, у Вас это получилось.\n'
                'Это неотвратимо приводит Вас к безумию и создает сингулярную аномалию '
                'бесконечной массы в точке Вашего пребывания.\n'
            )
    elif op == "0":
        print("Досвидания!")
        break
    else:
        print("Неверный знак")

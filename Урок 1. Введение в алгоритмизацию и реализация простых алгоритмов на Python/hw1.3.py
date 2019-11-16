"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
"""
while True:
    # Проверка ввода чисел
    try:
        x1 = float(input('введите x1: '))
        y1 = float(input('введите y1: '))
        x2 = float(input('введите x2: '))
        y2 = float(input('введите y2: '))
    except ValueError as err:
        print("Необходимо ввести числа! Повторите попытку.")
        continue
    # Проверка деления на ноль
    try:
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1
        break
    except ZeroDivisionError as er:
        print("Произошло деление на ноль! Повторите попытку.")
        continue

print(f"Уравнение прямой: y = {k}x + {b}")

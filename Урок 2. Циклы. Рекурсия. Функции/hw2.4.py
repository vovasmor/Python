"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""
while True:
    elem = -2
    sum = 0
    try:
        n_el = int(input("Введите число: "))
    except ValueError as err:
        print("Необходимо ввести число! Повторите попытку.")
        continue
    while n_el > 0:
        elem /= -2
        sum += elem
        n_el -= 1
    print(sum)

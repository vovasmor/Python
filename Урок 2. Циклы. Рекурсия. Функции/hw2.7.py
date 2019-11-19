"""
Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""
while True:
    addition = 0
    try:
        n_el = int(input("Введите число: "))
        for item in range(1, n_el+1):
            addition += item
        rm = n_el*(n_el+1)//2
        if addition == rm:
            print("Равенство верно\n")
        else:
            print("Равенство неверно\n")
    except ValueError as er:
        print("Необходимо ввести число!\n")

"""
Определить, является ли год, который ввел пользователем, високосным или невисокосным.
"""
while True:
    try:
        year = int(input("Введите год: "))
        if (year % 4 > 0) or (year % 100 == 0) and (year % 400 > 0):
            print(f"{year} год - невисокосный.")
        else:
            print(f"{year} год - високосный")

    except ValueError as er:
        print("Необходимо ввести число! Повторите попытку.\n")

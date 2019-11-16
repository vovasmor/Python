"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""
while True:
    print("Введите два символа")
    try:
        letter1 = ord(input("Первый символ: "))
        letter2 = ord(input("Вторый символ: "))
        if 97 <= letter1 <= 122 and 97 <= letter2 <= 122:
            print(f"Положение первой буквы:  {letter1 - 96}")
            print(f"Положение второй буквы:  {letter2 - 96}")
            if letter1 > letter2:
                print("Количество букв между символами: ", letter2 - letter1 - 1)
            elif letter1 > letter2:
                print("Количество букв между символами: ", letter1 - letter2 - 1)
            else:
                print("Символы одинаковы, между ними нет букв.")
            break
        else:
            print("Необходимо ввести буквы английского алфавита\n")
    except TypeError as er:
        print("Необходимо ввести символ!\n")













"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""
while True:
    try:
        number = [item for item in str(int(input("number: ")))]
    except ValueError as err:
        print("Необходимо ввести число! Повторите попытку.")
        continue
    number.reverse()
    print(f"{''.join(number)}\n")

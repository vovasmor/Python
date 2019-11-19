"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
while True:
    even = 0
    even_list = []
    odd = 0
    odd_list = []

    try:
        number = int(input("number: "))
    except ValueError as err:
        print("Необходимо ввести число! Повторите попытку.")
        continue

    for item in str(number):
        if int(item) % 2 == 0:
            even += 1
            even_list.append(item)
        else:
            odd += 1
            odd_list.append(item)
    print(
        f"\nИтоги числа {number}\n"
        f"{even} четных чисел({', '.join(even_list)})\n"
        f"{odd} нечетных чисел({', '.join(odd_list)})\n"
        )

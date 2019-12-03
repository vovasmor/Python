"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
import collections

dict_16 = {str(x): y for x, y in zip(range(10), range(10))}
dict_16.update({x: y for x, y in zip(["A", "B", "C", "D", "E", "F"], range(10, 16))})


def sum_16(number_1, number_2):
    defdict = collections.deque()
    number_1 = collections.deque(number_1)
    number_2 = collections.deque(number_2)
    while len(number_1) != len(number_2):
        if len(number_1) > len(number_2):
            number_2.appendleft("0")
        else:
            number_1.appendleft("0")
    number_1.reverse()
    number_2.reverse()
    k = 0
    for i in range(len(number_1)):
        sum_el = (dict_16[number_1[i]] + dict_16[number_2[i]] + k) % 16
        k = 1 if dict_16[number_1[i]] + dict_16[number_2[i]] > 15 else 0
        defdict.appendleft(''.join([key for key, value in dict_16.items() if value == sum_el]))
        if i == len(number_1) - 1 and k == 1:
            defdict.appendleft("1")
    return defdict


def mult_16(number_1, number_2):
    number_1 = collections.deque(number_1)
    number_2 = collections.deque(number_2)
    if len(number_1) < len(number_2):
        number_1, number_2 = number_2, number_1
    number_1.reverse()
    number_2.reverse()
    list_mult = []
    for i in range(len(number_2)):
        mult = []
        k = 0
        for j in range(len(number_1)):
            mul_el = ((dict_16[number_2[i]] * dict_16[number_1[j]] + k) % 16)
            k = (dict_16[number_2[i]] * dict_16[number_1[j]] + k) // 16
            mult.append((''.join([key for key, value in dict_16.items() if value == mul_el])))
            if j == len(number_1) - 1 and k:
                mult.append(str(k))
        list_mult.append(list(reversed(mult)))

    for item in range(1, len(list_mult)):
        list_mult[item].extend("0" * item)
        list_mult[0] = sum_16(''.join(list_mult[0]), ''.join(list_mult[item]))
    return list_mult[0]


def deque():
    number_1 = (input("Введите первое число в шестнадцатеричной системе счисления: ").upper())
    number_2 = (input("Введите второе число в шестнадцатеричной системе счисления: ").upper())
    print(f"{''.join(list(number_1))} + {''.join(list(number_2))} = {''.join(list(sum_16(number_1, number_2)))}")
    print(f"{''.join(list(number_1))} * {''.join(list(number_2))} = {''.join(list(mult_16(number_1, number_2)))}")


deque()

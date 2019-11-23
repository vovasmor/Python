"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random

# Ограничим длину массива до 10 элементов
my_list = [random.randint(0, 20) for i in range(10)]
print("Начальный список: ", my_list)

# Находим индексы минимального и максимального элементов массива
Max = my_list.index(max(my_list))
Min = my_list.index(min(my_list))
print(f"min: {my_list[Min]}\nmax: {my_list[Max]}")
if Min < Max:
    print(sum(my_list[Min+1:Max]))
else:
    print(sum(my_list[Max+1:Min]))

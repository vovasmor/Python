"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

# Ограничим длину массива до 8 элементов
my_list = [random.randint(0, 100) for i in range(8)]
print("Начальный список: ", my_list)
# Находим минимальный и максимальный элемент массива
Max = my_list.index(max(my_list))
Min = my_list.index(min(my_list))
# Меняем местами
my_list[Max], my_list[Min] = my_list[Min], my_list[Max]
print("Конечный спискок: ", my_list)

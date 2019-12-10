"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random


def bubble_sort(length):
    """
    Сортировка по убыванию случайного списка length длины
    :param length: int
    :return: list
    """
    my_list = [random.randint(-100, 100) for i in range(length)]
    number = len(my_list) - 1
    while number > 0:
        for i in range(number):
            # Если элемент меньше следующего, то меняем их местами
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        number -= 1
    return my_list


print(bubble_sort(10))

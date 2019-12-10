"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""
import random


def find_median(length):
    """
    :param length: int
    :return: list
    """
    middle = [random.randint(0, 100) for i in range(2*length + 1)]
    left, right = [], []
    for i in range(len(middle) // 2):
        left.append(middle.pop(middle.index(min(middle))))
        right.append(middle.pop(middle.index(max(middle))))
    right.reverse()
    print(f"Медианой списка {left}{middle}{right} является число {middle}")
    return middle


find_median(10)

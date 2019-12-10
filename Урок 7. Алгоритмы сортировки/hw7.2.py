"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы
"""
import random


def merger(lst):
    """
    :param lst: list
    :return: list
    """
    middle = len(lst)
    if middle < 2:
        return lst
    left = merger(lst[:middle // 2])
    right = merger(lst[middle // 2:middle])
    i, j = 0, 0
    result = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            result.append(right[j])
            j += 1
        elif not j < len(right):
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result


my_list = [random.randint(0, 50) for i in range(10)]
print(my_list)
print(merger(my_list))

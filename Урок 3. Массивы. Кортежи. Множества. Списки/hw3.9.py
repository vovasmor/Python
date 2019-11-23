"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random

min_list = []
matrix = [[random.randint(0, 20) for i in range(5)] for j in range(5)]
print('\n'.join(['\t'.join(['%d' % i for i in el]) for el in matrix]))

[min_list.append(min(line)) for line in matrix]
print(f"\n{min_list}\nМаксимальный элемент среди минимальных элементов {max(min_list)}")

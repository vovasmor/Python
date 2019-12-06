"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
"""

import random
from pympler import asizeof
from sys import getsizeof
import sys
import time
from memory_profiler import profile


"""
Создание матриц
"""
# ---------------------------------------------------------------------------------------------
@profile
def main(column, line):
    matrix = [[random.randint(1, 20) for i in range(1, line)] for j in range(1, column)]
    print(getsizeof(matrix))  # 52
    print(asizeof.asizeof(matrix))  # 456
    return matrix


# ---------------------------------------------------------------------------------------------
@profile
def with_2for(size):
    matrix = []
    for i in range(size):
        b = []
        for j in range(size):
            b.append(random.randint(0, 10))
        matrix.append(b)
    print(getsizeof(matrix))  # 68
    print(asizeof.asizeof(matrix))  # 608
    return matrix


# ---------------------------------------------------------------------------------------------
@profile
def with_for(size):
    matrix = []
    line = []

    for item in range(1, (size ** 2) + 1):
        number = random.randint(1, 20)
        if item % size == 0:
            line.append(number)
            matrix.append(line)
            line = []
        else:
            line.append(number)
    print(getsizeof(matrix))  # 68
    print(asizeof.asizeof(matrix))  # 704
    return matrix


# ---------------------------------------------------------------------------------------------
sys.setrecursionlimit(888888)


@profile
def recursion(line, column, count=0, func_matrix=[]):
    matrix_recursion = []
    if count + 1 == column:
        for item in range(line):
            matrix_recursion.append(random.randint(1, 20))
        func_matrix.append(matrix_recursion)
        print(getsizeof(func_matrix))  # 52
        print(asizeof.asizeof(func_matrix))  # 208
        return func_matrix
    else:
        for item in range(line):
            matrix_recursion.append(random.randint(1, 20))
        count += 1
        func_matrix = recursion(line, column, count)
        func_matrix.append(matrix_recursion)
        print(f"else", getsizeof(func_matrix))  # 68
        print(f"else", asizeof.asizeof(func_matrix))  # 672
        return func_matrix


main(50, 50)
with_2for(50)
with_for(50)
recursion(50, 50)

"""
Python 3.7.4, windows 10, 64 bit
В данном примере выделенная память оказалось одинаковой, однако рекурсия тратит чуть больше памяти чем другие.
24.3 MiB для первых трех примеров и 24.5 MiB для рекурсии
"""
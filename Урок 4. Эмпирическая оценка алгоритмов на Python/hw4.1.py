"""
Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.

Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import random
import timeit
import cProfile
import sys

"""
Анализирую скорость и сложность 9 задания 3-го урока, а именно, создание матрицы.
"""


# ---------------------------------------------------------------------------------------------
# Изначальное решение 9-го задания через генератор с двумя циклами. Сложность алгоритма: О(N**2)
def main(column, line):
    matrix = [[random.randint(1, 20) for i in range(1, line)] for j in range(1, column)]
    return matrix


# Решение через два цикла. Сложность алгоритма: О(N**2)
# ---------------------------------------------------------------------------------------------
def with_2for(size):
    matrix = []
    for i in range(size):
        b = []
        for j in range(size):
            b.append(random.randint(0, 10))
        matrix.append(b)
    return matrix


# ---------------------------------------------------------------------------------------------
# Решение квадратной матрицы через один цикл. Сложность алгоритма: О(N**2)
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
    return matrix


# ---------------------------------------------------------------------------------------------
# Решение через рекурсию. Сложность алгоритма: О(N**2)
sys.setrecursionlimit(888888)


def recursion(line, column, count=0, func_matrix=[]):
    matrix_recursion = []
    if count + 1 == column:
        for item in range(line):
            matrix_recursion.append(random.randint(1, 20))
        func_matrix.append(matrix_recursion)
        return func_matrix
    else:
        for item in range(line):
            matrix_recursion.append(random.randint(1, 20))
        count += 1
        func_matrix = recursion(line, column, count)
        func_matrix.append(matrix_recursion)
        return func_matrix


# ---------------------------------------------------------------------------------------------
"""
Матрица 15х15, number=10000:                            Матрица 150х150, number=10000:
main       2.8383926 секунд                             main       311.4872992 секунд
with_2for  3.2611969 секунд                             with_2for  316.5643872 секунд
with_for   3.4290283 секунд                             with_for   340.7777354 секунд
recursion  3.3639368 секунд                             recursion  325.5572231 секунд


cProfile.run('main(150, 150)'):
124361 function calls in 0.045 seconds
1    0.000    0.000    0.051    0.051 hw4.1.py:19(main)

cProfile.run('with_2for(150)'):
145207 function calls in 0.057 seconds
1    0.009    0.009    0.057    0.057 hw4.1.py:25(with_2for)

cProfile.run('with_for(150)'):
148778 function calls in 0.061 seconds
1    0.011    0.011    0.060    0.060 hw4.1.py:37(with_for)

cProfile.run('recursion(150, 150)'):
149051 function calls (148902 primitive calls) in 0.059 seconds
150/1    0.010    0.000    0.059    0.059 hw4.1.py:56(recursion)

Итог:
1. Функция with_for проигрывает из-за своей сложности (стоит также не забывать про константу О(1)),
функция recursion проигрывает из-за количества вызовов, 
но при больших значениях результаты можно улучшить после увеличения стека для рекурсии, 
потому что при обычных значениях стек переполняется.
Функция with_2for сложнее генераторов, поэтому наиболее выгодным алгоритмом является первый вариант main.
2. Использование профайлера, при малых значениях, малоцелесообразно
3. При малых значениях, рекурсия является наихудшим вариантом решения
4. Не стоит загружать компьютер во время просчитывания времени
"""

# print("main:", timeit.timeit("main(2, 2)", number=10000, setup="from __main__ import main"))
# print("with_2for:", timeit.timeit("with_2for(2)", number=10000, setup="from __main__ import with_2for"))
# print("with_for:", timeit.timeit("with_for(2)", number=10000, setup="from __main__ import with_for"))
# print("recursion:", timeit.timeit("recursion(2, 2)", number=10000, setup="from __main__ import recursion"))

# cProfile.run('main(15, 15)')
# cProfile.run('with_2for(15)')
# cProfile.run('with_for(15)')
# cProfile.run('recursion(15, 15)')

# print("main:", timeit.timeit("main(150, 150)", number=10000, setup="from __main__ import main"))
# print("with_2for:", timeit.timeit("with_2for(150)", number=10000, setup="from __main__ import with_2for"))
# print("with_for:", timeit.timeit("with_for(150)", number=10000, setup="from __main__ import with_for"))
# print("recursion:", timeit.timeit("recursion(150, 150)", number=10000, setup="from __main__ import recursion"))

# cProfile.run('main(150, 150)')
# cProfile.run('with_2for(150)')
# cProfile.run('with_for(150)')
# cProfile.run('recursion(150, 150)')

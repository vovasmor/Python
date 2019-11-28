"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
"""
import cProfile
import timeit


# ---------------------------------------------------------------------------------------------
#  Используя алгоритм «Решето Эратосфена»
def eratosthenes(index):
    if index < 600000:
        last_index = (index * 30) // 2
    elif index < 600:
        last_index = (index * 15) // 2
    else:
        last_index = (index * 50) // 2

    number = [i for i in range(last_index)]

    number[1] = 0

    for i in range(2, last_index):
        if number[i] != 0:
            j = i * 2
            while j < last_index:
                number[j] = 0
                j += i

    simple_num = [i for i in number if i != 0]
    return simple_num[index-1]


# Итог: Решето все еще лучши вариант

# ---------------------------------------------------------------------------------------------
# Без использования «Решета Эратосфена»


def find_simple(index):
    num = 3
    simple_number = [2]
    while True:
        if len(simple_number) == index:
            return simple_number[index - 1]
        else:
            for i in simple_number:
                if num % i == 0:
                    break
            else:
                simple_number.append(num)
        num += 1
# ---------------------------------------------------------------------------------------------


"""
Используя алгоритм «Решето Эратосфена»                    Без использования «Решета Эратосфена»
eratosthenes 10:    0.3855047                             find_simple 10:    0.0913236
eratosthenes 1000:  54.5626767                            find_simple 1000:  323.8823975


6 function calls in 0.006 seconds
1    0.004    0.004    0.005    0.005 hw4.2.py:15(eratosthenes)

8921 function calls in 0.037 seconds
1    0.036    0.036    0.037    0.037 hw4.2.py:44(find_simple)

1. Использование профайлера, при малых значениях, все также малоцелесообразно
2. При малых значениях решето Эратосфена проигрывает, однако становится выгодным с увеличением значений
"""

# print("eratosthenes:", timeit.timeit("eratosthenes(1000)", number=10000, setup="from __main__ import eratosthenes"))
# print("find_simple:", timeit.timeit("find_simple(1000)", number=10000, setup="from __main__ import find_simple"))
#
# cProfile.run('eratosthenes(1000)')
# cProfile.run('find_simple(1000)')



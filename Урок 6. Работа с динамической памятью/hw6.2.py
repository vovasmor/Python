"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
"""

from memory_profiler import profile
from pympler import asizeof
from sys import getsizeof


#  Используя алгоритм «Решето Эратосфена»
@profile
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

    print(len(simple_num))  # 35
    print(asizeof.asizeof(simple_num))  # 736

    return simple_num[index-1]


# ---------------------------------------------------------------------------------------------
# Без использования «Решета Эратосфена»
@profile
def find_simple(index):
    num = 3
    simple_number = [2]
    while True:
        if len(simple_number) == index:

            print(len(simple_number))   # 10
            print(asizeof.asizeof(simple_number))   # 264

            return simple_number[index - 1]
        else:
            for i in simple_number:
                if num % i == 0:
                    break
            else:
                simple_number.append(num)
        num += 1


eratosthenes(10)
find_simple(10)

"""
Python 3.7.4, windows 10, 64 bit
Как итог, результаты показали, что решето Эратосфена немного проигрывает по памяти, 
также величина числа не играет большой роли. 27.1 MiB для Эратосфена и 24.5 MiB для простого поиска числа.
"""

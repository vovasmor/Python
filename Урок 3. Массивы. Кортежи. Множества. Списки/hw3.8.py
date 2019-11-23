"""
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
matrix = []
for i in range(4):
    line = []
    Sum = 0
    print("%d-я строка:" % int(i+1))
    for j in range(4):
        while True:
            try:
                number = int(input())
                Sum += number
                line.append(number)
                break
            except ValueError as er:
                print("Необходимо ввести число!")
                continue
    line.append(Sum)
    matrix.append(line)
for i in matrix:
    print(i)

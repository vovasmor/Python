"""
Определить, какое число в массиве встречается чаще всего.
"""
import random

# Ограничим длину массива до 10 элементов
my_list = [random.randint(0, 9) for i in range(10)]
print("Начальный список: ", my_list)
# Создадим множество неповторяющихся элементов
my_list_set = set(my_list)

max_count = 0
max_item = None
for item in my_list_set:
    count = my_list.count(item)
    if count > max_count:
        max_count = count
        max_item = item

print(max_count, 'раз(а) встречается число', max_item)

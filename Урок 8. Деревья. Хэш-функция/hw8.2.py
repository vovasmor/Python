"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import Counter, deque


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(string):
    # Находим уникальные элементы и сортируем их
    uniq_el = deque(sorted(Counter(string).items(), key=lambda item: item[1]))
    while len(uniq_el) > 1:
        # Связываем два первых элемента с наименьшей частотой появления
        weight = uniq_el[0][1] + uniq_el[1][1]
        # Удалаем и возвращаем два первых элемента слева для left и right соответсвенно
        node = Node(left=uniq_el.popleft()[0], right=uniq_el.popleft()[0])
        # Теперь мы ищем куда можно вставить элементы, которые мы ранее связали в weight
        for number, value in enumerate(uniq_el):
            """
            weight: частота появления ранее связанных элементов
            value[1]: частота появления элемента в веденной строке word
            """
            if weight > value[1]:
                continue
            else:
                # Вставляем связанные элементы weight
                uniq_el.insert(number, (node, weight))
                break
        else:
            # Добавляем связанный корневой элемент
            uniq_el.append((node, weight))
    return uniq_el[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    # Если элемент не словарь, то записываем его
    if not isinstance(tree, Node):
        code_table[tree] = path
    # Если елемент словарь, то рекурсивно вводим его в эту же фунцию
    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


while True:
    word = input("Введите строку, которую хотите закодировать")
    if word == "":
        print("Вы ничего не ввели. Попробуйте снова.")
    else:
        break

haffman_code(haffman_tree(word))

# Выводим закодированный код
for i in word:
    print(code_table[i], end=' ')

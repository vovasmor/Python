"""
Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib


def hash_func(string):
    """
    :param string: str
    :return: dict
    """
    word_hash = hashlib.sha1(bytes(string, 'utf-8')).hexdigest()
    hash_dict = {}

    for i in range(len(string)):
        letter = ''
        for j in word[i:]:
            letter += j
            hash_letter = hashlib.sha1(bytes(letter, 'utf-8')).hexdigest()

            # Если хеш подстроки не равен хешу изначальной строки word
            # и он еще не был добавлен в hash_dict, то записываем его.
            if hash_letter != word_hash and hash_letter not in hash_dict:
                hash_dict[letter] = hash_letter

    return hash_dict


while True:
    word = str(input("Введите строку состоящую только из маленьких латинских букв").lower())
    if word == "":
        print("Вы ничего не ввели. Попробуйте снова.")
    elif not word.isalpha():
        print("Необходимо ввести только буквы")
    else:
        break

my_hash = hash_func(word)
print(f"Ваша строка {word} содержит {len(my_hash)} подстрок:")

for key, value in my_hash.items():
    print('\t', f'{key} - {value}')

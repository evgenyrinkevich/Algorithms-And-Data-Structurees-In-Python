# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
import hashlib


def sub_strings_count(string):
    hash_array = [hashlib.sha1(string[i:j].encode('utf-8')).hexdigest() for i in range(len(string))
                  for j in range(i + 1, len(string) + 1)]
    return f'В строке {string} {len(set(hash_array))} подстрок'

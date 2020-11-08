from typing import List


# 1.
# Вх: список чисел, Возвр: список чисел, где
# повторяющиеся числа урезаны до одного
# пример [0, 2, 2, 3] returns [0, 2, 3].


def rm_adj(nums):
    return list(set(nums))


# 2. Вх: Два списка упорядоченных по возрастанию, Возвр: новый отсортированный объединенный список
def merge(a: List, b: List) -> List:
    indexA = 0
    indexB = 0
    res = []
    while indexA < len(a) and indexB < len(b):
        if a[indexA] > b[indexB]:
            res.append(b[indexB])
            indexB += 1
        else:
            res.append(a[indexA])
            indexA += 1
    while indexA < len(a):
        res.append(a[indexA])
        indexA += 1
    while indexB < len(b):
        res.append(b[indexB])
        indexB += 1
    return res

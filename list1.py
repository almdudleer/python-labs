from typing import List


def me(words: List[str]) -> int:
    """Подсчитать количество строк, где строка длиннее двух символов и первый символ равен последнему"""
    return len([word for word in words if len(word) > 2 and word[0] == word[-1]])


# 2.
# Вх: список строк, Возвр: список со строками (упорядочено)
# за искл всех строк начинающихся с 'x', которые попадают в начало списка.
# ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'] -> ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']
def fx(words: List[str]) -> List[str]:
    x_words = sorted([word for word in words if len(word) > 0 and word[0] == "x"])
    other_words = [word for word in sorted(words) if len(word) == 0 or word[0] != "x"]
    return x_words + other_words


# 3.
# Вх: список непустых кортежей,
# Возвр: список сортир по возрастанию последнего элемента в каждом корт.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
def sort_tuples(tuples: List[tuple]):
    return sorted(tuples, key=lambda x: x[-1])

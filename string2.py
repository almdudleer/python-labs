import re


# 1.
# Вх: строка. Если длина > 3, добавить в конец "ing",
# если в конце нет уже "ing", иначе добавить "ly".
def ingify(string: str) -> str:
    if len(string) > 3:

        return string + "ing" if string.endswith("ing") else string + "ly"
    return string


# 2.
# Вх: строка. Заменить подстроку от 'not' до 'bad'. ('bad' после 'not')
# на 'good'.
# Пример: So 'This music is not so bad!' -> This music is good!


def not_bad(string: str) -> str:
    return re.sub(r"not.*bad", "good", string)

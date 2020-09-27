# 1.
# Входящие параметры: int <count> , 
# Результат: string в форме
# "Number of: <count>", где <count> число из вход.парам.
#  Если число равно 10 или более, напечатать "many"
#  вместо <count>
#  Пример: (5) -> "Number of: 5"
#  (23) -> 'Number of: many'
def num_of_items(count: int) -> str:
    return f'Number of: {count if count < 10 else "many"}'


# 2. 
# Входящие параметры: string s, 
# Результат: string из 2х первых и 2х последних символов s
# Пример 'welcome' -> 'weme'.
def start_end_symbols(s: str) -> str:
    assert len(s) > 1
    return s[:2] + s[-2:]


# 3. 
# Входящие параметры: string s,
# Результат: string где все вхождения 1го символа заменяются на '*'
# (кроме самого 1го символа)
# Пример: 'bibble' -> 'bi**le'
# s.replace(stra, strb)
def replace_char(s) -> str:
    return s[0] + ''.join([char if char != s[0] else "*" for char in s[1:]])


# 4
# Входящие параметры: string a и b, 
# Результат: string где <a> и <b> разделены пробелом 
# а превые 2 симв обоих строк заменены друг на друга
# Т.е. 'max', pid' -> 'pix mad'
# 'dog', 'dinner' -> 'dig donner'
def str_mix(a, b) -> str:
    return f'{b[0] + a[1:]} {a[0] + b[1:]}'

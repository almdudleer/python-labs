"""
Прочитать из файла (имя - параметр командной строки)
все слова (разделитель пробел)

Создать "Похожий" словарь который отображает каждое слово из файла
на список всех слов, которые следуют за ним (все варианты).

Список слов может быть в любом порядке и включать повторения.
например "and" ['best", "then", "after", "then", ...] 

Считаем , что пустая строка предшествует всем словам в файле.

С помощью "Похожего" словаря сгенерировать новый текст
похожий на оригинал.
Т.е. напечатать слово - посмотреть какое может быть следующим 
и выбрать случайное.

В качестве теста можно использовать вывод программы как вход.парам. для следующей копии
(для первой вход.парам. - файл)

Файл:
He is not what he should be
He is not what he need to be
But at least he is not what he used to be
  (c) Team Coach


"""

import random
import argparse
from typing import List, Dict

BOS_WORD = ""
EOS_WORD = "<EOS>"


def get_similarity_dict(words: List[str]) -> Dict[str, List[str]]:
    similarity_dict = {}
    for i, word in enumerate(words):
        similarity_dict[word] = words[i+1:]
    return similarity_dict


def generate_text(similarity_dict: Dict[str, List[str]], required_len) -> str:
    generated = []
    next_word = BOS_WORD
    i = 0
    while i < required_len:
        next_word = random.choice(similarity_dict[next_word])
        if next_word == EOS_WORD:
            next_word = BOS_WORD
            continue
        i += 1
        generated.append(next_word)
    return " ".join(generated)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", help="Input file")
    args = parser.parse_args()
    with open(args.input_file) as f:
        words = []
        for line in f:
            words += line.strip().split(" ")

    words = [BOS_WORD] + [w for w in words if w] + [EOS_WORD]
    similarity_dict = get_similarity_dict(words)
    generated = generate_text(similarity_dict, 40)
    print(generated)


if __name__ == "__main__":
    main()

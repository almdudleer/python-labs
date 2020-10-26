import sys
from lxml import etree
import re


def extr_name(filename):
    """
    Вход: nameYYYY.html, Выход: список начинается с года, продолжается имя-ранг в алфавитном порядке.
    '2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' и т.д.
    """
    return


def main():
    args = sys.argv[1:]
    print(args)
    if not args:
        print('use: [--file] file [file ...]')
        sys.exit(1)

    allNames = []

    for arg in args:
        names = []
        top = []
        file = open(arg)
        year = arg[4:-5]
        html = file.read()
        html_table = re.findall(r'<table width="48%".*?</table>', html, flags=re.DOTALL)
        html_table = re.sub(r'<caption>.*?</caption>', '', html_table[0], flags=re.DOTALL)
        html_table = re.sub(r'<tr>.*?</table>', '</table>', html_table, flags=re.DOTALL)
        table = etree.HTML(html_table).find("body/table")
        rows = iter(table)
        next(rows)
        for row in rows:
            values = [col.text for col in row]
            top.append(values)
            names.append((values[0], values[1]))
            names.append((values[0], values[2]))
        allNames.append((year, top[:10]))
        names.sort(key=lambda tup: tup[1])
        print(f"'{year}'", end='')
        for name in names:
            print(f", '{name[1]} {name[0]}'", end='')
        print()

    for record in allNames:
        print(record[0] + " top 10:")
        for name in record[1]:
            print(name)


if __name__ == '__main__':
    main()

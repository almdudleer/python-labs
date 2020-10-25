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
  file = open(args[0])
  html = file.read()
  html_table = re.findall(r'<table width="48%".*?</table>', html, flags=re.DOTALL)
  table = etree.HTML(html_table[0]).find("body/table")
  rows = iter(table)
  headers = [col.text for col in next(rows)]
  for row in rows:
    values = [col.text for col in row]
    print(dict(zip(headers, values)))




  # для каждого переданного аргументом имени файла, вывести имена  extr_name

  # напечатать ТОП-10 муж и жен имен из всех переданных файлов

if __name__ == '__main__':
  main()

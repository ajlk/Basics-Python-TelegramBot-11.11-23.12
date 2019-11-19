"""Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/"""

import requests

with open("dataset_263140_3.txt") as inf:
    info = inf.readline().strip()

basicURL = "https://stepic.org/media/attachments/course67/3.6.3/"
r = requests.get(info)
while True:
    if r.text[0] + r.text[1] == "We":
        break
    r = requests.get(basicURL + r.text)
print(r.text)

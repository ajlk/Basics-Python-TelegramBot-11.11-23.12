"""ам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов. Вам необходимо распаковать этот
архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением
".py". Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом
порядке. """

import zipfile
import os

with zipfile.ZipFile("main.zip", "r") as zip_ref:
    zip_ref.extractall()
ending = ".py"
list_of_folders = set()
for dirpath, dirnames, files in os.walk('main'):
    for file_name in files:
        if file_name[-3:] == ending:
            if dirpath not in list_of_folders:
                list_of_folders.add(dirpath.lstrip("./"))
new_set = sorted(list_of_folders)

for i in new_set:
    print(i)

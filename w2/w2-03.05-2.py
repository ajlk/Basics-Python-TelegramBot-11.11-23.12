"""Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое
частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько,
вывести лексикографически первое (можно использовать оператор < для строк). Слова, написанные в разных регистрах,
считаются одинаковыми. """


# Преобразуем список в словарь
def counter_lst_dict(d, lst):
    for i in lst:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1


# Конвертируем values словаря d1 в keys словаря d2
def counter_dict_dict(d1, d2):
    for key, value in d1.items():
        if value in d2:
            d2[value].append(key)
        else:
            d2[value] = [key]


# --------------------------------------------
listOfWords = ""
file = open("dataset_263138_3.txt", "r")
for line in file:
    listOfWords += line.lower().strip()
    listOfWords += " "
file.close()

listOfWords = listOfWords.split()
words = {}
counter_lst_dict(words, listOfWords)
sortedWords = {}
counter_dict_dict(words, sortedWords)

# Поиск наибольшего ключа
maxKey = 0
for key in sortedWords:
    if key > maxKey:
        maxKey = key

# Сортировка слов равной (наибольшей) длины
longestWords = sortedWords.get(maxKey)

print(str(longestWords[0]) + " " + str(maxKey))

"""
...алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом: s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых
символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную
последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

"""

word = input()
if len(word) == 0:
    quit()

i = 0
counter = 1
while i < len(word):
    if i + 1 == len(word):
        coded = word[i] + str(counter)
        print(coded)
        quit()
    if word[i] == word[i + 1]:
        i += 1
        counter += 1
    else:
        coded = word[i] + str(counter)
        print(coded, end="")
        i += 1
        counter = 1
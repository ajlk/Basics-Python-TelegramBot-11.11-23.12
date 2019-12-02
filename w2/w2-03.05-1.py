"""Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования
повторов, и производит обратную операцию, получая исходный текст. В исходном тексте не встречаются цифры, так что код
однозначно интерпретируем. """


def is_int(s_item):
    try:
        int(s_item)
        return True
    except ValueError:
        return False


with open("dataset_263138_2.txt") as inp:
    s = inp.readline().strip()

var_let = "0"
var_num = "0"

for i in range(len(s)):
    if not is_int(s[i]):
        if i != 0:
            print(var_let * int(var_num), end="")
            var_let = s[i]
            var_num = "0"
        else:
            var_let = s[i]
    else:
        var_num += s[i]
        if i == len(s) - 1:
            print(var_let * int(var_num))
            quit()
print()

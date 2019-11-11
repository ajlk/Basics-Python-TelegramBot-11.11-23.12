"""
Напишите программу, которая считывает целые числа с консоли по одному числу в строке.

Для каждого введённого числа проверить:
если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке.

"""

a = 0
my_list = []

while a <= 100:

    a = input()
    if a.isnumeric():
        a = int(a)
        if a > 100:
            break
    else:
        if len(my_list) == 0:
            quit()
        print(*my_list, sep="\n")
        print("Only numbers allowed")
        quit()

    if a >= 10:
        my_list.append(a)
    else:
        continue

print(*my_list, sep="\n")

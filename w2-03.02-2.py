"""Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные
значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного
списка """


def modify_list(l):
    l[:] = [int(x / 2) for x in l if x % 2 == 0]

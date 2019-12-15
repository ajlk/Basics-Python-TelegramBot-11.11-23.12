"""Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Формат входных данных В первой строке входных данных содержится целое число n - число классов исключений. В
следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й
класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от
себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза. В следующей строке
содержится число m - количество обрабатываемых исключений. Следующие m строк содержат имена исключений в том порядке,
в каком они были написаны у Антона в коде. Гарантируется, что никакое исключение не обрабатывается дважды. Формат
выходных данных Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода,
не изменив при этом поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных
данных. """

errors_dict = {}
values_was_printed = []

num_of_exceptions = input()



def exception_finder(dictionary, the_error, already_printed):
    if the_error not in dictionary or dictionary[the_error] == "":
        return -1
    else:
        pass


for i in range(int(num_of_exceptions)):
    temp_line = input().split()
    child = temp_line[0]
    parent = temp_line[2:]
    errors_dict[child] = parent
del temp_line

num_of_exceptions = input()

for i in range(int(num_of_exceptions)):
    var = input()
    for value_was_printed in values_was_printed:
        foo = exception_finder(errors_dict, var, value_was_printed)
        if foo == -1:
            values_was_printed.append(var)
            break
        else:


    values_was_printed.append(var)

"""
    for key, value in errors_dict.items():
        if key == var:
            for z in value:
                if z in was_printed:
                    can_be_skipped.append(var)
                    break
    was_printed.add(var)
"""
"""for i in can_be_skipped:
    print(i)"""

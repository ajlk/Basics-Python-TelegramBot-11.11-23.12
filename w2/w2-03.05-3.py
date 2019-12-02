"""Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке
записана следующая информация: Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку Поля внутри
строки разделены точкой с запятой, оценки — целые числа. Напишите программу, которая считывает файл с подобной
структурой и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке,
соответствующей этому абитуриенту. Также в конце файла, на отдельной строке, через пробел запишите средние баллы по
математике, физике и русскому языку по всем абитуриентам"""

# List of students
listOfStudentsRaw = []

with open("dataset_263138_4.txt") as inf:
    for line in inf:
        listOfStudentsRaw.append(line.strip())

# Dictionary with students
listOfStudents = {}
for key, value in enumerate(listOfStudentsRaw):
    listOfStudents[key] = value

# Iterators
totalPointsMath = 0
totalPointsPhys = 0
totalPointsRuss = 0
totalStudents = 0

for key in listOfStudents:
    theStudent = listOfStudents[key].split(";")
    totalPointsMath += float(theStudent[1])
    totalPointsPhys += float(theStudent[2])
    totalPointsRuss += float(theStudent[3])
    totalStudents += 1
    print((float(theStudent[1]) + float(theStudent[2]) + float(theStudent[3])) / 3)

print(totalPointsMath / totalStudents, end=" ")
print(totalPointsPhys / totalStudents, end=" ")
print(totalPointsRuss / totalStudents)

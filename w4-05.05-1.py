"""Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по
настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году."""

import csv
import operator

list_of_crimes = []
with open("Crimes.csv") as line:
    reader = csv.reader(line)
    for row in reader:
        list_of_crimes.append(row)
del list_of_crimes[0]

sorted_list = []
for i in range(len(list_of_crimes)):
    if list_of_crimes[i][2][6:10] == "2015":
        sorted_list.append(list_of_crimes[i][5])

crimes_dict = {}
for i in range(len(sorted_list)):
    if sorted_list[i] not in crimes_dict.keys():
        crimes_dict[sorted_list[i]] = 1
    else:
        crimes_dict[sorted_list[i]] += 1

#print(crimes_dict)
sorted_crimes_dict = sorted(crimes_dict.items(), key=operator.itemgetter(1), reverse=True)
#print(sorted_crimes_dict)
print(sorted_crimes_dict[0][0])

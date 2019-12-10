"""В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней,
равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.
"""

from datetime import date, timedelta

year, month, day = map(int, input().split())
delta = timedelta(int(input()))

d = date(year, month, day)

new_date = d + delta

print(f"{new_date.year} {new_date.month} {new_date.day}")

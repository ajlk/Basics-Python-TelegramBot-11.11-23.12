year = input()
if year.isnumeric():
    year = int(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Only numbers allowed")

# The check if a value is an integer
def is_valid(var):
    try:
        int(var)
    except ValueError:
        print("Only integers allowed")
        quit()
    if int(var) < 0:
        print("A value shall be equal or greater than zero")
        quit()
    return int(var)


# ---------------------------------

number = is_valid(input())

if number // 10 > 0:
    num_order = 2
else:
    num_order = 1

a = number % 10
if a == 1:
    ending = ""
elif 1 < a < 5:
    ending = "а"
else:
    ending = "ов"

if num_order == 2 and number % 100 // 10 == 1:
    ending = "ов"

print(str(number) + " программист" + ending)

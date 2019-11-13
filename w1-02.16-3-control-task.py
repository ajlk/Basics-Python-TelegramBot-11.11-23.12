import math


# The check of an figure type
def is_figure(var):
    if not (var == "треугольник" or var == "прямоугольник" or var == "круг"):
        print("A figure type not recognized.")
        quit()


# General check of values
def does_it_pass(var):
    # The check if a value is a number
    try:
        float(var)
    except ValueError:
        print("Only numbers allowed.")
        quit()

    # The check if a value is greater than zero
    if float(var) <= 0:
        print("Values shall be greater than zero.")
        quit()

    return float(var)


# ---------------------------------
pi = 3.14

figure = input().lower()
is_figure(figure)

if figure == "треугольник":
    val_1 = does_it_pass(input())
    val_2 = does_it_pass(input())
    val_3 = does_it_pass(input())
    p = (val_1 + val_2 + val_3) / 2
    print(math.sqrt(p * (p - val_1) * (p - val_2) * (p - val_3)))
    quit()

elif figure == "прямоугольник":
    val_1 = does_it_pass(input())
    val_2 = does_it_pass(input())
    print(val_1 * val_2)
    quit()

else:
    val_1 = does_it_pass(input())
    print(val_1 ** 2 * pi)
    quit()

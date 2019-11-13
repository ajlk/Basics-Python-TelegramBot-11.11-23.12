# ---------------------------------


# The check if a value is a number
def is_number(var):
    try:
        float(var)
    except ValueError:
        print("Only numbers allowed")
        quit()


# The check of an operation type
def is_operation(var):
    if not (var == "+" or var == "-" or var == "/" or var == "*" or var == "mod" or var == "pow" or var == "div"):
        print("Operation not found")
        quit()


# Where the magic happens
def to_do_cases(first_val, second_val, operations):
    if operations == "/" or operations == "mod" or operations == "div" and second_val == 0:
        print("Деление на 0!")
        quit()
    if operations == "+":
        print(first_val + second_val)
        quit()
    if operations == "-":
        print(first_val - second_val)
        quit()
    if operations == "/":
        print(first_val / second_val)
        quit()
    if operations == "*":
        print(first_val * second_val)
        quit()
    if operations == "mod":
        print(first_val % second_val)
        quit()
    if operations == "pow":
        print(first_val ** second_val)
        quit()
    if operations == "div":
        print(int(first_val // second_val))
        quit()


# ---------------------------------

# firstVal = input("Please enter a first value" + "\n")
firstVal = input()
is_number(firstVal)
# secondVal = input("Please enter a second value" + "\n")
secondVal = input()
is_number(secondVal)
# operation = input("Please enter an operation type: \"+\", \"-\", \"/\", \"*\", \"mod\", \"pow\" or \"div\"" + "\n")
operation = input()
is_operation(operation)

to_do_cases(float(firstVal), float(secondVal), operation)

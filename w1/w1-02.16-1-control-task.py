isNumber = input()
# ---------------------------------
# The check if a value is an integer
try:
    val = int(isNumber)
except ValueError:
    print("Only integers allowed")
    quit()
# ---------------------------------
number = int(isNumber)
foo = number in range(-14, 13) or number in range(15, 17) or number >= 19
print(foo)

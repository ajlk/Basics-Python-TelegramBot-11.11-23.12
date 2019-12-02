import math
try:
    var = float(input())
except ValueError:
    print("Only numbers allowed")
    quit()

print(2 * math.pi * var)

# Least common multiple search

import math

a = input()
if a.isnumeric():
    a = int(a)
else:
    print("Only numbers allowed")
    quit()
b = input()
if b.isnumeric():
    b = int(b)
else:
    print("Only numbers allowed")
    quit()

print(int((abs(a * b)) / math.gcd(a, b)))

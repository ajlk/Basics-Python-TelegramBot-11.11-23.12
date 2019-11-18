"""
Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла и
закрученной по часовой стрелке, как показано в примере (здесь n=5):
"""

try:
    n = int(input())
except ValueError:
    print("Only an integer allowed")
    quit()
if n <= 0:
    print("The value shall be greater than zero")
    quit()

numVal = 1  # value to be recorded to a cell
arr = [[0] * n for i in range(n)]

step = 0  # coefficient with step -1

while step < n:
    for i in range(step, n - step):
        arr[step][i] = numVal
        numVal += 1
    for i in range(step + 1, n - step):
        arr[i][n - (step + 1)] = numVal
        numVal += 1
    for i in range(n - (step + 2), step, -1):
        arr[n - (step + 1)][i] = numVal
        numVal += 1
    for i in range(n - (step + 1), step, - 1):
        arr[i][step] = numVal
        numVal += 1
    step += 1
for i in (range(n)):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()

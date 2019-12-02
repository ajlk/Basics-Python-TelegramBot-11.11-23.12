import copy
matrix = []
matrix_new = []

while True:
    try:
        var = list(map(int, input().split()))
    except ValueError:
        exit()
    matrix.append(var)
matrix_new = copy.deepcopy(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix_new[i][j] = matrix[i][j - 1] + matrix[i][j - len(matrix[0])+1] + matrix[i - 1][j] + \
                           matrix[i - len(matrix)+1][j]

for i in range(len(matrix_new)):
    for j in range(len(matrix_new[0])):
        print(matrix_new[i][j], end=" ")
    print()

matrix = [[1, 2, 3], [4, 5, 6]]
matrix_new = matrix.copy()

print(matrix_new)
matrix[0][0] = 10
print(matrix_new)

"""
matrix_new = matrix[:]
# 
# matrix_new = matrix * 1
matrix_new = [*matrix]
"""

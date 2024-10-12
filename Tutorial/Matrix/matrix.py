matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # Output: 6

matrix[0][1] = 10
print(matrix)  # Output: [[1, 10, 3], [4, 5, 6], [7, 8, 9]]

scaled_matrix = [[element * 2 for element in row] for row in matrix]
print(scaled_matrix)  # Output: [[2, 20, 6], [8, 10, 12], [14, 16, 18]]

transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_matrix)  # Output: [[1, 4, 7], [10, 5, 8], [3, 6, 9]]

import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix addition
result_add = matrix1 + matrix2

# Matrix multiplication (element-wise)
result_multiply = matrix1 * matrix2

# Matrix dot product
result_dot = np.dot(matrix1, matrix2)

submatrix = matrix[0:2, 1:3]  # First two rows, second and third columns

print(submatrix)
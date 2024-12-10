def printMat(matrix):

    [print(*row) for row in matrix]

def multiply_matrix(A, B):

    return [[sum(A[i][j] * B[j][k]
                 for j in range(len(B)))
             for k in range(len(B[0]))]
            for i in range(len(A))]

matrix_A = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [2, 2, 2, 2]]
matrix_B = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [2, 2, 2, 2]]

print("Matrix A:"); printMat(matrix_A)
print("Matrix B:"); printMat(matrix_B)

result_matrix = multiply_matrix(matrix_A, matrix_B)

print("Resultant Matrix:"); printMat(result_matrix)


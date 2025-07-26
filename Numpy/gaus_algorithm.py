import numpy as np

def gaus(matrix):
    n = len(matrix)

    for i in range(n):
        pivot = matrix[i][i]
        matrix[i] = matrix[i] / pivot

        for j in range(i + 1, n):
            factor = matrix[j][i]
            matrix[j] = matrix[j] - factor * matrix[i]

        # for i in range(n - 1, -1, -1):
        #     for j in range(i - 1, -1, -1):
        #         factor = matrix[j][i]
        #         matrix[j] = matrix[j] - factor * matrix[i]

    return matrix


def vector(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    return f"Values: {eigenvalues}, Vectors: {eigenvectors}>"


matrix = np.array([[-3, -1, 2, 11], [2,1,-1, 8], [-2,1,2, 3], [2,1,4,1]], dtype=float)

print(gaus(matrix))
print(vector(matrix))
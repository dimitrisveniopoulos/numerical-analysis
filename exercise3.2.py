import numpy as np

# Function that performs choesky decomposition
def cholesky(A):
    n = len(A)
    L = np.zeros((n,n))

    # Applying l_ij formula
    for j in range (n):
        for i in range (j, n):
            sum = 0
            for k in range(j):
                sum += L[i][k] * L[j][k]
            if i == j:
                L[i][j] = np.sqrt(A[i][j] - sum)
            else:
                L[i][j] = (A[i][j] - sum) / L[j][j]
    return L


A = [[5.2, 3, 0.5, 1, 2],
     [3, 6.3, -2, 4, 0],
     [0.5, -2, 8, -3.1, 3],
     [1, 4, -3.1, 7.6, 2.6],
     [2, 0, 3, 2.6, 15]]

L = cholesky(A)
print(L)
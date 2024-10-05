import numpy as np

# Function that creates P matrix
def pivot(array):
    n = len(array)
    A = array.copy()

    # Initializing P as a diagonal matrix with ones on the main diagonal
    P = np.zeros((n,n))
    for i in range(n):
        P[i][i] = 1

    # Sorting rows to get the final form of P matrix
    for j in range(n):
        max = abs(A[j][j])
        max_pos = j
        for i in range(j, n):
            if abs(A[i][j]) > max:
                max = abs(A[i][j])
                max_pos = i
        A[j], A[max_pos] = A[max_pos], A[j]
        P[[j, max_pos]] = P[[max_pos, j]]

    return P

# Function that performs the LU decomposition of matrix A
def lu_factorization(A):
    n = len(A)

    # Initializing L and U matrices
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    # Applying u_ij and l_ij formulas
    for j in range(n):
        L[j][j] = 1

        for i in range(j+1):
            s = 0
            for k in range(i):
                s += U[k][j] * L[i][k]
            U[i][j] = A[i][j] - s

        for i in range(j, n):
            s = 0
            for k in range(j):
                s += U[k][j] * L[i][k]
            L[i][j] = (A[i][j] - s) / U[j][j]

    return L, U


# Function that solves a system of equations using PA=LU factorization
def gauss(A, b):
    # Creating P, L and U matrices
    P = pivot(A)
    L, U = lu_factorization(np.dot(P, A))
    Pb = np.dot(P, b)

    n = len(A)

    # Solving Lc = Pb for c
    c = np.zeros(n)
    c[0] = Pb[0]
    for i in range(1, n):
        c[i] = Pb[i]
        for j in range(0, i):
            c[i] -= L[i][j] * c[j]

    # Solving Ux = c for x
    x = np.zeros(n)
    x[n - 1] = c[n - 1] / U[n - 1][n - 1]
    for i in range (n - 2, -1, -1):
        x[i] = c[i]
        for j in range (n - 1, i, -1):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x

A = [[2, 1, 5],
     [4, 4, -4],
     [1, 3, 1]]

b = [5,
     0,
     6]

x = gauss(A, b)

print(x)

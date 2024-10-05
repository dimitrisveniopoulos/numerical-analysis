import numpy as np

# Function that calculates infinity norm of vector x
def get_norm(x):
    max = 0
    for i in range(len(x)):
        if abs(x[i]) > max:
            max = abs(x[i])
    return max

# Functions that creates A and b matrices according to the given size
def create_arrays(n):
    A = np.zeros((n, n))
    for i in range(n):
        A[i][i] = 5
    for i in range(n - 1):
        A[i + 1][i] = -2
        A[i][i + 1] = -2

    b = np.ones(n)
    b[0] = 3
    b[n - 1] = 3

    return A, b


# Function that splits matrix A into a diagonal, a lower triangular and an upper triangular matrix
# according to Gauss - Seidel method
def split_array(A):
    n = len(A)

    L = np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            L[i][j] = A[i][j]

    D = np.zeros((n, n))
    for i in range(n):
        D[i][i] = A[i][i]

    U = np.zeros((n, n))
    for i in range (n):
        for j in range (i + 1, n):
            U[i][j] = A[i][j]

    return L, D, U


# Function that performs Gauss - Seidel method
# in order to solve the given equation system
def gauss_seidel(A, b, tol, max_iterations):
    # Creating L, D and U matrices
    L , D, U = split_array(A)
    # Initial solution is a zero matrix
    previous_x = np.zeros(len(A))
    iterations = 0
    while True:
        iterations += 1
        # Calculating approximate solution with Gauss - Seidel formula
        x = np.dot(np.linalg.inv(L + D), np.dot(-U, previous_x) + b)
        # Iteration ends when we find a solution within the tolerance of error
        # or when we have reached the maximum number of iterations
        if abs(get_norm(x) - get_norm(previous_x)) < tol or iterations == max_iterations:
            return x
        previous_x = x


# Solving for n = 10
A, b = create_arrays(10)
x = gauss_seidel(A, b, 0.00005, 25)
print("Solution found for n = 10: ")
print(np.array([x]).T)

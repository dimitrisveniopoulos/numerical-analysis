import numpy as np


# Function that calculates l1 norm of a vector
def get_norm(x):
    sum = 0
    for i in range(len(x)):
        sum += abs(x[i])
    return sum


# Function that creates the Google matrix
def create_g(A, q):
    n = len(A)
    G = np.zeros((n, n))

    # Applying g_ij formula
    for i in range(n):
        for j in range(n):
            G[i][j] = q / n + (A[j][i] * (1 - q)) / sum(A[j])

    return G


# Function that performs the power method
# in order to find the eigenvector of a matrix
# A: the matrix for which we calculate the eigenvector
# x: the starting eigenvector
# tol: tolerance of error
# max_iterations: maximum number of iterations
def power_method(A, x, tol, max_iterations):
    iterations = 0
    previous_l = 1
    while True:
        iterations += 1
        # Applying power method steps
        x = np.dot(A, x)
        l = max(abs(x))
        x = x / l
        # Iteration ends when the value of the eigenvalue is within the tolerance of error
        # or when the maximum number of iterations has been reached
        if abs(l - previous_l) < tol or iterations == max_iterations:
            # Normalizing eigenvector
            x = x / get_norm(x)
            return x


# Creating adjacency matrix A
A = [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]

# Creating Google matrix
q = 0.15
G = create_g(A, q)
# Initiating eigenvector to zeros
x = np.ones(len(A))
# Calculating eigenvector p using the power method
p = power_method(G, x, 0.00000005, 100)
print("Eigenvector p found.")
print(np.array([p]).T)


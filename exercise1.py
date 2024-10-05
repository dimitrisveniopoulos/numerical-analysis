import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return np.exp(np.sin(x) ** 3) + x ** 6 - 2 * x ** 4 - x ** 3 - 1


def df(x):
    return 3 * np.exp(np.sin(x) ** 3) * np.cos(x) * np.sin(x) ** 2 + 6 * x ** 5 - 8 * x ** 3 - 3 * x ** 2


# a: start of interval
# b: end of interval
# tol: tolerance of error
def bisection(a, b, tol):
    iterations = 0
    # Calculating the minimum number of iterations required
    # in order to approach root within tolerance of error
    iterations_needed = (np.log(b - a) - np.log(tol)) / np.log(2)
    while True:
        iterations += 1
        f_a = f(a)
        f_b = f(b)
        # Calculating current root approximation
        m = (a + b) / 2
        f_m = f(m)
        if f_m == 0 or iterations > iterations_needed:
            return m, iterations
        elif f_m * f_a < 0:
            b = m
        elif f_m * f_b < 0:
            a = m


# a: start of interval
# b: end of interval
# tol: tolerance of error
# max_iterations: maximum number of iterations
def newton(a, b, x, tol, max_iterations):
    iterations = 0
    while True:
        iterations += 1
        # Storing previous value of x
        previous_x = x
        # Calculating current root approximation
        x = x - f(x) / df(x)
        # Iteration stops when exact solution is found
        # or when current error is within tolerance of error
        # or when the maximum number of iterations has been reached
        if f(x) == 0 or np.abs(x - previous_x) < tol or iterations >= max_iterations:
            return x, iterations


# a: start of interval
# b: end of interval
# tol: tolerance of error
#max_iterations: maximum number of iterations
def secant(a, b, tol, max_iterations):
    iterations = 0
    x1 = a
    x2 = b
    while True:
        iterations += 1
        # Storing previous value of x
        previous_x = x2
        # Calculating current root approximation
        x = x2 - f(x2) * (x2 - x1) / (f(x2) - f(x1))
        # Iteration stops when exact solution is found
        # or when current error is within tolerance of error
        # or when the maximum number of iterations has been reached
        if f(x) == 0 or np.abs(x - previous_x) < tol or iterations >= max_iterations:
            return x, iterations
        x1 = x2
        x2 = x


tol = 0.000005
max_iterations = 100

# Printing final results
bisection_x1, iterations = bisection(-2, -1, tol)
print("Root x1 found with Bisection method: " + str(bisection_x1))
print("Iterations needed: " + str(iterations))

bisection_x2, iterations = bisection(-1.5, 1.5, tol)
print("Root x2 found with Bisection method: " + str(bisection_x2))
print("Iterations needed: " + str(iterations))

bisection_x3, iterations = bisection(1.5, 2, tol)
print("Root x3 found with Bisection method: " + str(bisection_x3))
print("Iterations needed: " + str(iterations))

newton_x1, iterations = newton(-2, -1, -2, tol, max_iterations)
print("Root x1 found with Newton - Raphson method: " + str(newton_x1))
print("Iterations needed: " + str(iterations))

newton_x2, iterations = newton(-1.5, 1.5, 1, tol, max_iterations)
print("Root x2 found with Newton - Rapshon method: " + str(newton_x2))
print("Iterations needed: " + str(iterations))

newton_x3, iterations = newton(1.5, 2, 2, tol, max_iterations)
print("Root x3 found with Newton - Rapshon method: " + str(newton_x3))
print("Iterations needed: " + str(iterations))

secant_x1, iterations = secant(-2, -1, tol, max_iterations)
print("Root x1 found with Secant method: " + str(secant_x1))
print("Iterations needed: " + str(iterations))

secant_x2, iterations = secant(-1.5, 1, tol, max_iterations)
print("Root x2 found with Secant method: " + str(secant_x2))
print("Iterations needed: " + str(iterations))

secant_x3, iterations = secant(1.5, 2, tol, max_iterations)
print("Root x3 found with Secant method: " + str(secant_x3))
print("Iterations needed: " + str(iterations))

# Creating graph
x = np.linspace(-2, 2)
y = np.exp(np.sin(x) ** 3) + x ** 6 - 2 * x ** 4 - x ** 3 - 1
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
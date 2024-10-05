import numpy as np
import random


def f(x):
    return 94 * np.cos(x) ** 3 - 24 * np.cos(x) + 177 * np.sin(x) ** 2 - 108 * np.sin(x) ** 4\
           - 72 * np.cos(x) ** 3 * np.sin(x) ** 2 - 65


def df(x):
    return (216 * np.cos(x) ** 2 - 432 * np.cos(x)) * np.sin(x) ** 3 \
           + (- 144 * np.cos(x) ** 4 - 282 * np.cos(x) ** 2 + 354 * np.cos(x) + 24) * np.sin(x)


def df2(x):
    return (432 - 432 * np.cos(x)) * np.sin(x) ** 4 \
           + (1224 * np.cos(x) ** 3 - 1296 * np.cos(x) ** 2 + 564 * np.cos(x) - 354) * np.sin(x) ** 2 \
           - 144 * np.cos(x) ** 5 - 282 * np.cos(x) ** 3 + 354 * np.cos(x) ** 2 + 24 * np.cos(x)

# a: start of interval
# b: end of interval
# tol: tolerance of error
# max_iterations: maximum number of iterations
def bisection(a, b, tol, max_iterations):
    iterations = 0
    while True:
        iterations += 1
        f_a = f(a)
        f_b = f(b)
        # Selecting random point within the interval
        x = random.uniform(a, b)
        f_x = f(x)
        # Iteration stops when exact solution is found
        # or when current error is within tolerance of error
        # or when the maximum number of iterations has been reached
        if f_x == 0 or abs(a - b) < tol or iterations == max_iterations:
            return x, iterations
        elif f_x * f_a < 0:
            b = x
        elif f_x * f_b < 0:
            a = x


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
        x = x - f(x) / df(x) - (f(x) ** 2 * df2(x)) / (2 * df(x) ** 3)
        # Iteration stops when exact solution is found
        # or when current error is within tolerance of error
        # or when the maximum number of iterations has been reached
        if f(x) == 0 or np.abs(x - previous_x) < tol or iterations >= max_iterations:
            return x, iterations

# a: start of interval
# b: end of interval
# tol: tolerance of error
# max_iterations: maximum number of iterations
def secant(a, b, tol, max_iterations):
    iterations = 0
    # Initiating starting points
    x1 = a
    x2 = (a + b) / 2
    x3 = b
    while True:
        iterations += 1
        # Storing previous value of x
        previous_x = x3
        q = f(x1) / f(x2)
        r = f(x3) / f(x2)
        s = f(x3) / f(x1)
        # Calculating current root approximation
        x = x3 - (r * (r - q) * (x3 - x2) + (1 - r) * s * (x3 - x1)) / ((q - 1) * (r - 1) * (s - 1))
        # Iteration stops when exact solution is found
        # or when current error is within tolerance of error
        # or when the maximum number of iterations has been reached
        if f(x) == 0 or np.abs(x - previous_x) < tol or iterations >= max_iterations:
            return x, iterations
        x1 = x2
        x2 = x3
        x3 = x


tol = 0.000005
max_iterations = 100

# Printing final results
bisection_x1, iterations = bisection(0, 1, tol, max_iterations)
print("Root x1 found with Bisection method: " + str(bisection_x1))
print("Iterations needed: " + str(iterations))

bisection_x2, iterations = bisection(1, 2, tol, max_iterations)
print("Root x2 found with Bisection method: " + str(bisection_x2))
print("Iterations needed: " + str(iterations))

bisection_x3, iterations = bisection(2, 3, tol, max_iterations)
print("Root x3 found with Bisection method: " + str(bisection_x3))
print("Iterations needed: " + str(iterations))

newton_x1, iterations = newton(0, 1, 0.5, tol, max_iterations)
print("Root x1 found with Newton - Raphson method: " + str(newton_x1))
print("Iterations needed: " + str(iterations))

newton_x2, iterations = newton(1, 2, 1, tol, max_iterations)
print("Root x2 found with Newton - Raphson method: " + str(newton_x2))
print("Iterations needed: " + str(iterations))

newton_x3, iterations = newton(2, 3, 2.5, tol, max_iterations)
print("Root x3 found with Newton - Raphson method: " + str(newton_x3))
print("Iterations needed: " + str(iterations))

secant_x1, iterations = secant(0.8, 2, tol, max_iterations)
print("Root x1 found with Secant method: " + str(secant_x1))
print("Iterations needed: " + str(iterations))

secant_x2, iterations = secant(1, 2, tol, max_iterations)
print("Root x2 found with Secant method: " + str(secant_x2))
print("Iterations needed: " + str(iterations))

secant_x3, iterations = secant(2, 3, tol, max_iterations)
print("Root x3 found with Secant method: " + str(secant_x3))
print("Iterations needed: " + str(iterations))
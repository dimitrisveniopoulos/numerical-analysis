import numpy as np


def f(x):
    return np.sin(x)


def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n + 1)
    sum = 0
    for i in range (1, n):
        sum += f(x[i])

    integral = (b - a) / (2 * n) * (f(x[0]) + f(x[n]) + 2 * sum)
    return integral


def simpson_rule(a, b, n):
    x = np.linspace(a, b, n + 1)

    sum1 = 0
    for i in range(2, n, 2):
        sum1 += f(x[i])

    sum2 = 0
    for i in range(1, n, 2):
        sum2 += f(x[i])

    return (b - a) / (3 * n) * (f(x[0]) + f(x[n]) + 2 * sum1 + 4 * sum2)


a = 0
b = np.pi / 2
number_of_intervals = 10
trapezoidal_integral = trapezoidal_rule(a, b, number_of_intervals)
print("Integral found with trapezoidal rule: " + str(trapezoidal_integral))
simpson_integral = simpson_rule(a, b, number_of_intervals)
print("Integral found with Simpson's rule: " + str(simpson_integral))
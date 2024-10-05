import numpy as np
import matplotlib.pyplot as plt


def splines(x_values, y_values, x):
    n = len(x_values)

    dx = np.zeros(n - 1)
    dy = np.zeros(n - 1)
    for i in range(n - 1):
        dx[i] = x_values[i + 1] - x_values[i]
        dy[i] = y_values[i + 1] - y_values[i]

    A = np.zeros((n, n))
    B = np.zeros(n)
    A[0, 0] = 1
    A[n - 1, n - 1] = 1
    for i in range(1, n - 1):
        A[i, i - 1] = dx[i - 1]
        A[i, i + 1] = dx[i]
        A[i, i] = 2 * (dx[i - 1] + dx[i])
        B[i] = 3 * (dy[i] / dx[i] - dy[i - 1] / dx[i - 1])

    a = y_values.copy()
    c = np.linalg.solve(A, B)
    d = np.zeros(n)
    b = np.zeros(n)
    for i in range(n - 1):
        d[i] = (c[i + 1] - c[i]) / (3 * dx[i])
        b[i] = (dy[i] / dx[i]) - (dx[i] / 3) * (2 * c[i] + c[i + 1])

    for i in range (n - 1):
        if (x_values[i] <= x <= x_values[i + 1]):
            return a[i] + b[i] * (x - x_values[i]) + c[i] * (x - x_values[i]) ** 2 + d[i] * (x - x_values[i]) ** 3


# Initializing x and y values
x_values = [-np.pi, -2.73, -2.15, -1.24, -0.12, 0, 0.73, 1.87, 3, np.pi]
y_values = np.zeros(len(x_values))
for i in range (len(y_values)):
    y_values[i] = np.round(np.sin(x_values[i]),5)

size = 200
new_x_values = np.linspace(-np.pi, np.pi, size)

# Calculating output values and error
splines_output = np.zeros(size)
splines_error = np.zeros(size)
for i in range(200):
    splines_output[i] = splines(x_values, y_values, new_x_values[i])
    splines_error[i] = np.sin(new_x_values[i]) - splines_output[i]

# Calculating RMSE
rmse = np.sqrt(( splines_error ** 2).mean())
print("RMSE = " + str(rmse))

# Plotting approximation graph
plt.plot(new_x_values, splines_output, color='red')
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()

# Plotting error graph
plt.plot(new_x_values, splines_error, color='red')
plt.xlabel("x")
plt.ylabel("Error")
plt.show()


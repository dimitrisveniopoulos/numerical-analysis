import numpy as np
import matplotlib.pyplot as plt


def least_squares(x_values, y_values, x, degree):
    n = len(x_values)
    k = degree + 1
    b = y_values.copy()
    A = np.zeros((n,k))

    for i in range(n):
        for j in range(k):
            A[i, j] = x_values[i] ** j

    c = np.linalg.solve(np.dot(A.transpose(), A), np.dot(A.transpose(), b))
    result = 0
    for i in range(k):
        result += c[i] * x ** i

    return result


# Initializing x and y values
x_values = [-np.pi, -2.73, -2.15, -1.24, -0.12, 0, 0.73, 1.87, 3, np.pi]
y_values = np.zeros(len(x_values))
for i in range (len(y_values)):
    y_values[i] = np.round(np.sin(x_values[i]),5)

size = 200
new_x_values = np.linspace(-np.pi, np.pi, size)

# Calculating output values and error
least_squares_output = np.zeros(size)
least_squares_error = np.zeros(size)
for i in range(200):
    least_squares_output[i] = least_squares(x_values, y_values, new_x_values[i], 4)
    least_squares_error[i] = np.sin(new_x_values[i]) - least_squares_output[i]

# Calculating RMSE
rmse = np.sqrt((least_squares_error ** 2).mean())
print("RMSE = " + str(rmse))

# Plotting approximation graph
plt.plot(new_x_values, least_squares_output, color='red')
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()

# Plotting error graph
plt.plot(new_x_values, least_squares_error, color='red')
plt.xlabel("x")
plt.ylabel("Error")
plt.show()


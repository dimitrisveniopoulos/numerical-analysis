import numpy as np
import matplotlib.pyplot as plt


def lagrange(x_values, y_values, x):
    n = len(x_values) - 1
    output = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if (i != j):
                p *= (x - x_values[j]) / (x_values[i] - x_values[j])
        output += y_values[i] * p
    return output


# Initializing x and y values
x_values = [-np.pi, -2.73, -2.15, -1.24, -0.12, 0, 0.73, 1.87, 3, np.pi]
y_values = np.zeros(len(x_values))
for i in range (len(y_values)):
    y_values[i] = np.round(np.sin(x_values[i]),5)

size = 200
new_x_values = np.linspace(-np.pi, np.pi, size)

# Calculating output values and error
lagrange_output = np.zeros(size)
lagrange_error = np.zeros(size)
for i in range(200):
    lagrange_output[i] = lagrange(x_values, y_values, new_x_values[i])
    lagrange_error[i] = np.sin(new_x_values[i]) - lagrange_output[i]

# Calculating RMSE
rmse = np.sqrt((lagrange_error ** 2).mean())
print("RMSE = " + str(rmse))

# Plotting approximation graph
plt.plot(new_x_values, lagrange_output, color='red')
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()

# Plotting error graph
plt.plot(new_x_values, lagrange_error, color='red')
plt.xlabel("x")
plt.ylabel("Error")
plt.show()



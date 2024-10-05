import numpy as np


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


days = [1,2,3,4,5,6,7,8,9,10]
degree = 2

name1 = "EUROBANK ERGASIAS ΥΠΗΡΕΣΙΩΝ ΚΑΙ ΣΥΜ Α.Ε. (ΕΥΡΩΒ)Προσ"
eurobank_initial_stocks = [0.4408, 0.5000, 0.4780, 0.3950, 0.4228, 0.3800, 0.3400, 0.3234, 0.3400, 0.3654]
eurobank_actual_stocks = [0.3150, 0.3420, 0.4180, 0.3970, 0.4160]
eurobank_interpolated_stocks = np.zeros(5)
eurobank_error = np.zeros(5)
for i in range (11,16):
    eurobank_interpolated_stocks[i - 11] = np.round(least_squares(days, eurobank_initial_stocks, i, degree), 4)
    eurobank_error[i - 11] = eurobank_actual_stocks[i - 11] - eurobank_interpolated_stocks[i - 11]
eurobank_rmse = np.round(np.sqrt((eurobank_error ** 2).mean()), 4)
print(eurobank_interpolated_stocks)
print(eurobank_rmse)


name2 = "ΠΕΙΡΑΙΩΣ FINANCIAL HOLDINGS Α.Ε. (ΠΕΙΡ)"
piraeus_initial_stocks = [1.4460, 1.5000, 1.3800, 1.1500, 1.2250, 1.0060, 1.0000, 0.9505, 0.9655, 1.0400]
piraeus_actual_stocks = [0.9630, 1.1010, 1.2400, 1.1980, 1.2350]
piraeus_interpolated_stocks = np.zeros(5)
piraeus_error = np.zeros(5)
for i in range (11,16):
    piraeus_interpolated_stocks[i - 11] = np.round(least_squares(days, piraeus_initial_stocks, i, degree), 4)
    piraeus_error[i - 11] = piraeus_actual_stocks[i - 11] - piraeus_interpolated_stocks[i - 11]
piraeus_rmse = np.round(np.sqrt((piraeus_error ** 2).mean()), 4)
print(piraeus_interpolated_stocks)
print(piraeus_rmse)

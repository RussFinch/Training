import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes
from statistics import mean


def best_fit_slope_and_intercept(xs, ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))

    b = mean(ys) - m*mean(xs)
    return m, b


def simply(originalarray):
    tmparr = []
    for arr in originalarray:
        for arr1 in arr:
            tmparr.append(arr1)
    return tmparr


# Load the diabetes dataset
diabetes = load_diabetes()

# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = np.array(simply(diabetes_X[:-20]))
diabetes_X_test = np.array(simply(diabetes_X[-20:]))

# Split the targets into training/testing sets
diabetes_y_train = np.array(diabetes.target[:-20])
diabetes_y_test = np.array(diabetes.target[-20:])

m, b = best_fit_slope_and_intercept(diabetes_X_train, diabetes_y_train)

test_Y = []
for x in diabetes_X_test:
    test_Y.append((m*x)+b)

# Plot outputs
plt.scatter(diabetes_X_train, diabetes_y_train, color='red', label='Train Data')
plt.scatter(diabetes_X_test, diabetes_y_test, color='green', label='Test Data')
plt.plot(diabetes_X_test, test_Y, color='blue', linewidth=3, label='Line of best fit')
plt.legend(loc=4)

plt.show()

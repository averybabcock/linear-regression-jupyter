#!/usr/bin/env python
# coding: utf-8

# This notebook demonstrates a simple linear regression analysis using Python to model Salary based on Years of Experience.

#Modified script (Part 2 Script and assignment 3 edits):

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error

if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

dataset = pd.read_csv(filename)
x = dataset[x_col].to_numpy()
y = dataset[y_col].to_numpy()

slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept

mse = mean_squared_error(y, y_pred)

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value ** 2}")
print(f"Correlation coefficient (r): {r_value}")
print(f"P-value: {p_value}")
print(f"Standard Error: {std_err}")
print(f"Mean Squared Error: {mse}")

sorted_indices = np.argsort(x)
x_sorted = x[sorted_indices]
y_pred_sorted = y_pred[sorted_indices]


plt.scatter(x, y, color='red')
plt.plot(x_sorted, y_pred_sorted, color='blue')
plt.title(f'{y_col} vs {x_col}')
plt.xlabel(x_col)
plt.ylabel(y_col)


plt.text(
    1,                   
    max(y) - 3500,            
    f"y = {slope:.2f}x + {intercept:.2f}\n"
    f"r = {r_value:.2f}\n"
    f"MSE = {mse:.2f}",
    fontsize=12,
    bbox=dict(facecolor='white', alpha=0.5)  
)

plt.savefig("linear_regression_python_output.png")
plt.show()
import numpy as np

arr = np.array([10, 20, np.nan, 40])
print(arr)

# In NumPy, missing values are usually represented as:

# np.nan for floating point data
# There is no true NaN for integers, so integers must be converted to float if they contain missing values

# np.nan means “Not a Number”.
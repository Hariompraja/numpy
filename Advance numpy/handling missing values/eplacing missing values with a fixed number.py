import numpy as np

arr = np.array([5, np.nan, 15])

arr_filled = np.nan_to_num(arr, nan=0)
print(arr_filled)
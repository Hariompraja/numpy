import numpy as np

arr = np.array([10, np.nan, 20, np.nan, 30])

clean_arr = arr[~np.isnan(arr)]
print(clean_arr)
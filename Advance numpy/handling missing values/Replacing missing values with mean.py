# Replacing missing values with mean
import numpy as np

arr = np.array([10, np.nan, 30, 40])

mean_value = np.nanmean(arr)
print("Mean:", mean_value)

arr[np.isnan(arr)] = mean_value
print(arr)

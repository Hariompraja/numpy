import numpy as np

arr = np.array([1, np.nan, 3, np.nan, 5])

missing_count = np.isnan(arr).sum()
print("Missing values:", missing_count)
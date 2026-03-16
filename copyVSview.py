import numpy as np

# a = np.array([1, 2, 3, 4, 5])
# b = a.view()
# b[1]=10

# print(a)
# print(b)

a = np.array([1,2,3,4,5])
b = a.copy()
b[0] = 100
print(a,b)
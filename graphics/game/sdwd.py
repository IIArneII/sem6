import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.sum(axis=0) / len(a)
print(b)

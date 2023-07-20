"""
Broadcasting
    - Numpy use optimized C code to perform mathematical operations.
    - Broadcasting is a clever set of rules that enables fast array calculations for arrays of similar (but not equal!)
      shape.
"""
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
A * B
# Output:
# array([5, 12],
#       [21, 32])

A * 2
# array([2, 4],
#       [6, 8])

A = np.random.rand(5, 10, 2)
B = np.random.rand(5, 2)
C = A * B[:, np.newaxis, :]
print("B[:, np.newaxis, :]: \n", B[:, np.newaxis, :])
print("C: ", C)


# outer product
# a = [a1, a2, a3]
# b = [b1, b2, b3]
# a x b = a1*b1, a1*b2, a1*b3
#         a2*b1, a2*b2, a2*b3
#         a3*b1, a3*b2, a3*b3
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
AB = a[:, np.newaxis] * b[np.newaxis, :]

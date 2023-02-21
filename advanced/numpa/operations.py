"""
Mathematical operations
    - np.sqrt
    - ndarray.sum
"""

import numpy as np

np.sqrt(np.array([4, 9, 16]))
# Result:
# array([2., 3., 4.])

# filter
a = np.random.rand(5, 3)
a > 0.3
# Result:
# array([[ True, False, True],
# [ True, True, True],
# [False, True, True],
# [ True, True, False],
# [ True, True, False]], dtype=bool)

# extraction
a[a > 0.5]
print(a[a > 0.5])
# Output:
# [ 0.9755 0.5977 0.8287 0.6214 0.5669 0.9553 0.5894 0.7196 0.9200 0.5781 0.8281 ]

a = np.random.rand(5, 3)
a.sum(axis=0)  # sum over the columns
# Result:
# array([ 2.7454, 2.5517, 2.0303])
a.sum(axis=1)  # sum over the rows
# Result:
# array([ 1.7498, 1.2491, 1.8151, 1.9320, 0.5814])
a.sum()  # With no argument operates on flattened array
# Result:
# 7.3275

# norms
r_i = np.random.rand(10, 2)
norm = np.sqrt((r_i**2).sum(axis=1))
print(norm)
# Output:
# [ 0.7314 0.9050 0.5063 0.2553 0.0778 0.9143 1.3245 0.9486 1.010 1.0212]

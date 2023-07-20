"""
Numpy arrays
    - pip install numpy
"""

import numpy as np

a = np.array([0, 1, 2])

a.dtype

a = np.array([1, 2, 3], dtype="float32")
a.astype("float32")

a = np.array([[0, 1, 2], [3, 4, 5]])
print(a)

a.shape

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

a.shape

a.reshape(4, 4)
print(a)

np.zeros((3, 3))
np.empty(
    (
        3,
        3,
    )
)
np.ones((3, 3), dtype="float32")

np.random.rand(3, 3)

np.zeros_like(a)
np.empty_like(a)
np.ones_like(a)


A = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
A[0]

[a for a in A]

A = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
A[0]  # first row
A[0, 1]  # first row second element
A[0:2]
A[0:2, 0:2]

A[0, 1] = 8
A[0:2, 0:2] = [[1, 1], [1, 1]]

# If we take a slice of the original array, and then we change
# one of its values, the original array will be updated as well.

a = np.array([1, 1, 1, 1])
a_view = a[0:2]
a_view[0] = 2
print(a)
# Output:
# [2 1 1 1]

# a.flasgs.writeable = False prevents mutation of the array

r_i = np.random.rand(10, 2)

# first index is moving while second index is fixed
x_i = r_i[:0]

# first index is fixed while second index is moving
y_i = r_i[0:]
print("r_i: ", r_i)
print("x_i: ", x_i)
print("y_i: ", y_i)


# fancy indexing
a = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
idx = np.array([0, 2, 3])
a[idx]
# Result:
# array([9, 7, 6])

# extracting elements from (0, 2) and (1, 3)
a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
idx1 = np.array([0, 1])
idx2 = np.array([2, 1])
a[idx1, idx2]
# Result:
# array([2 4])

# a[(0, 1)] == a[0, 1] but a[np.array([0, 1])] == a[[0, 1]]

idx1 = [[0, 1], [3, 2]]
idx2 = [[0, 2], [1, 1]]
a[idx1, idx2]
# Result:
# array([[0, 5],
#        [10, 7]])

# swap with slicing and fancy indexing
r_i = np.random(10, 2)
r_i[:, [0, 1]] = r_i[:, [1, 0]]

# mask
a = np.array([0, 1, 2, 3, 4, 5])
mask = np.array([True, False, True, False, False, False])
a[mask]
# Output:
# array([0, 2])


# numpy.fast and numpy.compress for performance
# %timeit is IPython command
r_i = np.random(100, 2)
idx = np.arange(50)  # integers 0 to 50

# %timeit np.take(r_i, idx, axis=0)
# 1000000 loops, best of 3: 962 ns per loop
# %timeit r_i[idx]
# 100000 loops, best of 3: 3.09 us per loop


idx = np.ones(100, dtype="bool")  # all True values
# %timieit np.compress(idx, r_i, axis=0)
# 1000000 loops, best of 3: 1.65 us per loop
# %timeit r_i[idx]
# 100000 loops, best of 3: 5.47 us per loop

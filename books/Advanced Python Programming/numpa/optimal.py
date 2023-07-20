"""
Reaching optimal performance with numexpr
    - numexpr optimizes and compiles array expressions on the fly
    - usage of CPU cache and takes advantage of multiple processors
    - numexpr.evaluate
    - use it with large arrays like distance matrix
"""

import time
import numpy as np
import numexpr as ne

a = np.random.rand(10000)
b = np.random.rand(10000)
c = np.random.rand(10000)
d = ne.evaluate("a + b * c")

# Distant Matrix
# x_ij = x_j - x_i
# y_ij = y_j - y_i
# d_ij = sqrt(x_ij ** 2 + y_ij ** 2)


# Distance Matrix numpy
def distance_numpy():
    r = np.random.rand(10000, 2)
    r_i = r[:, np.newaxis]  # 1000 elements of 1 size of 2 items
    r_j = r[np.newaxis, :]  # 1 element of 10000 size of 2 items
    d_ij = r_j - r_i  # 1000 elements of 1000 size of 2 items
    d_ij = np.sqrt((d_ij**2).sum(axis=2))


# Distance Matrix numexpr
# the reduction operations have to happen last, like sum
def distance_numexpr():
    r = np.random.rand(10000, 2)
    r_i = r[:, np.newaxis]  # NOQA
    r_j = r[np.newaxis, :]  # NOQA
    d_ij = ne.evaluate("sum((r_j - r_i)**2, 2)")  # NOQA
    d_ij = ne.evaluate("sqrt(d_ij)")  # NOQA


t0 = time.time()
for i in range(10):
    distance_numpy()
t1 = time.time()
print("Distance matrix numpy total time: ", t1 - t0)
# Output:
# Distance matrix numpy total time:  20.99950861930847

t0 = time.time()
for j in range(10):
    distance_numexpr()
t1 = time.time()
print("Distance matrix numexpr total time: ", t1 - t0)
# Output:
# Distance matrix numexpr total time:  6.0494585037231445

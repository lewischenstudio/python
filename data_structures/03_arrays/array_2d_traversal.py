"""Traversal - Two Dimensional Array"""

import numpy as np

twoD_array = np.array(
    [
        [11, 15, 10, 6],
        [10, 14, 11, 5],
        [12, 17, 12, 8],
        [15, 18, 14, 9],
    ]
)

print(twoD_array)


def traverseTwoDArray(arr):
    for i in range(len(arr)):  # O(mn)
        for j in range(len(arr[0])):  # O(n)
            print(arr[i][j])


traverseTwoDArray(twoD_array)

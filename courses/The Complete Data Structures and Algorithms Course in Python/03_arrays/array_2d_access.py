"""Accessing an Element in Two Dimensional Arrays"""

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


def accessElements(arr, row_index, col_index):
    if row_index >= len(arr) or col_index >= len(arr[0]):
        print("Incorrect index")
        return
    print(arr[row_index][col_index])


accessElements(twoD_array, 2, 3)
accessElements(twoD_array, 2, 4)

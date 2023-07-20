"""Search for an Element in Two Dimensional Arrays"""

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


def searchTwoDArray(arr, value):
    for i in range(len(arr)):  # O(mn)
        for j in range(len(arr[0])):  # O(n)
            if arr[i][j] == value:  # O(n)
                return f"The value is located at index {i} {j}"
    return "The element is not found"


print(searchTwoDArray(twoD_array, 11))
print(searchTwoDArray(twoD_array, 17))
print(searchTwoDArray(twoD_array, 55))

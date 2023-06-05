"""Insertion - Two Dimensional Array"""

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

new_twoD_array = np.insert(twoD_array, 1, [[1, 2, 3, 4]], axis=0)
print(new_twoD_array)

new_twoD_array = np.append(twoD_array, [[1, 2, 3, 4]], axis=0)
print(new_twoD_array)

"""Lists vs Arrays"""

import numpy as np

myArray = np.array(
    [
        1,
        2,
        3,
        4,
        5,
    ]
)
myList = [1, 2, 3, 4, 5]

print(myArray / 2)
print(myList)


myArray = np.array([1, 2, 3, 4, 5, "a"])
myList = [1, 2, 3, 4, 5, "a"]


print(myArray)
print(myList)

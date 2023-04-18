"""
Write a function to check if an array contains a number in an array.
"""
import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


def findMaxProduct(array_):
    maxProduct = 0
    for i in range(len(array_)):
        for j in range(i + 1, len(array_)):
            if array_[i] * array_[j] > maxProduct:
                maxProduct = array_[i] * array_[j]
                pairs = str(array_[i]) + ", " + str(array_[j])
    print(pairs)
    print(maxProduct)


findMaxProduct(myArray)

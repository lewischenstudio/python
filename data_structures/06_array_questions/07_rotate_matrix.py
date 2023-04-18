"""
Given an Image represented by an NxN matrix, write a method to rotate
the image by 90 degrees.
"""
import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr1_ = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
arr2_ = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])


def rotateMatrixToRight(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # save top element
            top = matrix[layer][i]
            # move left element to top
            matrix[layer][i] = matrix[-i - 1][layer]
            # move bottom element to left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            # move right element to bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            # move top element to right
            matrix[i][-layer - 1] = top
    return matrix


def rotateMatrixToLeft(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # save top element
            top = matrix[layer][i]
            # move right element to top
            matrix[layer][i] = matrix[i][-layer - 1]
            # move bottom element to right
            matrix[i][-layer - 1] = matrix[-layer - 1][-i - 1]
            # move left element to bottom
            matrix[-layer - 1][-i - 1] = matrix[-i - 1][layer]
            # move bottom element to top
            matrix[-i - 1][layer] = top
    return matrix


print("original: \n", arr1)
print("to left arr1: \n", rotateMatrixToLeft(arr1))
print("to right arr1: \n", rotateMatrixToRight(arr1_))

print("original: \n", arr2)
print("to left arr2: \n", rotateMatrixToLeft(arr2))
print("to right arr2 \n", rotateMatrixToRight(arr2_))

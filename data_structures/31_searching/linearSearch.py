"""
Linear Search
"""


def linearSearch(arr, value):
    for i in range(len(arr)):  # O(N)
        if arr[i] == value:
            return i
    return -1


arr = [20, 40, 30, 50, 90]
linearSearch(arr, 90)

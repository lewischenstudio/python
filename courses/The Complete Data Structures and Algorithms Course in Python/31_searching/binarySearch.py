"""
Binary Search
"""


def binarySearch(arr, value):
    start = 0
    end = len(arr) - 1
    middle = (start + end) // 2
    print(start, middle, end)
    while not (arr[middle] == value) and start <= end:
        if value < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = (start + end) // 2
        print(start, middle, end)
    if arr[middle] == value:
        return middle
    return -1


arr = [8, 9, 12, 15, 17, 19, 20, 21, 28]
binarySearch(arr, 16)

# [8, 9, 12, 15, 17, 19, 20, 21, 28]
#  S              M
#  S  M      E
#        SM  E
#            SME

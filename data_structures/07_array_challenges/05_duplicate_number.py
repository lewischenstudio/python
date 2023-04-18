"""
Duplicate Number
Write a function to find the duplicate number on given integer array/list.

Example

removeDuplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
"""


def removeDuplicates(myList):
    arr = []
    for item in myList:
        if item not in arr:
            arr.append(item)
    return arr


print(removeDuplicates([1, 1, 2, 2, 3, 4, 5]))

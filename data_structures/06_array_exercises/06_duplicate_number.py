"""Coding Exercise 6: Duplicate Number"""


def removeDuplicates(myList):
    arr = []
    for item in myList:
        if item not in arr:
            arr.append(item)
    return arr


print(removeDuplicates([1, 1, 2, 2, 3, 4, 5]))

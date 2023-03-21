"""
Duplicate Number

Write a function to find the duplicate number on given integer array/list.
"""

def remove_duplicates(myList):
    arr = []
    for item in myList:
        if item not in arr:
            arr.append(item)
    return arr

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))


def removeDuplicates(myList):
    new_list=[]
    for i in myList:
        if i not in new_list:
            new_list.append(i)
    return new_list
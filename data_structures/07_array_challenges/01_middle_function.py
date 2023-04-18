"""
Middle Function
Write a function called middle that takes a list and returns a new list that contains all but the first and last
elements.

myList = [1, 2, 3, 4]
middle(myList)  # [2,3]
"""


def middle(lst):
    if len(lst) in [0, 1]:
        return lst
    return lst[1:-1]


myList = [1, 2, 3, 4]
middle(myList)  # [2,3]

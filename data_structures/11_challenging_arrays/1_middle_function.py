"""
Middle Function

Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
"""

def middle(lst):
    if len(lst) in [0, 1]:
        return lst
    return lst[1:-1]

myList = [1, 2, 3, 4]
print(middle(myList))  # [2,3]

def middle(lst):
    new = lst[1:]  
    del new[-1]
    return new
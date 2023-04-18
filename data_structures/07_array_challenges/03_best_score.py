"""
Best Score
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
firstSecond(myList) # 90 87
"""


def firstSecond(givenList):
    first = 0
    second = 0
    for number in givenList:
        if number >= first:
            second = first
            first = number
    return (first, second)


myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(firstSecond(myList))

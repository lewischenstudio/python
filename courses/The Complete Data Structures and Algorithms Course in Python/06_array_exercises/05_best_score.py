"""Coding Exercise 5: Best Score"""


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

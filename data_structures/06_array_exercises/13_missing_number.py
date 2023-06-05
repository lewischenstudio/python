"""Coding Exercise 13: Missing Number"""


def missingNumber(myList, totalCount):
    sum1 = totalCount * (totalCount + 1) / 2
    sum2 = sum(myList)
    return sum1 - sum2


print(missingNumber([1, 2, 3, 4, 6], 6))

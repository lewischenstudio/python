"""
Missing Number
Write a function to find the missing number in a given integer array of 1 to 100.

Example

missingNumber([1, 2, 3, 4, 6], 6) # 5
"""


def missingNumber(myList, totalCount):
    sum1 = totalCount * (totalCount + 1) / 2
    sum2 = sum(myList)
    return sum1 - sum2


print(missingNumber([1, 2, 3, 4, 6], 6))

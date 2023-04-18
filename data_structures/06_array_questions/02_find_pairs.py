"""
Write a function to find all pairs of integers whose sum is equal to a given number.
[2, 6, 3, 9, 11]     9   ----> [6, 3]
"""


def findPairs(list_, sum_):
    a = False
    b = False
    for i in range(len(list_)):
        for j in range(i + 1, len(list_)):
            if (list_[i] + list_[j]) == sum_:
                print(list_[i], list_[j])
                a = True
                b = True
    if not a and not b:
        print("Not Found")


findPairs([2, 6, 3, 9, 11], 9)
findPairs([2, 6, 3, 9, 11], 11)
findPairs([2, 6, 3, 9, 11], 6)

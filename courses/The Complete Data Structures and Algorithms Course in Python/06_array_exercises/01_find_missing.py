"""Coding Exercise 1: Find Missing Number"""

import random


def findMissing(a=1, b=100):
    mylist = [n for n in range(a, b + 1)]
    c = random.randint(a, b)
    mylist.remove(c)
    print("The random number is ", c)
    sum1 = sum(mylist)
    sum2 = b * (b + 1) / 2
    print("The missing number is ", sum2 - sum1)


findMissing(1, 100, 67)

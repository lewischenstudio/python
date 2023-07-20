"""
Interview Questions - 1
How to find the sum of digits of a positive integer number using recursion?

Step 1: Recursive case - the flow
10  10/10 = 1 and Remainder = 0
54  54/10 = 5 and Remainder = 4
112 112/10 = 11 and Remainder = 2
    11/10 = 1 and Remainder = 1
Step 2: Base case - the stopping criterion
n = 0
Step 3: Unintentional case - the constraint
sumOfDigits(-11) ??
sumofDigits(1.5) ??
"""


def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "The number must be postive integer only!"
    if n in [0, 1]:
        return int(n)
    return int(n % 10) + sumOfDigits(int(n / 10))


print(sumOfDigits(284))

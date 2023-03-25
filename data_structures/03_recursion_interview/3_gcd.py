"""
Interview Questions - 3
How to find GCD (Greatest Common Divisor) of two numbers using recursion?

Step 1: Recursive case - the flow
GCD is the largest positive integer that divides the numbers without a reminder
gcd(8, 12) = 4
8 = 2 * 2 * 2
12 = 2 * 2 * 3

Euclidean algorithm
gcd(48, 18)
Step 1: 48/18 = 2 remainder 12
Step 2: 18/12 = 1 remainder 6
Step 3: 12/6 = 0 remainder 0

gcd(a, 0) = a
gcd(a, b) = gcd(b, a mod b)

Step 2: Base case - the stopping criterion
- b = 0

Step 3: Unintentional case - the constraint
- Positive integers
- Convert negative numbers to positive
"""


def gcd(a, b):
    assert int(a) == a and int(b) == b, "The numbers must be integers only"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(36, 48))

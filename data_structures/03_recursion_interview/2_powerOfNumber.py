"""
Interview Questions - 2
How to calculate the power of a number using recursion?

Step 1 : Recursive case - the flow
x^n = x * x * x * ... (n times) ... * x
2^4 = 2 * 2 * 2 * 2
x^a + x^b = x ^ (a + b)
x^3 + x^4 = x ^ (3 + 4)

Step 2 : Base case - the stopping criterion
- n = 0
- n = 1

Step 3 : Unintentional case - the constraint
- power(-1,2) ??
- power(3.2, 2) ??
- power(2, 1.2) ??
- power(2, -1) ??
"""


def powerOfNumber(x, n):
    assert n >= 0 and int(n) == n, "The number must be postive integer only!"
    if n in [0, 1]:
        return x
    return x * powerOfNumber(x, n - 1)


print(powerOfNumber(3, 4))

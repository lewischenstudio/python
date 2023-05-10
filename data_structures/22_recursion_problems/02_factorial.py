"""
Write a function factorial which accepts a number and returns the factorial of that number.
A factorial is the product of an integer and all the integers below it; e.g.,
factorial four ( 4! ) is equal to 24, because 4 * 3 * 2 * 1 equals 24.
factorial zero (0!) is always 1.

Step 1: Recursive case - the flow
factorial(1) # 1
factorial(2) # 2 * 1
factorial(4) # 4 * 3 * 2 * 1
factorial(7) # 7 * 6 * 5 * 4 * 3 * 2 * 1

factorial(n) = n * factorial(n - 1)

Step 2: Base case - the stopping criterion
- n = 0 or 1

Step 3: Unintentional case - the constraint
- factorial(-1) ??
- factorial(1.5) ??
"""


def factorial(num):
    assert num >= 0 and int(num) == num, "The number must be postive integer only!"
    if num in (0, 1):
        return 1
    return num * factorial(num - 1)


print(factorial(5))

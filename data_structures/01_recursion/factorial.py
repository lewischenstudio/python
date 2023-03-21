"""
Factorial

- It is the product of all positive integers less than or equal to 0
- Denoted by n! (Christian kramp in 1808)
- Only positive numbers.
- 0! = 1.

Example 1:
4! = 4 * 3 * 2 * 1 = 24

Example 2:
10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3,628,800

n! = n * (n - 1) * (n - 2) * ... * 2 * 1

Step 1 : Recursive case - the flow
n! = n * (n - 1) * (n - 2) * ... * 2 * 1 = n * (n - 1 )!

Step 2 : Base case - the stopping criterion
- 0! = 1
- 1! = 1

Step 3 : Unintentional case - the constraint
factorial(-1) ??
factorial(1.5) ??
"""

def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be postive integer only!'
    if n in [0, 1]:
        return 1
    return n * factorial(n - 1)

print(factorial(-4))
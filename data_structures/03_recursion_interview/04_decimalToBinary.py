"""
Interview Questions - 4
How to convert a number from Decimal to Binary using recursion?

Step 1: Recursive case - the flow
Step 1: Divide the number by 2
Step 2: Get the integer quotient for the next iteration
Step 3: Get the remainder for the binary digit
Step 4: Repeat the steps until the quotient is equal to 0

13 to binary
13/2 = 6 r 1
6/2 = 3 r 0
3/2 = 1 r 1
1/2 = 0 r 1
Answer: 1011

10 to binary
10/2 = 5 r 0
5/2 = 2 r 1
2/2 = 1 r 0
1/2 = 0 r 1
Answer: 1010

f(a) = a%2 + 10 * f(a/2)

Step 2: Base case - the stopping criterion
- a = 0

Step 3: Unintentional case - the constraint
- Positive integers
- Convert negative numbers to positive
"""


def decimalToBinary(a):
    assert a >= 0 and int(a) == a, "The number must be postive integer only!"
    if a == 0:
        return 0
    return a % 2 + 10 * decimalToBinary(int(a / 2))


print(decimalToBinary(3))

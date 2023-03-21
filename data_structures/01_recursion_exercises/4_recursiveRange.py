"""
Write a function called recursiveRange which accepts a number and adds up all the numbers
from 0 to the number passed to the function.

Step 1: Recursive case - the flow
recursiveRange(6) # 21
recursiveRange(10) # 55 

recursiveRange(6) = 0 + 1 + 2 + 3 + 4 + 5 + 6 = 6 + recursiveRange(5) 
recursiveRange(6) = 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 10 + recursiveRange(9)

recursiveRange(n) = n + recursiveRange(n - 1)

Step 2: Base case - the stopping criterion
- n == 0

Step 3: Unintentional case - the constraint
- Float or integer
- No negative number?
"""

def recursiveRange(num):
    assert float(num) == num or int(num) == 0, 'The input must be float or integer!'
    if num <= 0:
        return num
    return num + recursiveRange(num - 1)

print(recursiveRange(6))
print(recursiveRange(10))
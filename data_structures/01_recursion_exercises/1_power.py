"""
Write a function called power which accepts a base and an exponent. 
The function should return the power of the base to the exponent. 
This function should mimic the functionality of math.pow() - do not worry 
about negative bases and exponents.

Step 1: Recursive case - the flow
power(2, 0) # 1
power(2, 2) # 4
power(2, 4) # 16

2^0 = 2 ** 0
2^2 = 2 * 2
2^4 = 2 * 2 * 2 * 2

power(base, exp) = base * power(base, exp - 1)

Step 2: Base case - the stopping criterion
- base = 0

Step 3: Unintentional case - the constraint
- Real number
"""

def passConstraint(val):
    return isinstance(val, float) or isinstance(val, int)

def power(base, exponent):
    assert passConstraint(base), "Input value must be float or integer"
    assert passConstraint(exponent), "Input value must be float or integer"
    if exponent <= 0:
        return base ** exponent
    return base * power(base, exponent - 1)

print(power(2, 3))

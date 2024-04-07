"""
Programming Challenge: Factorial
"""

def factorial(num):
    number_2 = 1
    for number in range(1, num + 1): 
        # factorial: 1 x 2 x 3 x ... x num
        number_2 = number_2 * number
    return number_2

print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))


def factorial_forward(num):
    # factorial: num x ... x 3 x 2 x 1 
    number_2 = 1
    for number in range(num, 0, -1):
        number_2 = number_2 * number
    return number_2

print(factorial_forward(3))
print(factorial_forward(4))
print(factorial_forward(5))
print(factorial_forward(6))
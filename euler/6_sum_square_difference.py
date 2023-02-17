"""
Copyright (c) 2022, Lewis Chen
All rights reserved.

This source code is licensed under the MIT-style license found in the
LICENSE file in the root directory of this source tree. 
"""

def sum_square_difference():
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the 
    first ten natural numbers and the square of the sum is 
    3025 - 385 = 2640.
    Find the difference between the sum of the squares of the 
    first one hundred natural numbers and the square of the sum.
    """
    sum_of_squares = 0
    square_of_sums = 0
    for i in range(1, 101):
        sum_of_squares += i**2
        square_of_sums += i
    square_of_sums = square_of_sums**2
    difference = square_of_sums - sum_of_squares
    print('difference: ', difference)

sum_square_difference()
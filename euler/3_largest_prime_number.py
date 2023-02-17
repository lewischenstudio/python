"""
Copyright (c) 2022, Lewis Chen
All rights reserved.

This source code is licensed under the MIT-style license found in the
LICENSE file in the root directory of this source tree. 
"""
import time

def largest_prime_factor(number):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?
    """
    a = number
    n = 2
    factors = []
    t = time.time()
    while n > 1:
        if a % n == 0:
            a = a / n
            factors.append(n)
        else:
            n += 1
        if a / n < 1:
            break
    elapsed = time.time() - t
    print('elapsed ', elapsed)
    print('factors: ', factors)
    prod = 1
    for i in factors: prod = prod * i
    print(prod)
    print('largest prime: ', factors[-1])

number = 13195
number = 600851475143
largest_prime_factor(number)

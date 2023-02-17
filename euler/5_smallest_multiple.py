"""
Copyright (c) 2022, Lewis Chen
All rights reserved.

This source code is licensed under the MIT-style license found in the
LICENSE file in the root directory of this source tree. 
"""
import time

def smallest_multiple_1(initial, start, end):
    """
    2520 is the smallest number that can be divided by each of the numbers 
    from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the 
    numbers from 1 to 20?
    This is algorithm is very optimized
    """
    a = initial
    t = time.time()
    primes = []
    not_primes = []
    factors = []

    # Obtain the list of primes, non-primes and common factors
    for i in range(start, end + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        else:
            not_primes.append(i)
            for i in not_primes:
                for j in range(1, i+1):
                    if i % j == 0 and j not in factors:
                        factors.append(j)
    
    # Multiply the number by the primes since they don't share common factors
    for i in primes:
        a = a * i
    
    # If the value is evenly divisible then break the while loop
    # Add the last prime to the initial value
    while a > 0:
        b = 0
        for j in range(1, end + 1):
            if a % j == 0:
                b += 1
        if b == end:
            break
        # this step greatly shortens the time
        a += primes[-1]
    elapsed = time.time() - t
    print('elapsed ', elapsed)
    for i in range(1, end + 1):
        print(f'a / {i}: ', a / i)
    print('result: ', a)


def smallest_multiple_2(initial, end):
    """
    Correct but very slow and resourceful code
    """
    if end > 17:
        print('This will take a long time.\n'
            'Use smallest_multiple_1() instead.')
        return None

    a = initial
    t = time.time()
    while a > 0:
        b = 0
        for i in range(1, end + 1):
            if a % i == 0:
                b += 1
        if b == end:
            break
        a += 1
    elapsed = time.time() - t
    print('elapsed ', elapsed)
    print('a2: ', a)
    print(f'a / {b}: ', a / b)

a = 2520
end = 22 #
smallest_multiple_1(a, 11, end)
# smallest_multiple_2(a, end)

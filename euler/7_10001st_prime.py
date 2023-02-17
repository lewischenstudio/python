"""
Copyright (c) 2022, Lewis Chen
All rights reserved.

This source code is licensed under the MIT-style license found in the
LICENSE file in the root directory of this source tree. 
"""
import time
import math

def find_that_prime(place):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    """
    primes = [2, 3, 5, 7]
    if place < 5:
        return primes[place - 1]
    a = 2
    t = time.time()
    factor = 2
    if place > 2000:
        factor = int(place / 1000)
    while a > 1:
        divisible = False
        if a % 2 == 0 or \
            a % 3 == 0 or \
            a % 4 == 0 or \
            a % 5 == 0 or \
            a % 6 == 0 or \
            a % 7 == 0 or \
            a % 8 == 0 or \
            a % 9 == 0 or \
            a % 10 == 0:
            divisible = True
        if not divisible:
            primes.append(a)
        a += 1
        if len(primes) >= factor * place:
            break
    new_primes = []
    for i in range(len(primes)):
        number = primes[i]
        before = primes[0:i]
        is_prime = True
        for item in before:
            if number % item == 0:
                is_prime = False
                break
        if is_prime:
            new_primes.append(number)
    elapsed = time.time() - t
    print('last prime: ', primes[-1])
    print('elapsed: ', elapsed)

find_that_prime(100)
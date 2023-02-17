"""
Copyright (c) 2022, Lewis Chen
All rights reserved.

This source code is licensed under the MIT-style license found in the
LICENSE file in the root directory of this source tree. 
"""
import time

def largest_palindrome_product_1(number):
    """
    A palindromic number reads the same both ways. The largest palindrome 
    made from the product of two 2-digit numbers is 9009 = 91 x 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    This is a slightly slower version
    """
    t = time.time()
    smallest = int(number * 0.1)
    largest = 0
    get_i = 0
    get_j = 0
    for i in range(number, smallest, -1):
        for j in range(i, smallest, -1):
            if str(i * j) == str(i * j)[::-1] and i * j >= largest:
                largest = i * j
                get_i = i
                get_j = j
                break
    elapsed = time.time() - t
    print('elapsed ', elapsed)
    print(f'product is {get_i} x {get_j}')
    print(f'palindrome is {largest}')


def largest_palindrome_product_2(number):
    """
    A palindromic number reads the same both ways. The largest palindrome 
    made from the product of two 2-digit numbers is 9009 = 91 x 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    This is a slightly faster version
    """
    t = time.time()
    smallest = int(number * 0.1)
    largest = 0
    get_i = 0
    get_j = 0
    count = 0
    for i in range(number, smallest, -1):
        found_palindrome = False
        for j in range(i, smallest, -1):
            if str(i * j) == str(i * j)[::-1]:
                found_palindrome = True
                break
        if found_palindrome and i * j >= largest:
            largest = i * j
            get_i = i
            get_j = j
            count += 1
        # this assumes there is always a palindrome greater than this
        if largest >= number**2 * 0.99:
            break
    elapsed = time.time() - t
    print('elapsed ', elapsed)
    print(f'product is {get_i} x {get_j}')
    print(f'palindrome is {largest}')


def quick_sort(arr):

    elements = len(arr)

    # Base case
    if elements < 2:
        return arr
    
    current_index = 0 # Index of the partitioning element

    for i in range(1, elements):
        if arr[i] <= arr[0]:
            current_index += 1
            temp = arr[i]
            arr[i] = arr[current_index]
            arr[current_index] = temp
    
    temp = arr[0]
    arr[0] = arr[current_index] 
    arr[current_index] = temp #Brings pivot to it's appropriate position

    left = quick_sort(arr[0:current_index]) #Sorts the elements to the left of pivot
    right = quick_sort(arr[current_index+1:elements]) #sorts the elements to the right of pivot

    arr = left + [arr[current_index]] + right #Merging everything together
    return arr

# largest_palindrome_product_1(9999)
largest_palindrome_product_2(9999)
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minSwapsRequired' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def minSwapsRequired(s):
    # Write your code here
    # Write your code here
    # count ones and zeros
    count_0 = s.count('0')
    count_1 = s.count('1')
    # what is the condition that tells if it cannot be a palindrome?
    # do that here
    print('hi')
    print('s[::1]: ', s == s[::-1])
    # check if s is already a palindrome:
    if s == s[::-1]:
        return 0
    # if it is not a palindrome, then do the following:
    new_s = [i for i in s]
    print('new_s: ', new_s)
    # loop through every item
    # i = current position
    # this double loop is trying to determine the position of item
    # to be swap once.
    # the idea is to locate the current position, look for the 
    # rest of the string to see if swapping 1 to 0 or vice versa
    # can result a palindrome or not. If not, then swap the current 
    # position to the opposite value than its own. Given the new swapped
    # list, loop through the rest of the items again until the entire list
    # is a palindrome. 
    positions = []
    for i in range(len(new_s) -1):
        rest = new_s[i+1:]
        for j in range(len(rest)):
            new_rest = new_s[i+1:]
            print('new_rest 1: ', new_rest)
            if new_rest == new_rest[::-1]:
                positions.append(i+j)
                print('found 1')
                print('j: ', j)
                break
            else:
                if rest[j] == '1':
                    new_rest[j] = '0'
                elif rest[j] == '0':
                    new_rest[j] = '1'
                print('new_rest 2: ', new_rest)
                if new_rest == new_rest[::-1]:
                    positions.append(j+1)
                    print('found 2')
                    print('j: ', i+j)
                    break
        print('j: ', j)
    print('positions: ', positions)
    
    # now we found the positions to swap items
    # count the minimun number of times it takes 
    # to swap in the positions to make a new palindrome
    temp_s = new_s
    for i in range(len(positions)):
        index = positions[i]
        if index <= 1:
            temp = temp[0]
            temp_s[0] = temp_s[index]
            temp_s[index] = temp
        else:
            temp = temp_s[index]
            temp_s[index] = temp_s[index+1]
            temp_s[index+1] = temp
        if temp_s == temp_s[::-1]:
            break
    print('temp_s: ', temp_s)
    print('i: ', i+1)

    
            #     print('rest: ', rest)
        # try to swap the left item with the right item and regroup to the new string
        # left_string = [new_s[i]]
        # right_string = [new_s[i+1]]
        # swap
        # temp_string = new_s[:i] + right_string + left_string
        # print('new_s: ', new_s)
        # break
    # print('temp_string: ', temp_string)

minSwapsRequired('0100101')
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = minSwapsRequired(s)

#     fptr.write(str(result) + '\n')

#     fptr.close()


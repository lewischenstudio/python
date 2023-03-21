"""
Pairs

Write a function to find all pairs of an integer array whose sum is equal to a given number.
"""

def pair_sum(myList, sum):
    arr = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum:
                arr.append(f'{myList[i]}+{myList[j]}')
    return arr

print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))


def pairSum(myList, sum):
    result = []
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if myList[i] + myList[j] == sum:
                result.append(str(myList[i]) +"+"+ str(myList[j]))
    return result
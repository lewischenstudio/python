"""
Best Score

Given a list, write a function to get first, second best scores from the list.
List may contain duplicates.
"""

def first_second(arr):
    first = 0
    second = 0
    for number in arr:
        if number >= first:
            second = first
            first = number
        if number > second and number != first:
            second = number
    return (first, second)

myList = [84,85,86,85,90,85,83,23,45,87,84,1,2,0]
print(first_second(myList)) # 90 87

def firstSecond(given_list):
    a = given_list   #make a copy
    a.sort(reverse=True)
    print(a)
    first = a[0]
    second = None
    print('given_list: ', given_list)
    for element in given_list:
        if element != first:
            second = element
            return first, second

print(firstSecond(myList))
"""
Write a recursive function called flatten which accepts an array of arrays and returns a new array with all values flattened.

Step 1: Recursive case - the flow
flatten([1, 2, 3, [4, 5]]) # [1, 2, 3, 4, 5]
flatten([1, [2, [3, 4], [[5]]]]) # [1, 2, 3, 4, 5]
flatten([[1], [2], [3]]) # [1, 2, 3]
flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) # [1, 2, 3]

if arr[0] is an array:
    return flatten([arr[0][0]] + arr[1:])
return [arr[0]] + flatten(arr[1:])

someRecursive(arr, callBack) = someRecursive(arr[1:], callBack)

Step 2: Base case - the stopping criterion
- length is 0

Step 3: Unintentional case - the constraint
- Array only
"""

def flatten(arr):
    assert isinstance(arr, list), "Input must be an array!"
    if len(arr) == 0:
        return arr
    if isinstance(arr[0], list):
        if len(arr[0]) > 1:
            return flatten([arr[0][0]] + [arr[0][1:]] + arr[1:])
        return flatten([arr[0][0]] + arr[1:])
    return [arr[0]] + flatten(arr[1:])

print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]])) # [1, 2, 3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3]

def flatten_for(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else: 
            resultArr.append(custItem)
    return resultArr

print(flatten_for([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
print(flatten_for([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
print(flatten_for([[1], [2], [3]])) # [1, 2, 3]
print(flatten_for([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3]

"""
Write a recursive function called someRecursive which accepts an array and a callback.
The function returns true if a single value in the array returns true when passed to the callback.
Otherwise it returns false.

Step 1: Recursive case - the flow
someRecursive([1,2,3,4], isOdd) # true
someRecursive([4,6,8,9], isOdd) # true
someRecursive([4,6,8], isOdd) # false

someRecursive(arr, callBack) = someRecursive(arr[1:], callBack)

Step 2: Base case - the stopping criterion
- length is 1

Step 3: Unintentional case - the constraint
- Array only
"""

def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def someRecursive(arr, cb):
    assert isinstance(arr, list) and len(arr) > 0, "Input value must be a non-empty array!"
    if len(arr) == 1:
        return cb(arr[0])
    if cb(arr[0]):
        return cb(arr[0])
    return someRecursive(arr[1:], cb)

print(someRecursive([1,2,3,4], isOdd)) # true
print(someRecursive([4,6,8,9], isOdd)) # true
print(someRecursive([4,6,8], isOdd)) # false
"""
Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each string in the array.

Step 1: Recursive case - the flow
capitalizeFirst(['car', 'taco', 'banana']) # ['Car','Taco','Banana']

capitalizeFirst(arr) = capitalize(arr[0]) + capitalizeFirst(arr[1:])

Step 2: Base case - the stopping criterion
- length is 0

Step 3: Unintentional case - the constraint
- Array of strings only
"""

def passConstraint(arr):
    for item in arr:
        if not isinstance(item, str):
            return False
    return True

def capitalizeFirst(arr):
    assert type(arr) is list, "Input must be an array!"
    assert passConstraint(arr), "Each item in the array must be string!"
    if len(arr) == 0:
        return []
    return [arr[0][0].upper() + arr[0][1:]] + capitalizeFirst(arr[1:])

print(capitalizeFirst(['car', 'taco', 'banana'])) # ['Car','Taco','Banana']

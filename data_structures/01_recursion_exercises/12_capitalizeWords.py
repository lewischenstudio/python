"""
Write a recursive function called capitalizeWords. Given an array of words, 
return a new array containing each word capitalized.

Step 1: Recursive case - the flow
words = ['i', 'am', 'learning', 'recursion']
capitalizeWords(words) # ['I', 'AM', 'LEARNING', 'RECURSION']

capitalizeWords(arr) = arr[0].upper() + capitalizeWords(arr[1:])

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

def capitalizeWords(arr):
    assert type(arr) is list, "Input must be an array!"
    assert passConstraint(arr), "Each item in the array must be string!"
    if len(arr) == 0:
        return []
    return [arr[0].upper()] + capitalizeWords(arr[1:])

words = ['i', 'am', 'learning', 'recursion']
print(capitalizeWords(words)) # ['I', 'AM', 'LEARNING', 'RECURSION']
"""
Write a function called productOfArray which takes in an array of numbers and 
returns the product of them all.

Step 1: Recursive case - the flow
productOfArray([1,2,3]) #6
productOfArray([1,2,3,10]) #60

poa([1,2,3]) = 1 * 2 * 3 = 1 * poa([2, 3])
poa([1,2,3,10]) = 1 * 2 * 3 * 10 = 1 * poa([2,3,10])

poa(array) = poa[0] * poa[1: length]

Step 2: Base case - the stopping criterion
- n <= 1

Step 3: Unintentional case - the constraint
- Array of float or integer
"""

def productOfArray(arr) -> float:
    for i in arr:
        assert float(i) == i or int(i) == i, "Each item in the array must be float or integer!"
    if len(arr) <= 1:
        return arr[0]
    return arr[0] * productOfArray(arr[1:len(arr)])

print(productOfArray([1,2,3]))
print(productOfArray([1,2,3,10]))
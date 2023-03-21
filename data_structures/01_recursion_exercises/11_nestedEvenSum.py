"""
Write a recursive function called nestedEvenSum. Return the sum of all even numbers in an 
object which may contain nested objects.

Step 1: Recursive case - the flow
nestedEvenSum(obj1) # 6
nestedEvenSum(obj2) # 10

Step 2: Base case - the stopping criterion
- length is 0

Step 3: Unintentional case - the constraint
- Object only
"""

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

def nestedEvenSum(obj, sum=0):
    assert type(obj) is dict, "Input must be an object!"
    new_sum = sum
    for value in obj.values():
        if type(value) is dict:
            new_sum = nestedEvenSum(value, new_sum)
        elif type(value) is float or type(value) is int:
            if value % 2 == 0:
                new_sum = new_sum + value
    return new_sum

print(nestedEvenSum(obj1)) # 6
print(nestedEvenSum(obj2)) # 10
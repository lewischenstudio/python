"""
Write a function called stringifyNumbers which takes in an object and finds all 
of the values which are numbers and converts them to strings. Recursion would be 
a great way to solve this!

Step 1: Recursive case - the flow
stringifyNumbers(obj) -> numbers become strings

Step 2: Base case - the stopping criterion
- length is 0

Step 3: Unintentional case - the constraint
- Object only
"""

def stringifyNumbers(obj):
    new_obj = {}
    for key, value in obj.items():
        if type(value) is dict:
            new_obj[key] = stringifyNumbers(value)
        elif type(value) is float or type(value) is int:
            new_obj[key] = str(value)
        else:
            new_obj[key] = value
    return new_obj


obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

print(stringifyNumbers(obj))
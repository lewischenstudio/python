"""
Write a function called collectStrings which accepts an object and returns an
array of all the values in the object that have a typeof string.

Step 1: Recursive case - the flow
stringifyNumbers(obj) -> numbers become strings

Step 2: Base case - the stopping criterion
- length is 0

Step 3: Unintentional case - the constraint
- Object only
"""


def collectStrings(obj):
    arr = []
    for value in obj.values():
        if type(value) is str:
            arr.append(value)
        elif type(value) is dict:
            arr.extend(collectStrings(value))

    return arr


obj = {
    "stuff": "foo",
    "data": {
        "val": {
            "thing": {
                "info": "bar",
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": "baz",
                    }
                },
            }
        }
    },
}

print(collectStrings(obj))  # ['foo', 'bar', 'baz']

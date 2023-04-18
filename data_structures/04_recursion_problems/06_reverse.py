"""
Write a recursive function called reverse which accepts a string and returns a new string in reverse.

Step 1: Recursive case - the flow
reverse('python') # 'nohtyp'
reverse('appmillers') # 'srellimppa'

reverse(string) = string[-1] + reverse(string[0:-1])

Step 2: Base case - the stopping criterion
- length = 1

Step 3: Unintentional case - the constraint
- String only
"""


def reverse(strng):
    assert isinstance(strng, str), "Input must be a string!"
    str_to_list = list(strng)
    if len(str_to_list) == 1:
        return str_to_list[0]
    return str_to_list[-1] + reverse("".join(str_to_list[0:-1]))


print(reverse("python"))
print(reverse("appmillers"))

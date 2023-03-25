"""
Write a recursive function called isPalindrome which returns true if the string passed 
to it is a palindrome (reads the same forward and backward). Otherwise it returns false.

Step 1: Recursive case - the flow
isPalindrome('awesome') # false
isPalindrome('foobar') # false
isPalindrome('tacocat') # true
isPalindrome('amanaplanacanalpanama') # true
isPalindrome('amanaplanacanalpandemonium') # false

if first letter == last letter:
    return true
else:
    return 0

isPalindrome('tacocat') = 1 + isPalindrome('acoca')

Step 2: Base case - the stopping criterion
- length = 1 return true
- length = 2 return first letter == last letter

Step 3: Unintentional case - the constraint
- String only
"""


def isPalindrome(strng):
    assert str(strng) == strng, "Input value must be string!"
    str_to_list = list(strng)
    if len(str_to_list) == 1:
        return True
    if len(str_to_list) == 2:
        return str_to_list[0] == str_to_list[1]
    if str_to_list[0] == str_to_list[-1]:
        return isPalindrome("".join(str_to_list[1 : len(str_to_list) - 1]))
    return False


print(isPalindrome("awesome"))  # false
print(isPalindrome("foobar"))  # false
print(isPalindrome("tacocat"))  # true
print(isPalindrome("amanaplanacanalpanama"))  # true
print(isPalindrome("amanaplanacanalpandemonium"))  # false
print(isPalindrome("1001001"))  # true

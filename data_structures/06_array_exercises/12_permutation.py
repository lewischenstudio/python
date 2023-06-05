""""Coding Exercise 12: Permutation"""


def permuntation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


print(permuntation([1, 2, 3], [3, 2, 1]))
print(permuntation(["a", "c", "b"], ["c", "a", "b"]))

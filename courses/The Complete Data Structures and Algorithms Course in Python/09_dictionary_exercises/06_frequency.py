"""Coding Exercise 06: Same Frequency"""


def check_same_frequency(list1, list2):
    for item in list1:
        if list1.count(item) == list2.count(item):
            pass
        else:
            return False
    return True


def check_same_frequency2(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter

    return count_elements(list1) == count_elements(list2)

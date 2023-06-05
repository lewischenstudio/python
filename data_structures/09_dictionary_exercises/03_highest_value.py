"""Coding Exercise 03: Key with the Highest Value"""


def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)

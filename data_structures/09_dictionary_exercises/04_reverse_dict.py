"""Coding Exercise 04: Reverse Key-Value Pairs"""


def reverse_dict(my_dict):
    return {v: k for k, v in my_dict.items()}

"""Coding Exercise 6: Common Elements"""


def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

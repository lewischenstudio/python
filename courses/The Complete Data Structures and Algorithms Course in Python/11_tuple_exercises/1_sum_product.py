"""Coding Exercise 1: Sum and Product"""


def sum_product(t):
    sum_result = 0
    product_result = 1

    for num in t:
        sum_result += num
        product_result *= num

    return sum_result, product_result

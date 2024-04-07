"""
Introduction
"""

print("hello world")

print("How could he be born so easily tricked by this phony scheme?")
print("My grade changes depending on my performance")

"""
Variable
A variable is an element, feature or factor that is likely to vary or change.
In Python, a variable is a thing that can be changed.
E.g., x = 10
"""
# x is called the variable's name
# 10 is called the variable's value
x = 10

# ex_var is the variable's name
# 5 is the variable's value
ex_var = 5

# This process is called "Assignment"
# As programmers, we assign the value 50 to the variable "hello"
hello = 50

# We can assign a different value to the existing variable
ex_var = 7

"""
JavaScript naming rule: cambleCase, e.g., helloWorld = 10
Python naming rule: snake case: e.g., hello_world = 10
"""

"""
Basic Data Types:
Floating numbers
Integers
Booleans
"""


"""
Components and Math Operations
"""
addition = 4 + 5
subtraction = 5 - 2
division = 7 / 2
multiplication = 3 * 8

# Exponentiation, Floor Division and Modulo
exponentiation = 4 ** 4  # 256
floor_division = 16 // 5  # 3
modulo = 7 % 3  # 1
my_modulo = 21 % 3
print("my_modulo: ", my_modulo)

# Assignment Operators
add_assign = 5
# add_assign = add_assign + 7
add_assign += 7
print("add_assign: ", add_assign)
# Subtraction
sub_assign = 10
sub_assign -= 5
# Multiplication
mult = 10
mult *= 5
# Division 
div = 10
div /= 5
# Exponentiation
exp = 5
exp **= 3 # =5*5*5=25*5=125
# Floor division
floor = 10
floor //=6
# Modulo
mod = 10
mod %= 7

# Operator Procedence
# ()
# **
# %, /, //, and *
# + and -
res = (10 + 8) ** 2 / 3 // (2 * (9 - 7))
print("res: ", res)

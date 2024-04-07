## Section 04: Functions

#### Table of Contents

- functions
- function with no parameters exercise
- function with no parameters exercise solution
- function with 1 parameter exercise
- function with 1 parameter exercise solution
- Programming Challenge: Volume of a Rectangular Prism
- Volume of a Rectangular Prism Solution
- Programming Challenge: Celsius to Fahrenheit
- Celsius to Fahrenheit Solution with integers
- Celsius to Fahrenheit Solution with round()
- importing modules
- Programming Challenge: Miles Per Gallon
- Miles Per Gallon Solution
- variable scope
- Quiz 3: variable scope quiz

### functions

```python
def prints_four():
    print("this")
    print("is")
    print("an")
    print("example")

print_four()
print_four()
print_four()
print_four()
print_four()

def addition_function(a, b):
    print(a + b)


```

This function `addition_function(a, b)` takes two parameters `a` and `b` and
prints the addition of the two values.

#### Defining a function

```python
def function_name():
    print(2 + 2)
```

#### Calling a function

```python
function_name()
```

#### Function parameters

```python
def function_name(parameter):
    print(parameter + 2)

function_name(8)
```

#### Multiple parameters

```python
def function_name(p1, p2, p3):
    print(p1 + p2 + p3)

function_name("I", "like", "chocolate")

def function_name(p1, p2, p3):
    print(str(p1) + str(p2) + str(p3))

function_name("I", "like", "chocolate")
function_name("I", "1", "chocolate")
function_name("I", 1, "chocolate")
function_name("I", 2.2, "chocolate")
function_name("I", 1, 1)
function_name(1, 1, 1)

first_str = "The number "
def function_name(p1, p2, p3):
    print(p1 + str(p2) + p3)

function_name(first_str, 5, " is an integer.")
```

#### Default parameters

```python
def default_example(num1=7, num2=8):
    print(num1 * num2)

default_example() # 56
default_example(1) # 8
default_example(3,2) # 6
```

#### Return

```python
def default_example(num1=7, num2=8):
    print(num1 * num2)
    return num1 * num2

default_example() # 56
default_example(1) # 8
default_example(3,2) # 6
```

#### Using return with expressions

```python
def default_example(num1=7, num2=8):
    return num1 * num2

print(default_example())
print(default_example() + 44)
```

#### Return type

```python
def none_example():
    print('hello')
    # return None (this is optional as None is the default return)

# NoneType because it's not returning anything
# or it only returns None
type(none_example()) # <class 'NoneType'>

def str_example():
    return 'Hello'

def int_example():
    return 10

def float_example():
    return 1.0

type(str_example()) # <class 'str'>
type(int_example()) # <class 'int'>
type(float_example()) # <class 'float'>
```

### function with no parameters exercise

Do all of this in a .py file in Pycharm.

- Create a function called `hello_world_printer()` which takes no parameters and
  prints the string "hello world"
- Call the function `hello_world_printer()`

```python
def hello_world_printer():
    print('hello world')

hello_world_printer()
```

### function with no parameters exercise solution

```python
def hello_world_printer():
    print("hello world")


hello_world_printer()
```

### function with 1 parameter exercise

Do all of this in a .py file in Pycharm

- Create a function called name_printer which takes 1 parameter and prints it
- Create a variable called name and assign it user `input()`. input()'s message
  should ask the user to enter their name.

```python
def name_printer(parameter):
    print(parameter)

name = input("Enter your name.")
name_printer(name)
```

### function with 1 parameter exercise solution

```python
def name_printer(user_name):
    print(user_name)


name = input("Please enter your name.")
name_printer(name)
```

### Programming Challenge: Volume of a Rectangular Prism

For this programming challenge, you will be creating a function that calculates
the volume of a rectangular prism in cubic feet. The formula to find the volume
of a rectangular prism is V = L x W x H where L, W and H are length, width, and
height, respectively.

First, create three variables representing length, width, and height. Assign
each of them an integer as **user input** using the `input()` function and
`int()`.

Next, create a function to calculate the volume of the rectangular prism. It
should have 3 parameters representing length, width, and height and return the
volume of a rectangular prism calculated using those 3 parameters.

Finally, use `print()` to display "The volume of the rectangular prism is [call
function here to calculate volume] cubic feet." in the output. You will have to
use `str()` on the function call to be able to concatenate it with strings since
it returns an integer.

```python
L = int(input("Length: "))
W = int(input("Width: "))
H = int(input("Height: "))

def volume(length, width, height):
    return length * width * height

volume(length, W, H)
print("The volume of the rectangular prism is " + str(volume(L, W, H)) + " cubic feet.")
```

#### Scope

```python
p1 = "hello world"
p2 = 10
w1 = True
w2 = 1.23
def just_a_printer(parameter):
    n1 = "here"
    n2 = 20
    print(n1)
    print(n2)
    print(w1)
    print(w2)
    print(parameter)

w3 = "yes"
just_a_printer(w3)
```

### Volume of a Rectangular Prism Solution

```python
length = int(input("Enter an integer that represents length in feet."))
width = int(input("Enter an integer that represents width in feet."))
height = int(input("Enter an integer that represents height in feet."))


def prism_vol(l, w, h):
    return l * w * h


print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")
```

### Programming Challenge: Celsius to Fahrenheit

The formula for converting from degrees Celsius to degrees Fahrenheit is as
follows:

F = 1.8 x C + 32

Where F is the Fahrenheit temperature and C is the Celsius temperature.

In a .py file, create a variable and assign it an integer representing a celsius
temperature that is entered as user `input()`. `input()`'s message should prompt
the user to enter an integer value.

For this programming challenge, you will then write a function called
`fahrenheit` that takes in **an integer** representing a **Celsius temperature**
as its argument. The function will return the Fahrenheit equivalent temperature
of that argument to 1 place after the decimal.

At the end of your program, display the Fahrenheit equivalent in a print
statement message formatted like so: "The Fahrenheit equivalent of [user entered
integer] degrees Celsius is [number returned by function]".

To make sure that the function works, run your program multiple times and call
the function on different user entered integer values both negative and
positive.

```python
celsius = int(input("Enter an integer value for Celsius temperature: "))

def fahrenheit(parameter):
    return 1.8 * parameter + 32

print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)))
```

### Celsius to Fahrenheit Solution with integers

```python
celsius = int(input("Please enter an integer value for degrees celsius. "))

def fahrenheit(cel):
    # To avoid the approximation error that would occur if the float 1.8 was used in the calculation, 1.8 * 10 is used
    # instead, resulting in the integer 18.  To balance this out, 32 is also multiplied by 10 to get 320.  After the
    # calculations in the parentheses are finished, the result is divided by 10, which gives the correct Fahrenheit
    # temperature.
    return (18 * cel + 320) / 10

print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")
```

### Celsius to Fahrenheit Solution with round()

```python
celsius = int(input("Please enter an integer value for degrees celsius. "))

def fahrenheit(cel):
    # The second argument of round() is 1 since we only want the Fahrenheit temperature to be displayed with 1 number
    # after the decimal point
    return round((1.8 * cel + 32), 1)

print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")
```

### importing modules

#### Module Import

```python
import random

print(random.randint(1, 10))
```

#### Function Import

```python
from random import randint

print(randint(1, 10))
```

#### Universal Import (not recommended)

```python
from random import *

random()
```

### Programming Challenge: Miles Per Gallon

For this exercise, you will create a program that approximates the number of
miles per gallon that a car gets.

In a .py file, create two variables, one which will hold a randomly generated
integer between 10 and 25 (inclusive of both 10 and 25), and another which will
hold a randomly generated integer between and inclusive of 200 and 400. The
first variable represents the number of gallons of gas that the car's fuel tank
holds. The second variable represents the miles that the car can travel on a
full tank before needing a refuel.

Using the formula miles per gallon (MPG) = miles driven/gallons used, calculate
the car's MPG and display it in the output using print(). Use floor division
instead of regular division for this calculation to get an integer instead of a
float. This will give a realistic approximation of miles per gallon even though
floats such as 19.8 round down a large amount when using floor division since
sometimes, car manufacturers sometimes exaggerate miles per gallon. In addition,
display the values held in the variables you created for gallons of gas in the
car's fuel tank and miles it can travel on a full tank with two different print
statements.

[Gas](/04_functions/gas.py)

### Miles Per Gallon Solution

```python
from random import randint
# generates random integer between and inclusive of 10 and 25 to represent gas in the car's fuel tank
fuel = randint(10, 25)
# generates random integer between and inclusive of 200 and 400 to represent miles the car can go without refueling
miles = randint(200, 400)
# calculates and displays the MPG of the car assuming car manufacturers overestimates in their claims
print("The car can travel " + str(miles // fuel) + " miles per gallon.")
# displays the number of gallons of fuel that the car's fuel tank can hold
print("The car's fuel tank can hold " + str(fuel) + " gallons.")
# displays the number of miles that the car can travel on a full tank
print("The car can travel " + str(miles) + " miles on a full tank.")
```

### variable scope

```python
example = "hello world"

def loc_ex():
    example = "this is a string"
    haa = "hsdfadf"
    return example

def adf():
    return haa # NameError

print(example)
print(loc_ex)
```

#### Why is understanding variable scope important?

- Local variables cannot be used by code in the global scope.
- Global variables can be accessed by code in a local scope.
- The local scope of one function can't be used variable from another function's
  local scope.
- You can use the same name for different variables as long as they are in
  different scopes. (Not recommended)

#### Local variables cannot be used by code in the global scope.

```python
def loc_ex():
    breakfast = "waffles"
    return breakfast

loc_ex()
print(breakfast) # NameError
```

#### Global variables can be accessed by code in a local scope.

```python
def print_glob():
    print(glob_var)

glob_var = "This is a string"
print_glob()
```

#### The local scope of one function can't be used variable from another function's local scope.

```python
def first():
    loc = 2
    return loc

def second():
    return loc

first()
second() # NameError
```

#### You can use the same name for different variables as long as they are in different scopes. (Not recommended)

```python
def loc_ex1():
    fruit = "pear"
    print(fruit)

def loc_ex2():
    fruit = "banana"
    print(fruit)

fruit = "apple"
loc_ex1()
loc_ex2()
print(fruit)
```

#### Global Statements

```python
def loc_ex():
    global fruit
    fruit = "pear"
    print(fruit)

fruit = "apple"
loc_ex()
print(fruit)
```

#### What is the point of scopes anyway?

Well, the answer is that having scopes compartmentalizes problems and helps to
quickly give you a better idea of where a problem involving a variable is
happening within your code. What that means is that, if there is a problem with
a local variable, scopes would give you a general idea of where the problem is
because you would know the local scope that covers the area where that local
variable is. For global variables, the same logic applies. If a problem occurs
with a global variable's value, having local scopes be separate from the global
scope means that you know that you don't need to waste time looking at local
scopes for errors. Also, because of the way local scopes are created and
destroyed in functions, programmers don't need to worry about code within each
individual local scope affecting things outside of it, whether that is code in
the global scope or another function's local scope. Provided that the function's
code is working, all that matters is what is returned from the function's local
scope.

### Quiz 3: variable scope quiz

#### Question 1:

What will the following program do if it is run?

```python
words = "hello world"
def hi_world():
    return words
print(hi_world())
```

"hello world" will be printed since words is a variable that is in the global
scope.

#### Question 2:

What will the following program do if it is run?

```python
def pi_returner():
    approx = 3.14
    return approx
print(pi_returner())
```

The variable approx is being accessed by `pi_returner()`'s call. This results in
3.14 being displayed in the output because approx belongs to pi_returner's local
scope, meaning that approx can be accessed anywhere within the `pi_returner()`
function.

#### Question 3:

What will the following program do if it is run?

```python
def float_holder():
    flo = 21.9
    return flo
float_holder()
print(flo)
```

flo is a local variable, meaning that it can only be accessed by the function
associated with it, float_holder(), not code in the global scope like the
`print()` statement at the bottom of the program.

#### Question 4:

What will the following program do if it is run?

```python
an_int = 50
def inty():
    an_int = 100
    return an_int
print(inty())
```

When it is called, `inty()` returns the value of the local variable an_int, not
the global variable an_int. 100 is printed as a result.

#### Question 5:

What will the following program do if it is run?

```python
an_int = 50
def inty():
    an_int = 100
    return an_int
print(an_int)
```

The program will print 50 since an_int is a global variable and the an_int
inside of `inty()` can only be accessed by calling `inty()`.

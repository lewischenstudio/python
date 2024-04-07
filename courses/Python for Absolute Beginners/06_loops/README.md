## Section 06: Loops

#### Table of Contents

- while loops
- While Loops Exercise
- While Loops Exercise Solution
- Programming Challenge: Sum of Numbers From A Positive Integer
- Sum of Numbers From a Positive Integer Solution
- for loops
- For Loops Exercise
- For Loops Exercise Solution
- Programming Challenge: Find The Number of Characters in A String
- Find The Number of Characters in A String Solution
- range()
- Quiz 6: range() quiz
- Programming Challenge: Fizz Buzz
- Fizz Buzz Solution
- Programming Challenge: Factorial
- Factorial Solution

### while loops

```python
counter = 0
while counter < 3:
    print("counter is " + str(counter) + " and print something")
    counter += 1
```

This is equivalent to the following code

```python
counter = 0
if counter < 3:
    print("counter is " + str(counter) + " and print something")
    counter += 1
if counter < 3:
    print("counter is " + str(counter) + " and print something")
    counter +1
if counter < 3:
    print("counter is " + str(counter) + " and print something")
    counter +1
```

#### Avoid Infinite Loops

#### Infinite Loop 1: counter += 0

```python
counter = 0
while counter < 30:
    print("counter = " + str(counter) + " and print something for " + str(counter))
    counter += 0
    print('after counter += 0, counter = ' + str(counter))
print('after the while loop, counter = ' + str(counter))
```

#### Infinite Loop 2: while counter >= 0

```python
counter = 0
while counter >= 0:
    print("counter = " + str(counter) + " and print something for " + str(counter))
    counter += 1
    print('after counter +=1, counter = ' + str(counter))
print('after the while loop, counter = ' + str(counter))
```

### While Loops Exercise

For this exercise, you will print 10 descending integers starting from 10 and
ending at 1 with each integer being 1 less than the last and each integer
printed on a new line.

Create a variable and assign it the integer 10.

Then, print

10 9 8 7 6 5 4 3 2 1

in the output by using a while loop to print numbers while the variable does not
equal 0. Use the `-=` operator to reassign descending values to the variable.

```python
counter = 10
while counter >= 1:
    print(counter)
    counter -= 1
```

### While Loops Exercise Solution

```python
dec_int = 10

while dec_int != 0:
    print(dec_int)
    dec_int -= 1
```

Below conditions are the same:

`while counter >= 1`

`while counter > 0`

`while counter != 0`

### Programming Challenge: Sum of Numbers From A Positive Integer

Write a program which gets a positive integer from a user using `input()` and
assigns it to a variable.

The program should then use a while loop to get the sum of all of the integers
from the integer that was entered by the user down to 1. For example, if the
integer entered by the user was 6, the while loop would find the sum of 6, 5, 4,
3, 2, and 1, which is 21.

At the bottom of your program create two print statements. One will display the
user entered integer and the other will display the sum found by the while loop.

[sum_of_integers.py](./sum_of_integers.py)

### Sum of Numbers From a Positive Integer Solution

```python
# pos_int is a variable which holds a user entered integer.
pos_int = int(input("Please enter a positive integer."))
# This variable stores the initial value of pos_int before it is used in the loop so
# that later it can be used to display pos_int's initial value in the output.
int_init = pos_int
# This is a variable which will be used to hold the sum of all the integers from pos_int.
summed = 0
# The while loop will run while pos_int's stored integer value is greater than 0
while pos_int > 0:
    # This is the equivalent of summed = summed + pos_int
    # In other words: new value of summed = old value of summed + new value of pos_int
    summed += pos_int
    # This will decrement pos_int so that pos_int will eventually equal 0 and the while
    # loop will stop running its code.
    pos_int -= 1

print(int_init)  # displays the initial value of pos_int
print(summed)    # displays the sum of integers from pos_int
```

### for loops

```python
word = "house"

for letter in word:
    print(letter)
```

### For Loops Exercise

Use a for loop to print each letter from the string "hello world".

```python
hello_world = "hello world"
for letter in hello_world:
    print(letter)
```

### For Loops Exercise Solution

```python
words = "hello world"

for letter in words:
    print(letter)
```

### Programming Challenge: Find The Number of Characters in A String

In a .py file, write a program which calculates the number of characters in a
string.

The string should be entered using `input()` and assigned to a variable.

Use `print()` twice at the end of your program. The first `print()` will print
the string that the user entered and the second `print()` will display the
number of characters in the string. For example, if the user entered the string
"hello world", the number of characters would be 11.

### Find The Number of Characters in A String Solution

```python
user_str = input("Please enter a string.")

count = 0  # This variable will be used to hold the number of characters in the string.
# This for loop adds 1 to count for each character in user_str.
for char in user_str:
    count += 1

print(user_str)
print(count)
```

### range()

`range()` is a function that creates a sequence of numbers to allow iterating
over each number.

#### One argument

Starts from 0 to 4

```python
one_input = range(5)

for num in one_input:
    print(num)
```

#### Two arguments

Starts from 5 to 9

```python
two_inputs = range(5, 10)
for num in two_inputs:
    print(num)
```

#### Three arguments

Prints 1 4 7 10 13 16 19

```python
three_inputs = range(1, 20, 3)

for num in three_inputs:
    print(num)
```

Prints 20 17 14 11 8 5 2

```python
three_inputs = range(20, 1, -3)

for counter in three_inputs:
    print(counter)
```

A while loop example for the above

```python
counter = 20

while counter > 1:
    print(counter)
    counter -= 3
```

### Quiz 6: range() quiz

#### Question 1:

What numbers are in the range() `range(3)`

0, 1 and 2

A range with 1 input starts at 0, goes up in increments of 1, and ends at 1 less
than its input, which in this case is 2.

#### Question 2:

What numbers does the `range(11, 16)` consist of?

11, 12, 13, 14 and 15

A range() with 2 inputs starts at the first input, and goes up in increments of
1 until 1 less than the second input is reached, which in this case is 15.

#### Question 3:

What numbers are in the range() below?

`range(10, 25, 5)`

10, 15 and 20

When range() is used with 3 inputs, it starts at the first input and goes up by
increments equal to the 3rd input until 1 less than the second input is reached.

#### Question 4:

What are the numbers that make up the range()

`range(6, -1, -2)`

6, 4, 2 and 0

This example starts at a high number and goes down from that since it has a
negative step argument. This example starts at 6, ends at 1 more than -1, and
goes down in increments of 2. Since 1 more than -1 is 0, it consists of the
numbers 6, 4, 2, and 0.

### Programming Challenge: Fizz Buzz

Write a program that iterates over the integers 1 through 50 using a loop.

However, for numbers which are multiples of both 3 and 5 print “FizzBuzz” in the
output. For example, 15 is divisible by both 3 and 5, so instead of printing 15,
print "FizzBuzz". For numbers which are multiples of 3 but not 5 (such as 42)
print “Fizz” instead of the number. For the numbers that are multiples of 5 but
not 3 (such as 20) print “Buzz” instead of the number.

All of the integers which are not multiples of 3 or 5 should just be printed as
themselves.

### Fizz Buzz Solution

```python
for num in range(1, 51):
    # If num is divisible by both 3 and 5, "FizzBuzz" will be printed.
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # If num is only divisible by 3, "Fizz" will be printed.
    elif num % 3 == 0:
        print("Fizz")
    # If num is only divisible by 5, "Buzz" will be printed.
    elif num % 5 == 0:
        print("Buzz")
    # num itself will be printed in all other cases.
    else:
        print(num)
```

### Programming Challenge: Factorial

Create a function which takes one positive integer as its input and returns its
factorial.

To make sure that your function works correctly, you should call it with the
inputs 3, 4, and 5 and print what is returned by those calls. For those inputs,
you should get 6, 24, and 120, respectively.

### Factorial Solution

```python
# The argument fac_num's name is short for factorial number.
def factorial(fac_num):
    # The local variable returned will be used in the for loop used to calculate fac_num's
    # factorial. To do this, it will be multiplied by decrementing values of
    # fac_num. Since it will be multiplied, it was given the initial value of 1.
    returned = 1
    # By the end of this for loop, returned will have been reassigned fac_num's factorial.
    for item in range(fac_num, 1, -1):
        returned *= item

    # returns returned, which now holds the value of fac_num's factorial
    return returned

print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(5))  # 120
```

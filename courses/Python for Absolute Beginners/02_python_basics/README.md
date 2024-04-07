## Section 02: Python Basics

#### Table of Contents

- Variables and Assignment
- Basic Data Types
- Variables and Assignment Exercises
- Variables and Assignment Exercises Solution
- Comments and Math Operators
- Quiz 1: Comments and Math Operators Quiz
- Comments and Math Operators Review Exercises
- Comments and Math Operators Review Exercise Solution
- print()
- print() exercises
- print() exercises solutions
- More On Floats
- Quiz 2: More On Floats Quiz
- Programming Challenge: Grocery Store Purchase
- Grocery Store Purchase Solution with integers
- Grocery Store Purchase Solution with round()


### Quiz 1: Comments and Math Operators Quiz

#### Question 1:

In Python, the symbol \* represents what math operator?

multiplication

#### Question 2:

What does the expression 11 % 3 evaluate to?

2

#### Question 3:

What does the expression 20 / 4 evaluate to?

5

#### Question 4:

What does the expression 15 / 3 _ 2 _ 2 - (3 + 4) evaluate to?

13

#### Question 5:

Suppose that you had a variable called number which has had the value 5 assigned
to it. If on a lower line, number \*\*= 3 was typed, what value would the
variable number be reassigned?

125

### Comments and Math Operators Review Exercises

#### Create a variable and assign it the sum of two integers

```python
abc = 2 + 3
```

#### Create a variable and assign it the difference (subtraction) of two integers

```python
milk = 7 - 2
```

#### Create a variable and assign it the result of one integer being divided by another integer

```python
potato = 35 / 7
```

#### Create a variable and assign it the product (multiplication) of two integers

```python
speaker = 3 * 7
```

#### Create a variable and assign it the result of 3 raised to the 8th power

```python
fan = 3 ** 8
```

#### Create a variable and assign it the result of 10 floor division 3

```python
switch = 10 // 3
```

#### Create a variable and assign it the integer 2 using the expression 17 modulo [number]

```python
box = 17 % 3
```

#### Answers

```python
summed = 2 + 3
difference = 10 - 8
divided = 1000 / 10
product = 7 * 5
exponent = 3 ** 8
floored = 10 // 3
mod = 17 % 15  # could have used 3, 5, or 15 to get 2 as a result
```

### print()

```python
example_1 = 10
print(example_1)
```

### print() exercises

#### Do all of this in a .py file in Pycharm. Make a comment for each line of code you write.

- create a variable, assign it a value of any data type, then use print() to
  display its assigned value in the output
- use print() to print a value of any data type directly
- use print() to display the result of an expression that uses at least 2 math
  operators

### More on Floats

```python
print(1.23 + 2.80)
# 4.0299999999999
```

The reason this is giving a lot of 9 is because Python is built on top of C++,
which estimates decimal numbers by fixed binary numbers.

#### Workaround 1

Dividing by an integer

```python
ex2 = (123 + 280) / 100
print(ex2)
# 4.03
```

#### Workaround 2

Use `round()` function

```python
ex3 = 1.23 + 2.80
print(round(ex3, 2))
```

### More On Floats Quiz

#### Question 1:

Suppose that in a .py file, you had the following line of code:

```python
summed = 3.14159 + 2.71828
```

If you wanted to round the sum assigned to the variable summed to 4 places using
`round()` and then display that sum, what would you type?

```python
print(round(summed, 4))
```

#### Question 2:

Suppose that you had a .py file with the following line of code in it:

```python
summed = 10.9 + 211.05
```

If you wanted to use integers instead of `round()` to get the correct sum of
these two floats, 221.95, what is the smallest multiple of 10 that you can
multiply them and divide them by to get integers?

100

Multiplying 10.9 and 211.05 by 100 results in 1090 and 21105. Dividing the sum
of those 2 integers by 100 like this (1090 + 21105) / 100 results in the correct
sum of 221.95.

### Programming Challenge: Grocery Store Purchase

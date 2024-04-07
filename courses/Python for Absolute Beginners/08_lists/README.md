## Section 08: Lists

#### Table of Contents

- introduction to lists
- introduction to lists exercises
- introduction to lists exercises solutions
- indexes and list slicing
- indexes and list slicing exercises
- indexes and list slicing exercises solutions
- del and list methods
- del and list methods exercises
- del and list methods exercises solutions
- Strings

### introduction to lists

```python
checked_list = [1, 2, 3, 4]
print(1 in checked_list) # True
print(8 in checked_list) # False
print(1 not in checked_list) # False
```

### introduction to lists exercises

Do all of this in a .py file in Pycharm.

1. Create a variable and assign it a list that contains an integer, a float, a
   Boolean value, a string, and a list of 3 integers.
2. Create another variable and assign it a call of the list() function with a
   string as its argument.
3. Use the keyword "in" to check if the letter "e" is in the list assigned to
   the variable from step 2 and print the result.
4. Use the keyword "not in" to check if the letter "a" is not in the list
   assigned to the variable from step 2 and print the result.

### introduction to lists exercises solutions

```python
mixed = [10, 4.97, True, "mountain", [9, 8, 7]]
li_str = list("cheese")
print("e" in li_str)
print("a" not in li_str)
```

### indexes and list slicing

```python
indexes_example = ["carpet", "hardwood", "linoleum"]
print(indexes_example[0])
print(indexes_example[1])
print(indexes_example[2])
```

```python
indexes_example = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(indexes_example[2][0])
```

#### Negative indexes

```python
negative = [1, 2, 3, 4, 5]
print(negative[-1])
print(negative[-2])
print(negative[-3])
print(negative[-4])
print(negative[-5])
```

```python
mixed = [False, 365, 4.24, "this is a string"]
print(mixed[2] + 1.76)
print("I have used \"" + mixed[-1] + "\" as an example of too many times.")
```

#### List slicing

```python
sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sliced[:4]) # [1, 2, 3, 4]
print(sliced[3:8]) # [4, 5, 6, 7]
print(sliced[6:]) # [7, 8, 9]
```

#### Reassigning a value

```python
example = [2, 4, 6, 8, 0]
print(example)
example[3] = 10
print(example) # [2, 4, 6, 10, 0]
example[1:4] = [3, 2, 1]
print(example) # [2, 3, 2, 1, 0]
example[4:7] = [7, 6, 5]
print(example) # [2, 4, 6, 8, 7, 6, 5]
```

### indexes and list slicing exercises

Do all of this in a .py file in Pycharm.

1. Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]
2. Access the first list from the list of lists in step 1 by index then print
   it.
3. Access the 14 from the list in step 1 then print it.
4. Create a second variable and assign it the list ["chair", "table", "desk",
   "lamp", "bed"]
5. Use a negative integer to access "chair" from the variable in step 4 by index
   then print it.
6. Print "Most people own at least 2 chairs." by concatenating the 2 from the
   list in step 1 and the "chair" from the list in step 4 with "Most people own
   at least ", a space, and a period.
7. Create a third variable and assign it the list [0.98, 8.76, 6.54, 4.32]
8. Print the slice [8.76, 6.54, 4.32] from the variable you created in step 7.
9. Print the slice [8.76, 6.54] from the variable you created in step 7.
10. Print the slice [0.98, 8.76] from the variable you created in step 7.

### indexes and list slicing exercises solutions

### del and list methods

### del and list methods exercises

### del and list methods exercises solutions

### Strings

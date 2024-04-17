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

```python
up_by_two = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(up_by_two[0])
print(up_by_two[3][1])
furniture = ["chair", "table", "desk", "lamp", "bed"]
print(furniture[-5])
print("Most people own at least " + str(up_by_two[0][1]) + " " + furniture[0] + "s.")
floats = [0.98, 8.76, 6.54, 4.32]
print(floats[1:])
print(floats[1:3])
print(floats[:2])
```

### del and list methods

```python
planets = ["pluto", "mars", "earth", "venus"]
del planets[0]
print(planets)
```

```python
planets = ["pluto", "mars", "earth", "venus"]
planets.remove("pluto")
planets.remove("urenus")
print(planets)
```

#### del vs remove()

```python
colors = ["blue", "red", "white", "blue", "orange", "blue"]
colors.remove("blue")
print(colors)
```

#### .append()

```python
pets = ["cat", "dog", "parrot"]
print(pets)
pets.append("fish")
print(pets) # ["cat", "dog", "parrot", "fish"]
```

#### .inert()

```python
pets = ["cat", "dog", "parrot"]
pets.insert(1, "turtle")
print(pets) # pets = ["cat", "turtle", "dog", "parrot"]
```

#### .sort()

```python
num_list = [2.78, 4, -19, 10000, 0]
print(num_list)
num_list.sort()
print(num_list) # [-19, 0, 2, 4, 10000]
```

#### .index()

```python
metals = ["copper", "gold", "silver", "iron"]
print(metals.index("copper"))
print(metals.index("platinum")) # not found error
```

```python
numbers = [4, 3, 2, 1, 0, 1, 2, 3, 4]
print(numbers.index(3))
```

```python
bands = ["Queen", "Led Zeppelin", "The Beatles", "MUSE", "Radiohead"]
end = bands.pop()
print(bands)
print(end)
```

### del and list methods exercises

Do all of this in a .py file in Pycharm.

1. Create a variable called arctic_animals and assign it the list
   `["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]`
2. Use del to remove "tiger" from the list assigned to arctic_animals.
3. Use the `.remove()` method to remove the string "elephant" from the list
   assigned to arctic_animals.
4. Use the `.append()` method to add the string "arctic fox" to the list
   arctic_animals.
5. Use .insert() to insert the string "snowy owl" between the strings "polar
   bear" and "walrus" inside of arctic_animals.
6. Use the .sort() method to rearrange the strings in arctic_animals into
   alphabetical order.
7. Use print() to display the list assigned to arctic_animals
8. Use .index() to get the index number of "reindeer" from arctic_animals then
   print it.
9. Use .pop() to get the last item from the list arctic_animals then print it.

### del and list methods exercises solutions

```python
arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
arctic_animals.remove("elephant")
arctic_animals.append("arctic fox")
arctic_animals.insert(2, "snowy owl")
arctic_animals.sort()
print(arctic_animals)
print(arctic_animals.index("reindeer"))
print(arctic_animals.pop())
```

### Lists vs. Strings

Lists = mutable

Strings = immutable

```python
ex_1 = [1, 2, 3]
ex_1[1] = 5
print(ex_1) # [1, 5, 3]
```

```python
ex_2 = "123"
ex_2[1] = 5
print(ex_2) # error
ex_2 = "153"
print(ex_2) # 153
```

#### Creating new strings from old strings

```python
ex_3 = "No, you can't."
ex_4 = "Yes" + ex_3[3:11] + "!"
print(ex_4)
```

```python
ex_5 = 3.14
ex_6 = "coconut"
ex_7 = ex_5
ex_8 = ex_6
print(ex_7) # 3.14
print(ex_8) # coconut
```

```python
ex_9 = [1, 2, 3, 4, 5]
ex_10 = ex_9
ex_10[2] = 4
print(ex_9)  # [1, 2, 4, 4, 5]
print(ex_10) # [1, 2, 4, 4, 5]
# This is because ex_10 and ex_9 are sharing the same computer memory.
# Changing ex_10 will also change ex_9 because they share the same memory location.
```

#### Why does Python have references?

```python
import copy
ex_12 = [1, 2, 3, 4, 5]
ex_13 = copy.deepcopy(ex_12) # copy ex_12 to a different memory location
ex_13[2] = 4
print(ex_12) # [1, 2, 3, 4, 5]
print(ex_13) # [1, 2, 4, 4, 5]
```

```python
import copy
ex_12 = [1, 2, 3, 4, 5]
ex_13 = copy.deepcopy(ex_12) # copy ex_12 to a different memory location
ex_13[2] = 4
ex_14 = ex_13
ex_14[4] = 6
print(ex_12) # [1, 2, 3, 4, 5]
print(ex_13) # [1, 2, 4, 4, 6]
```

#### list line continuation

```python
ex_15 = ["bush",
         "fern",
         "tree",
         "moss"]
print(ex_15) # ["bush", "fern", "tree", "moss"]
```

#### \ line continuation

```python
ex_16 = 2 + \
        4 + \
        1
print(ex_16)
ex_17 = "The Emp\
         ir Strikes\
         Back"
print(ex_17) # The Empire Strikes Back
ex_18 = "hello" + \
        "world"
print(ex_18) # hello world
```

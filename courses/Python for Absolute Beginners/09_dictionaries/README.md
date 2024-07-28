## Section 09: Dictionaries

#### Table of Contents

- introduction to dictionaries
- introduction to dictionaries exercises
- introduction to dictionaries exercises solution
- dictionary methods 1: .keys(), .values(), .items(), and .get()
- dictionary methods 1 exercises
- dictionary methods 1 exercises solution
- dictionary methods 2: .fromkeys(), .pop(), and .popitem()
- dictionary methods 2 exercises
- dictionary methods 2 exercises solution
- dictionary methods 3: .clear(), .copy(), and .update()
- dictionary methods 3 exercises
- dictionary methods 3 exercises solution
- dictionary methods 4: .setdefault()
- dict()

### introduction to dictionaries

A dictionary is a key-value pair data type.

```python
console = {'nintendo': 'wii'}
# key is 'nintendo'
# value of key 'nintendo' is 'wii'
```

#### accessing the keys

```python
consoles = {"nintendo": "wii", "microsoft": "xbox", "sony": "playstation"}
print(consoles["microsoft"])
val = consoles["microsoft"]
print(val)
print("The " + consoles["sony"] + " 4 is Sony's newest gaming console.")
```

#### key-values

```python
mohs_hardness = {9: 'corundum', 10: 'diamond'}
floats = {1.23: 1000, 3.14159: 10000, 2.718: 10000}
mixed = {"string": 1, 10210: 2, 4.976: 3, False: 4}
```

#### dictionaries are unordered

List items are ordered, but dictionary items are not ordered.

```python
print([2, 4, 6] == [2, 4, 6])
print([2, 4, 6] == [6, 4, 2])
```

```python
first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
second = {2: 2.3, 0: 2.1, 3: 2.4, 1: 2.2}
print(first == second)
```

#### keyError

```python
first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
print(first[4]) # KeyError: 4
```

#### in key

```python
first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
print(1 in first)
print(4 not in first)
```

### introduction to dictionaries exercises

Do all of this in a .py file in Pycharm.

- create a variable and assign it a dictionary that has 5 key value pairs
- print and access the value held at the third key in the dictionary
- use the in keyword to check if a key appears in the dictionary and print the
  result
- use not in to check if a key does not appear in the dictionary and print the
  result

### introduction to dictionaries exercises solution

```python
# example solution
dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(dictionary["c"])
print("a" in dictionary)
print("b" not in dictionary)
```

### dictionary methods 1: .keys(), .values(), .items(), and .get()

### dictionary methods 1 exercises

### dictionary methods 1 exercises solution

### dictionary methods 2: .fromkeys(), .pop(), and .popitem()

### dictionary methods 2 exercises

### dictionary methods 2 exercises solution

### dictionary methods 3: .clear(), .copy(), and .update()

### dictionary methods 3 exercises

### dictionary methods 3 exercises solution

### dictionary methods 4: .setdefault()

### dict()

```

```

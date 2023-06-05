## Section 09: Dictionary Coding Exercises

#### Table of Contents
- Coding Exercise 01: Count Word Frequency
- Coding Exercise 02: Common Keys
- Coding Exercise 03: Key with the Highest Value
- Coding Exercise 04: Reverse Key-Value Pairs
- Coding Exercise 05: Conditional Filter
- Coding Exercise 06: Same Frequency

### Coding Exercise 01: Count Word Frequency

Define a function to count the frequency of words in a given list of words.

**Example**:
```python
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 

# Output
{'apple': 3, 'orange': 2, 'banana': 1}
```



### Coding Exercise 02: Common Keys

Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

**Example**:
```python
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)
# Output:

{'a': 1, 'b': 5, 'c': 7, 'd': 5}
```



### Coding Exercise 03: Key with the Highest Value

Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

**Example**:
```python
my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict)
# Output:
b
```


### Coding Exercise 04: Reverse Key-Value Pairs

Define a function which takes as a parameter dictionary and returns a dictionary in which everse the 
key-value pairs are reversed.

**Example**:
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict(my_dict)
# Output:

{1: 'a', 2: 'b', 3: 'c'}
```


### Coding Exercise 05: Conditional Filter

Define a function that takes a dictionary as a parameter and returns a dictionary with elements based
on a condition.

**Example**:
```python
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0) 
# Output:
{'b': 2, 'd': 4}
```

### Coding Exercise 06: Same Frequency

Define a function which takes two lists as parameters and check if two given lists have the same
frequency of elements.

**Example**:
```python
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)
# Output:
False
```

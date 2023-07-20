## Section 08: Dictionaries

#### Table of Contents
- What is a Dictionary?
- Create a Dictionary
- Dictionaries in memory
- Insert /Update an element in a Dictionary
- Traverse through a Dictionary
- Search for an element in a Dictionary
- Delete/ Remove an element from a Dictionary
- Dictionary Methods
- Dictionary Operations / Builtin Functions
- Dictionary vs List
- Time and Space Complexity of a Dictionary
- Dictionary Comprehension
- Quiz 3: Dictionary Quiz


### What is a Dictionary?

A dictionary is a collection object which is unordered, changeable and indexed.

**Lewis**: a person who owns or works in a corn mill.

```
myDict = {
    "Lewis": "a person who owns or works in a corn mill",
    "Programmer": "a person who writes computer programs"
}
myArray = ["Lewis", "Programmer", "App"]
```
myArray[0] = "Lewis"
myDict["Lewis"] = "a person who owns or works in a corn mill"


**Key-Value Pair**



### Dictionaries in memory

A **hash table** is a way of doing **key-value lookups**. You store the values in an array, and then
use a **hash function** to find the index of the array cell that corresponds to your key-value pair.


![N Queens Problem](https://github.com/lcycstudio/python/tree/master/data_structures/08_dictionary/hash_function.png)




### Dictionary vs List

| **Dictionary**                  | **List**                   |
|---------------------------------|----------------------------|
| Unordered                       | Ordered                    |
| Access via keys                 | Access via index           |
| Collection of key pair values   | Collection of elements     |
| Preferred for unique key values | Preferred for ordered data |
| No duplicate members            | Allow duplicate members    |



### Time and Space Complexity of a Dictionary

| **Operation*                      | **Time Complexity** | **Space Complexity** |
|-----------------------------------|---------------------|----------------------|
| Creating a Dictionary             | O(len(dict))        | O(n)                 |
| Inserting a value in a Dictionary | O(1) or O(n)        | O(1)                 |
| Traversing a given Dictionary     | O(n)                | O(1)                 |
| Accessing a given value           | O(1)                | O(1)                 |
| Searching a given value           | O(n)                | O(1)                 |
| Deleting a given value            | O(1)                | O(1)                 |



### Dictionary Comprehension

```python
new_dict = {new_key: new_value for item in list}

new_dict = {new_key: new_value for (key, value) in dict.items()}

```


### Quiz 3: Dictionary Quiz





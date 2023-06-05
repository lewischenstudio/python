## Section 04: Python Lists

#### Table of Contents
- What is a List? How to create it?
- Accessing/Traversing a list
- Update/Insert a List
- Slice/Delete from a List
- Searching for an element in a List
- List Operations/Functions
- Lists and strings
- Common List pitfalls and ways to avoid them
- Lists vs Arrays
- Time and Space Complexity of List
- List Comprehension
- Conditional List Comprehension
- Practice Test 1: List Interview Questions


### What is a List? How to create it?

A list is a data structure that holds an ordered collection or items.

[10, 20, 30, 40] -----> Integers

['Edy', 'John', 'Jane'] -----> Strings

['spam', 1, 2.0, 5] -----> String, Integer, Float

['spam', 5, 2.0, [10,20]] -----> String, Integer, Float, Nested List



### Lists vs Arrays

#### Similarities
1. Both data structures are mutable.
2. Both can be indexed and iterated through.
3. They can be both sliced.



### Time and Space Complexity of List

| **Operation**                  | **Time Complexity** | **Space Complexity** |
|--------------------------------|---------------------|----------------------|
| Creating an empty array        | O(1)                | O(1)                 |
| Creating a List with elements  | O(N)                | O(N)                 |
| Inserting a value in an array  | O(N)                | O(1)                 |
| Traversing a given array       | O(N)                | O(1)                 |
| Accessing a given cell in List | O(1)                | O(1)                 |
| Searching a given cell in List | O(N)                | O(1)                 |
| Deleting a given cell in List  | O(N)                | O(1)                 |



### List Comprehension

```python
prev_list = [1,2,3]
new_list = []
for i in prev_list:
  multiply_2 = i * 2
  new_list.append(multiply_2)

list_ = [i * 2 for i in prev_list]
```


### Conditional List Comprehension

```python
new_list = [new_item for item in list if condition]
```

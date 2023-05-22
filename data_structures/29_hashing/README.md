## Section 29: Hashing

#### Table of Contents
- What is Hashing? Why we need it?
- Hashing Terminology
- Hash Functions
- Types of Collision Resolution Techniques
- Hash Table is Full
- Pros and Cons of Resolution Techniques
- Practical Use of Hashing
- Hashing vs Other DS


### What is Hashing? Why we need it?

Hashing is a method of sorting and indexing data. The idea behind hashing is to
allow large amounts of data to be indexed using keys commonly created by formulas.

#### Why Hashing?
It is time efficient in case of SEARCH operation

| Data Structure      | Time Complexity  for SEARCH |
|---------------------|-----------------------------|
| Array / Python List | O(logN)                     |
| Linked List         | O(N)                        |
| Tree                | O(logN)                     |
| Hashing             | O(1) or O(N)                |


### Hashing Terminology

**Hash function**: it is a function that can be used to map data of arbitrary data
to data of fixed size.

**Hash value**: A value that is returned by Hash function.
**Hash Table**: It is a data structure which implements an associative array
abstract data type, a structure that can map keys to values.
**Collision**: A collision occurs when two different keys to a has function produce
the same output.


### Hash Functions

Search time complexity: O(1)

#### Mod function
```python
def mod(number, cellNumber):
  return number % cellNumber
```

#### ASCII function
```python
def modASCII(string, cellNumber):
  total = 0
  for i in string:
    total += ord(i)
  return total % cellNumber
```

Properties of good Hash function
- It is distributed hash values uniformly across hash tables to avoid collision
- It has to use all the input data


### Types of Collision Resolution Techniques

#### Collision Resolution Techniques

```
          Resolution Techniques
        /                 \
      /                     \
Direct Chaining         Open Addressing
                        |-- Linear Probing
                        |-- Quadratic Probing
                        |-- Double Hashing
```

**Direct Chaining**: Implements the buckets as linked list. Colliding elements are stored in this list.
```
      HF
ABCD ---> 2
EFGH ---> 2
IJKL ---> 2
LOVE ---> 7
0| 
1|
2| 111 -> [(ABCD,111), 222] -> [(EFGH,222), 333] -> [(IJKL, 333), Null]
3|
4|
5|
6|
7| 444 -> [(LOVE,444), null]
```

**Open Addressing**: Colliding elements are stored in other vacant buckets. During 
storage and lookup these are found through so called probing.
- **Linear Probing**: It places new key into closet following empty cell
- **Quadratic Probing**: Adding arbitrary quadratic polynomial to the index until
an empty cell is found
-- **Double Hashing**: Interval between probes is computed by another has function



### Hash Table is Full

#### Direct Chaining
This situation will never happen.

#### Open Addressing
Create 2X size of current Hash Table and recall hashing for current keys.


### Pros and Cons of Resolution Techniques

#### Direct Chaining
- Hash table never gets full
- Huge linked list causes perforamce leaks
- Time complexity for search operation becomes O(N)

#### Open Addressing
- Easy implementation
- When Hash Table is full, creation of new Hash Tables affects performance
- Time complexity for search operation becomes O(N)

#### Tips
- If the input size is known, then we always use **Open Addressing**
- If we perform deletion operation very often, then we can choose **Direct Chaining**


### Practical Use of Hashing
- Password verification
- File system: File path is mapped to physical location on disk

### Hashing vs Other DS
- On an average Inserion/Deletion/Search operations take O(1) time.
- When Hash function is not good enough Insertion/Deletion/Search operations take O(N) time

| Operations | Array / Python List | Linked List | Tree    | Hashing      |
|------------|---------------------|-------------|---------|--------------|
| Insertion  | O(N)                | O(N)        | O(logN) | O(1) or O(N) |
| Deletion   | O(N)                | O(N)        | O(logN) | O(1) or O(N) |
| Search     | O(N)                | O(N)        | O(logN) | O(1) or O(N) |
## Section 03: Arrays

#### Table of Contents
- What is an Array?
- Types of Array
- Arrays in Memory
- Create an Array
- Insertion to Array
- Traversal Operation
- Accessing an element of Array
- Searching for an element in Array
- Deleting an element from Array
- Time and Space Complexity of One Dimensional Array
- One Dimensional Array Practice
- Create Two Dimensional Array
- Insertion - Two Dimensional Array
- Accessing an element of Two Dimensional Array
- Traversal - Two Dimensional Array
- Searching for an element in Two Dimensional Array
- Deletion - Two Dimensional Array
- Time and Space Complexity of 2D Array
- When to use/avoid array
- Download the Resources


### What is an Array?

- It is a box of macaroons.
- All macaroons in this box are next to each other
- Each macaroon can be identified uniquely based on their location

- Array can be store data of specified type
- Elements of an array are located in a contiguous
- Each element of an array has a unique index

#### Why do we need arrays?

To store large amount of data instead of using variables.



### Types of Array

- One dimensional
- Multi-dimensional
  - two dimensional
  - three dimensional
  - ...
  - N dimensional

#### One Dimensional Array
It is an array with a bunch of values having been declared with a single index.

`a[i]` --> i between 0 and n

```
[5, 4, 10, 11, 8, 11, 68, 87, 12]
a[0] = 5
a[1] = 4
...
a[5] = 11
```

#### Two Dimensional Array
It is an array with a bunch of values having been declared with double index.

`a[i][j]` --> i and j between 0 and n

#### Three Dimensional Array
It is an array with a bunch of values having been declared with triple index.

`a[i][j][k]` --> i, j and k between 0 and n



### Arrays in Memory

![Arrays in Memory](https://github.com/lcycstudio/python/tree/master/data_structures/03_arrays/array_in_memory.png)



### Time and Space Complexity of One Dimensional Array

| **Operation**                   | **Time Complexity** | **Space Complexity** |
|---------------------------------|---------------------|----------------------|
| Creating an empty array         | O(1)                | O(1)                 |
| Creating an array with elements | O(N)                | O(N)                 |
| Inserting a value in an array   | O(N)                | O(1)                 |
| Traversing a given array        | O(N)                | O(1)                 |
| Accessing a given cell          | O(1)                | O(1)                 |
| Searching a given cell          | O(N)                | O(1)                 |
| Deleting a given cell           | O(N)                | O(1)                 |



### Time and Space Complexity of 2D Array

| **Operation**                        | **Time Complexity**  | **Space Complexity** |
|--------------------------------------|:--------------------:|:--------------------:|
| Creating an empty array              | O(1)                 | O(1)                 |
| Creating an array with elements      | O(MN)                | O(MN)                |
| Inserting a column/row in an array   | O(MN)                | O(MN)                |
| Traversing a given array             | O(MN)                | O(1)                 |
| Accessing a given cell               | O(1)                 | O(1)                 |
| Searching a given cell               | O(MN)                | O(1)                 |
| Deleting a given cell                | O(MN)                | O(1)                 |



### When to use/avoid array

#### When to use
- To store multiple variables of same data type
- Random access

#### When to avoid
- Same data type elements
- Reserve memory



### Download the Resources





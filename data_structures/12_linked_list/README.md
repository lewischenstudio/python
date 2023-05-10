## Section 12: Linked List

#### Table of Contents
- What is a Linked List?
- Linked List vs Arrays
- Types of Linked List
- Linked List in the Memory
- Creation of Singly Linked List
- Insertion in Singly Linked List in Memory
- Insertion in Singly Linked List Algorithm
- Insertion Method in Singly Linked List
- Traversal of Singly Linked List
- Search for a value in Singly Linked List
- Deletion of node from Singly Linked List
- Deletion of entire Singly Linked List
- Time and Space Complexity of Singly Linked List


### What is a Linked List?
A **linked list** is a form of a sequential collection, and it does not have to be in order.
A linked list is made up of independent nodes that may contain any type of data, and each 
node has a reference to the next node in the link.

A linked list is consisted of a **head**, a **tail**, and **nodes**.

Nodes: data and references.


### Linked List vs Arrays

Linked List = [Head, 1] --> [1, 111] --> [2, 222] --> [4, 333] ---> [5, null] <-- [Tail, 333]

Array = [0, 1, 2, 3, 4, 5]

- Elements of a linked list are independent objects.
- Variable size - the size of a linked list is not predefined.
- Insertion and removals in a linked list are very efficient.


### Types of Linked Lists
- Singly Linked List
- Circular Singly Linked List
- Doubly Linked List
- Circular Doubly Linked List


#### Singly Linked List
[Head, 001] \
[(001, 1), 111] --> [(111, 2), 222] --> [(222, 4), 333] --> [(333, 5), null] \
[Tail, 333]

#### Circular Singly Linked List
[Head, 001] \
[(001, 1), 111] --> [(111, 2), 222] --> [(222, 4), 333] --> [(333, 5), null] --> [(001, 1), 111] \
[Tail, 333]

#### Doubly Singly Linked List
[Head, 001] \
[null, (001, S1), 111] --> [001, (111, S2), 222] --> [111, (222, S3), 333] --> [222, (333, S4), null] \
[Tail, 333]

#### Circular Doubly Linked List
[Head, 001] \
[333, (001, S1), 111] --> [001, (111, S2), 222] --> [111, (222, S3), 333] --> [222, (333, S4), 111] --> [333, (S1,001), 111] \
[Tail, 333]


### Linked List in the Memory
Each node in a linked list is stored randomly in memory. We cannot access a node just by 
referecing to the memory or indexing.


### Creation of a Singly Linked List
- Create Head and Tail, initialize with null
- Create a blank Node and assign a value to it and reference to null
- Link Head and Tail with these Node


### Time and Space Complexity of Singly Linked List
|                         | Time Complexity  | Space Complexity |
|-------------------------|------------------|------------------|
| Creation                | O(1)             | O(1)             |
| Insertion               | O(n)             | O(1)             |
| Searching               | O(n)             | O(1)             |
| Traversing              | O(n)             | O(1)             |
| Deletion of a node      | O(n)             | O(1)             |
| Deletion of linked list | O(1)             | O(1)             |
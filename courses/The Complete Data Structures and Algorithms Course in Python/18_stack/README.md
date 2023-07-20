## Section 18: Stack

#### Table of Contents
- What is a Stack?
- Stack Operations
- Create Stack using List without size limit
- Operations on Stack using List (push, pop, peek, isEmpty, Delete)
- Create Stack with limit (pop, push, peek, isFull, isEmpty, delete)
- Create Stack using Linked List
- Operation on Stack using Linked List (pop, push, peek, isEmpty, delete)
- Time and Space Complexity of Stack using Linked List
- When to use/avoid Stack

### What is a Stack?

Stack is a data structure that stores items in a Last-In/First-Out (LIFO) manner, like stacking plates.

LIFO method - one way open

What we need Queue Data Structure?
- Browser stack
- Container stack


### Stack Operations
- Create stack
- Push
- Pop
- Peek
- isEmpty
- isFull
- deleteStack


### Create Stack using List without size limit

Stack using List
- Easy to implement
- Speed problem when it grows


### Create Stack using Linked List

Stack using Linked List
- Fast performance
- Implementation is not easy

### When to use/avoid Stack

Use:
- LIFO (Last-In-First-Out) functionality
- The chance of data corruption is minimum

Avoid:
- Random access is not possible


### Time and Space Complexity of Stack
|                         | Time Complexity  | Space Complexity |
|-------------------------|------------------|------------------|
| Create Stack            | O(1)             | O(1)             |
| Push                    | O(1)             | O(1)             |
| Pop                     | O(1)             | O(1)             |
| Peek                    | O(1)             | O(1)             |
| isEmpty                 | O(1)             | O(1)             |
| Delete Entire Stack     | O(1)             | O(1)             |
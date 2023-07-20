## Section 13: Linked List

#### Table of Contents
- What is a Linked List?
- Linked List vs Lists/Arrays
- Types of Linked List
- Linked List in the Memory
- Creation of Singly Linked List
- Insertion in Singly Linked List in Memory
- __iter__ method
- Insertion in Singly Linked List Algorithm
- Insertion Method in Singly Linked List
- Traversal of Singly Linked List
- Search for a value in Single Linked List
- Deletion of node from Singly Linked List
- Deletion Method in Singly Linked List
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


### __iter__ method

```python
def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
```
Here is a breakdown of the code line-by-line:

- `def __iter__(self):`
  
  This is the declaration of the `__iter__` special method in Python. It allows an 
  object to be iterable, which means it can be used in a loop (like a for loop). When
  a class has an `__iter__` method, Python will use it in contexts where it needs to
  iterate over the object.
- `node = self.head`
  
  This line initializes the node variable to point to the head of the linked list.
  It sets the starting point for the iteration.
- `while node:`
  
  This is the start of a while loop that continues as long as node is not None. This
  loop will allow you to traverse the linked list, moving from one node to the next.
- `yield node`
  
  This yield keyword is used here to create a generator. Generators are a type of
  iterable, like lists or tuples. However, unlike lists, they do not store all their
  values in memory at once – they generate them on the fly. So, whenever the Python
  interpreter needs the next value while iterating, it comes back to this yield
  statement, and the next value is "yielded" or produced.
- `node = node.next`

  This line moves the node pointer to the next node in the list. This is how we 
  traverse to the next element for each iteration of the while loop.

#### Why do we need __iter__?

Without an `__iter__` method, you wouldn't be able to iterate over instances of the class
using a for loop or other iteration mechanism. By defining `__iter__`, you're telling Python
that your object is iterable, and how exactly to iterate over it. For a linked list, this
typically means starting at the head of the list and following the 'next' pointers to each
subsequent node, until reaching the end of the list. This is exactly what the given `__iter__`
method implementation does.

Here is an example usage of this `__iter__` method:

```python
linked_list = LinkedList() 
linked_list.append(1) 
linked_list.append(2) 
linked_list.append(3) 
for node in linked_list: 
    print(node.value)
```

In this example, the for loop will print the values of the nodes in the linked list in
order. This is possible because the LinkedList class has an `__iter__` method.

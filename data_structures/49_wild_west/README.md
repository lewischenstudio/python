## Section 49: The Wild West

#### Table of Contents
- Coding Exercise 01: Singly Linked List - Push
- Coding Exercise 02: Singly Linked List - Pop
- Coding Exercise 03: Singly Linked List - Get
- Coding Exercise 04: Singly Linked List - Insert
- Coding Exercise 05: Singly Linked List - Rotate
- Coding Exercise 06: Singly Linked List - Set
- Coding Exercise 07: Divide and Conquer - countZeroes
- Coding Exercise 08: Divide and Conquer - sortedFrequency
- Coding Exercise 09: Divide and Conquer - findRotatedIndex
- Coding Exercise 10: Singly Linked List - Remove
- Coding Exercise 21: Insertion Sort
- Coding Exercise 12: Bubble Sort
- Coding Exercise 13: Sorting with Pivot : Quicksort
- Coding Exercise 14: Stack - Push
- Coding Exercise 15: Stack - Pop
- Coding Exercise 16: Stack with Two Queues
- Coding Exercise 17: Queue - Enqueue
- Coding Exercise 18: Binary Search Tree - Insert
- Coding Exercise 19: Binary Search Tree - Find
- Coding Exercise 20: Binary Search Tree - DFSPreOrder
- Coding Exercise 21: Binary Search Tree - DFSInOrder
- Coding Exercise 22: Binary Search Tree - DFSPostOrder
- Coding Exercise 23: Binary Search Tree - Remove
- Coding Exercise 24: Binary Search Tree - Check If Balanced
- Coding Exercise 25: Max Binary Heap - Insert
- Coding Exercise 26: Min Binary Heap - Insert
- Coding Exercise 27: Max Binary Heap - Extract Max
- Coding Exercise 28: Graph - Add Vertex


### Coding Exercise 01: Singly Linked List - Push
Implement the following on the SinglyLinkedList class:

`push`

This function should take in a value and add o node to the end of the SinglyLinkedList. It should return the SinglyLinkedList.

**Examples**
```python
singlyLinkedList = SinglyLinkedList()
singlyLinkedList.push(5)  # Success
singlyLinkedList.length   # 1
singlyLinkedList.head.val # 5
singlyLinkedList.tail.val # 5
 
singlyLinkedList.push(10)    # Success
singlyLinkedList.length      # 2
singlyLinkedList.head.val    # 5
singlyLinkedList.head.next.val  # 10
singlyLinkedList.tail.val    # 10
```
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

### Coding Exercise 02: Singly Linked List - Pop

Implement the following on the SinglyLinkedList class:

**pop**

This function should remove a node at the end of the SinglyLinkedList. It should return the
node removed.

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
 
singlyLinkedList.pop().val # 10
singlyLinkedList.tail.val  # 5
singlyLinkedList.length    # 1
singlyLinkedList.pop().val # 5
singlyLinkedList.length    # 0
singlyLinkedList.pop()     # Undefined
```



### Coding Exercise 03: Singly Linked List - Get

Implement the following on the SinglyLinkedList class:

**get**

This function should find a node at a specified index in a  SinglyLinkedList. It should return
the found node.

**Examples**

```python
singlyLinkedList = SinglyLinkedList()
singlyLinkedList.push(5)  # Success
singlyLinkedList.push(10)  # Success
singlyLinkedList.push(15)  # Success
singlyLinkedList.push(20)  # Success
 
singlyLinkedList.get(0).val    # 5
singlyLinkedList.get(1).val    # 10
singlyLinkedList.get(2).val    # 15
singlyLinkedList.get(3).val    # 20
singlyLinkedList.get(4).val    # None
```



### Coding Exercise 04: Singly Linked List - Insert

Implement the following on the SinglyLinkedList class:

**Insert**

This function should insert a node at a specified index in a  SinglyLinkedList. It should
return true if the index is valid, and false if the index is invalid (less than 0 or greater
the length of the list).

**Examples**

(Note: you do not need to re-implement push, the test will be provided with it)

```python
singlyLinkedList = SinglyLinkedList()
singlyLinkedList.push(5)  # Success
singlyLinkedList.push(10)  # Success
singlyLinkedList.push(15)  # Success
singlyLinkedList.push(20)  # Success

singlyLinkedList.insert(2, 12)  # True
singlyLinkedList.insert(100, 12) # False
singlyLinkedList.length         # 5
singlyLinkedList.head.val       # 5
singlyLinkedList.head.next.val   # 10
singlyLinkedList.head.next.next.val  # 12
singlyLinkedList.head.next.next.next.val # 15
singlyLinkedList.head.next.next.next.next.val # 20
 
singlyLinkedList.insert(5, 25) # True
singlyLinkedList.head.next.next.next.next.next.val # 25
singlyLinkedList.tail.val # 25
```



### Coding Exercise 05: Singly Linked List - Rotate

Implement the following on the SinglyLinkedList class:

**Rotate**

This function should rotate all the nodes in the list by some number passed in. For instance,
if your list looks like 1 -> 2 -> 3 -> 4 -> 5 and you rotate by 2, the list should be modified
to 3 -> 4 -> 5 -> 1 -> 2. The number passed in  to rotate can be any integer.

Time Complexity : O(N), where N is the length of the list.

Space Complexity : O(1)

**Examples**

(Note: you do not need to re-implement push, the test will be provided with it)

```python
singlyLinkedList = SinglyLinkedList()
singlyLinkedList.push(5)  # Success
singlyLinkedList.push(10)  # Success
singlyLinkedList.push(15)  # Success
singlyLinkedList.push(20)  # Success
singlyLinkedList.push(25)  # Success
 
singlyLinkedList.rotate(3)
 
singlyLinkedList.head.val  # 20
singlyLinkedList.head.next.val   # 25
singlyLinkedList.head.next.next.val  # 5
singlyLinkedList.head.next.next.next.val # 10
singlyLinkedList.head.next.next.next.next.val # 15
singlyLinkedList.tail.val # 15
singlyLinkedList.tail.next # None
 
singlyLinkedList = SinglyLinkedList()
singlyLinkedList.push(5)  # Success
singlyLinkedList.push(10)  # Success
singlyLinkedList.push(15)  # Success
singlyLinkedList.push(20)  # Success
singlyLinkedList.push(25)  # Success
 
singlyLinkedList.rotate(-1)
 
singlyLinkedList.head.val  # 25
singlyLinkedList.head.next.val   # 5
singlyLinkedList.head.next.next.val  # 10
singlyLinkedList.head.next.next.next.val # 15
singlyLinkedList.head.next.next.next.next.val # 20
singlyLinkedList.tail.val # 20
singlyLinkedList.tail.next # None
```


### Coding Exercise 06: Singly Linked List - Set

Implement the following on the SinglyLinkedList class:

**Set**

This function should accept an index and a value and update the value of the node in the
SinglyLinkedList at the index with new value. It should return true if the node is updated
successfully or false if an invalid index is passed in.

**Examples**

(Note: you do not need to re-implement push, the test will be provided with it)

```python
singlyLinkedList = SinglyLinkedList()
singlyLinkedList.push(1)
singlyLinkedList.push(2)
 
singlyLinkedList.set(0,10)  # True
singlyLinkedList.set(1,20)  # True
singlyLinkedList.length    # 2
singlyLinkedList.head.val  # 10
 
singlyLinkedList.set(10,10) # False
singlyLinkedList.set(2,100) # False
 
singlyLinkedList.head.next.val # 20
```



### Coding Exercise 07: Singly Linked List - Remove

Implement a function on the SinglyLinkedList class which should remove a node at a specified
index in a SinglyLinkedList. If the index is valid it should return the removed node otherwise
it should return undefined.

**Example**

```python
singlyLinkedList = SinglyLinkedList()
singlyLinkedList.push(5)  # Success
singlyLinkedList.push(10)  # Success
singlyLinkedList.push(15)  # Success
singlyLinkedList.push(20)  # Success
singlyLinkedList.push(25)  # Success
singlyLinkedList.remove(2).val # 15
singlyLinkedList.remove(100) # None
singlyLinkedList.length  # 4
singlyLinkedList.head.val   # 5
singlyLinkedList.head.next.val  # 10
singlyLinkedList.head.next.next.val  # 20
```


### Coding Exercise 08: Divide and Conquer - countZeroes

Divide and Conquer - countZeroes
Given an array of 1s and 0s which has all 1s first followed by all 0s, write a function called
countZeroes, which returns the number of zeroes in the array.
```python
countZeroes([1,1,1,1,0,0]) # 2
countZeroes([1,0,0,0,0]) # 4
countZeroes([0,0,0]) # 3
countZeroes([1,1,1,1]) # 0
```
Time Complexity - O(log n)



### Coding Exercise 09: Divide and Conquer - sortedFrequency

Given a sorted array and a number, write a function called sortedFrequency that counts the
occurrences of the number in the array.

```python
sortedFrequency([1, 1, 2, 2, 2, 2, 3], 2) # 4
sortedFrequency([1, 1, 2, 2, 2, 2, 3], 3) # 1
sortedFrequency([1, 1, 2, 2, 2, 2, 3], 4) # -1
sortedFrequency([], 4) # -1
```

Time Complexity - O(log n)



### Coding Exercise 10: Divide and Conquer - findRotatedIndex

Write a function called findRotatedIndex which accepts a rotated array of sorted numbers and
an integer. The function should return the index of the integer in the array. If the value is
not found, return -1.

Constraints:

Time Complexity - O(log n)

Space Complexity - O(1)

```python
findRotatedIndex([3, 4, 1, 2], 4) # 1
findRotatedIndex([4, 6, 7, 8, 9, 1, 2, 3, 4], 8) # 3
findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 3) # 6
findRotatedIndex([37, 44, 66, 102, 10, 22], 14) # -1
findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 12) # -1
findRotatedIndex([11, 12, 13, 14, 15, 16, 3, 5, 7, 9], 16) # 5
findRotatedIndex([11, 12, 13, 17, 39], 17) # 3
findRotatedIndex([11], 11) # 0
findRotatedIndex([], 11) # -1
findRotatedIndex([4, 4, 4, 4, 4], 5) # -1
```



### Coding Exercise 11: Insertion Sort

Implement insertionSort. Given an array, insertionSort will sort the values in the array. 
The function take 2 parameters: an array and an optional comparator function. The comparator
function is a callback that will take two values from the array to be compared. The function
returns a negative value if the first value is less than the second, a positive value if the
first value is greater than the second, and 0 if both values are equal. The default comparator
you provide should assume that the two parameters are numbers and that we are sorting the
values from smallest to largest.

**Insertion Sort**

Guidance for how insertion sort should work:
- Start by picking the second element in the array ( we will assume the first element is the
start of the "sorted" portion)
- Now compare the second element with the one before it and swap if necessary
- Continue to the next element and if it is in the incorrect order, iterate through the sorted
portion to place the element in the correct place
- Repeat until the array is sorted.
- Your function should accept an array and return an array of sorted values

**Example**

```python
nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32]
insertionSortSwap(nums)
Output:
[2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]
 
 
kit = ['LilBub', 'Garfield', 'Blue', 'Grumpy']
def strComp(a,b):
    if a < b:
        return -1
    if a > b:
        return 1
    return 0
# insertionSortSwap(kit, strComp)
# Output: ['Blue', 'Garfield', 'Grumpy', 'LilBub']
 
class Kitty:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name +" "+str(self.age)
moarKittyData = [
    Kitty('LilBub',7),
    Kitty('Garfield',40),
    Kitty('Heathcliff',45),
    Kitty('Blue',1),
    Kitty('Grumpy',6),
]
def oldestToYoungest(a,b):
    return b.age - a.age

test = insertionSortSwap(moarKittyData, oldestToYoungest)
for i in test:
    print(i)
 
# Output:
# Heathcliff 45
# Garfield 40
# LilBub 7
# Grumpy 6
# Blue 1
```


### Coding Exercise 12: Bubble Sort

Implement bubbleSort. Given an array, bubbleSort will sort the values in the array. The function
take 2 parameters: an array and an optional comparator function.

def insertionSortSwap(arr, comparator=None):
    if callable(comparator)==False:
        # provide a default
    return arr
The comparator function is a callback that will take two values from the array to be compared.
The function returns a negative value if the first value is less than the second, a positive
value if the first value is greater than the second, and 0 if both values are equal.

The default comparator you provide should assume that the two parameters are numbers and that
we are sorting the values from smallest to largest.

**Example**

```python
bubbleSort([4,20,12,10,7,8]) # [4, 7, 8, 10, 12, 20]
bubbleSort([0, -9, 7, 3]) # [-9, 0, 3, 7]
bubbleSort([1,2,3])  # [1, 2, 3]
bubbleSort([])  #[]

nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32]
bubbleSort(nums) 
# Output:
# [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]

 
kit = ['LilBub', 'Garfield', 'Blue', 'Grumpy']
def strComp(a,b):
    if a < b:
        return -1
    if a > b:
        return 1
    return 0
bubbleSort(kit, strComp)
 
# ['Blue', 'Garfield', 'Grumpy', 'LilBub']
 
class Kitty:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name +" "+str(self.age)
moarKittyData = [
    Kitty('LilBub',7),
    Kitty('Garfield',40),
    Kitty('Heathcliff',45),
    Kitty('Blue',1),
    Kitty('Grumpy',6),
]

def oldestToYoungest(a,b):
    return b.age - a.age

test = bubbleSort(moarKittyData, oldestToYoungest)
for i in test:
    print(i)

# Output:
# Heathcliff 45
# Garfield 40
# LilBub 7
# Grumpy 6
# Blue 1
```



### Coding Exercise 13: Sorting with Pivot : Quicksort

In this exercise, your goal is to implement a function called pivot. This function contains nearly
all of the logic you'll need in order to implement Quick Sort.

The pivot function is responsible for taking an array, setting the pivot value, and mutating the
array so that all values less than the pivot wind up to the left of it, and all values greater than
the pivot wind up to the right of it.It's also helpful if this helper returns the index of where
the pivot value winds up.

**Examples**

```python
arr1 = [5,4,9,10,2,20,8,7,3]
arr2 = [8,4,2,5,0,10,11,12,13,16]
arr3 = ['LilBub', 'Garfield', 'Blue', 'Grumpy']
 
def strLength(a,b):
    return len(a)-len(b)
 
pivot(arr1) # 3
pivot(arr2) # 4
pivot(arr3, strLength) # 1
quickSort(arr2, end=len(arr2)-1) # [0, 2, 4, 5, 8, 10, 11, 12, 13, 16]

# Hint: When we get to Quick Sort function, it will be helpful for the pivot helper to accept not
# only an array and an optional comparator, but also an optional start and end index. These should
# default to 0 and the array length minus 1, respectively.
```



### Coding Exercise 14: Stack - Push

Implement the following method on the Stack class:

**push** - takes in a node and puts it at the top of the stack.  Should return the new size of the stack.

**Examples**

```python
stack = Stack()
stack.push(10) #1
stack.first.data #10
stack.last.data #10
stack.push(100) #2
stack.first.data #100
stack.last.data #10
stack.push(1000) #3
stack.first.data #1000
stack.last.data #10
```


### Coding Exercise 15: Stack - Pop

Implement the following methods on the Stack class:

pop - removes the node at the top of the stack and returns the value of that node.

**Examples**

```python
stack = Stack()
stack.push(10)
stack.push(100)
stack.push(1000)
removed = stack.pop()
print(removed) #1000
print(stack.size) #2
stack.pop()
stack.pop()
print(stack.size) #0
```


### Coding Exercise 16: Stack with Two Queues


Implement a stack using two queues:
- push (returns the stack)
- pop (returns the value popped)

**Examples**

```python

stack = Stack()
 
stack.push(10).push(20).push(30)
stack.pop() # 30
stack.pop() # 20
stack.pop() # 10
stack.pop() # None
stack.push(30).push(40).push(50)
stack.pop() # 50
stack.push(60)
stack.pop() # 60
```


### Coding Exercise 17: Queue - Enqueue

Implement the following methods on the Queue class.

enqueue

This function adds the value to the end of the queue.  This should be an O(1) operation and
return the new size of the queue.

**Examples**

```python
queue = Queue()
queue.enqueue(10) # 1
queue.size # 1
queue.enqueue(100) # 2
queue.size # 2
queue.enqueue(1000) # 3
queue.size # 3
```



### Coding Exercise 18: Binary Search Tree - Insert

Write a function on the BinarySearchTree class.

insert - accepts a value and inserts it into the BST in the correct position. The function
should return the binary search tree.

**Examples**

```python
bsTree = BST() 
bsTree.insert(15)
bsTree.insert(20)
bsTree.insert(10)
bsTree.insert(12)
bsTree.root.data # 15
bsTree.root.right.data # 20
bsTree.root.left.right.data # 12
```



### Coding Exercise 19: Binary Search Tree - Find

Write a function on the BinarySearchTree class

**find**

This function should find a node in a binary tree. It should return the node if found, otherwise
return None.

Note : As insert function use from previous example.

**Examples**

```python
bsTree = BST() 
bsTree.insert(15)
bsTree.insert(20)
bsTree.insert(10)
bsTree.insert(12)
 
bsTree.find(20).data # 20
bsTree.find(20).right # None
bsTree.find(20).left # None
bsTree.find(100) # None
```



### Coding Exercise 20: Binary Search Tree - DFSPreOrder

Implement the following functions on the Binary Search Tree class. insert has been implemented
for you to help with testing.

**DFSPreOrder**

This function should search through each node in the binary search tree using pre-order depth 
first search and return an array containing each node's value.

**Examples**

```python
bsTree = BST() 
bsTree.insert(15)
bsTree.insert(20)
bsTree.insert(10)
bsTree.insert(12)
bsTree.depthFirstSearchPreOrder() # [15, 10, 12, 20]
```



### Coding Exercise 21: Binary Search Tree - DFSInOrder

Implement the following functions on the Binary Search Tree class. insert has been implemented
for you to help with testing.

**DFSInOrder**

This function should search through each node in the binary search tree using in-order depth
first search and return an array containing each node's value.

**Examples**

```python
bsTree = BST() 
bsTree.insert(15)
bsTree.insert(20)
bsTree.insert(10)
bsTree.insert(12)
bsTree.depthFirstSearchInOrder() # [10, 12, 15, 20]
```



### Coding Exercise 22: Binary Search Tree - DFSPostOrder

Implement the following functions on the Binary Search Tree class. insert has been implemented
for you to help with testing.

**DFSPostOrder**

This function should search through each node in the binary search tree using post-order depth
first search and return an array containing each node's value.

**Examples**

```python
bsTree = BST() 
bsTree.insert(15)
bsTree.insert(20)
bsTree.insert(10)
bsTree.insert(12)
bsTree.depthFirstSearchPostOrder() # [12, 10, 20, 15]
```



### Coding Exercise 23: Binary Search Tree - Remove

Implement the following function for the following Binary Search Tree . insert is implemented
to help with testing.

remove

This function should remove a node from a binary search tree. Your remove function should be able
to handle removal of the root node, removal of a node with one child and removal of a node with two
children. The function should return the node removed.

**Examples**

```python
bsTree = BST()
insertNode(bsTree.root, 15)
insertNode(bsTree.root, 20)
insertNode(bsTree.root, 10)
insertNode(bsTree.root, 12)
removeNode(bsTree.root, 12)
bsTree.root.rightChild.data #20
bsTree.root.leftChild.data #10
bsTree.root.leftChild.rightChild #None
```



### Coding Exercise 24: Binary Search Tree - Check If Balanced

Write a function isBalanced that should return true if the BST is balanced, otherwise false.

A balanced tree is defined as a tree where the depth of all leaf nodes or nodes with single
children differ by no more than one.

**Examples**

```python
bsTree = BST()
insertNode(bsTree.root, 15)
insertNode(bsTree.root, 20)
insertNode(bsTree.root, 10)
insertNode(bsTree.root, 12)
isBalanced(bsTree.root) #True
```



### Coding Exercise 25: Max Binary Heap - Insert

Implement the following functions on the MaxBinaryHeap class.

insert

This function should insert a node in a binary heap. Make sure to re-order the heap after
insertion if necessary.

**Examples**

```python
newHeap = MaxHeap(5)
insertNode(newHeap,4)
insertNode(newHeap,5)
insertNode(newHeap,2)
insertNode(newHeap,1)
insertNode(newHeap,6)
insertNode(newHeap,10) # The Binary Heap is full
newHeap.customList   # [None, 6, 5, 2, 1, 4]
```



### Coding Exercise 26: Min Binary Heap - Insert

Implement the following functions on the MinBinaryHeap class.

insert

This function should insert a node in a binary heap. Make sure to re-order the heap after
insertion if necessary.

**Examples**

```python
newHeap = MinHeap(5)
insertNode(newHeap,4)
insertNode(newHeap,5)
insertNode(newHeap,2)
insertNode(newHeap,1)
insertNode(newHeap,6)
insertNode(newHeap,10) # The Binary Heap is full
newHeap.customList   # [None, 1, 2, 4, 5, 6]
```



### Coding Exercise 27: Max Binary Heap - Extract Max

Implement following function on the Max Binary Heap Class.

extractMax

This function should remove the root node in a binary heap. Make sure to re-order the heap after
removal if necessary.

**Examples**

```python
newHeap = MaxHeap(6)
insertNode(newHeap,1)
insertNode(newHeap,2)
insertNode(newHeap,3)
insertNode(newHeap,4)
insertNode(newHeap,5)
insertNode(newHeap,6)
extractMax(newHeap)
newHeap.values # [5,4,2,1,3]
```


### Coding Exercise 28: Graph - Add Vertex

Implement the following methods on the Graph class.

addVertex

This function should add a node to the graph and place a new key in the adjacency list with the
value of an empty array.

```python
graph = Graph()
graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.adjacencyList["A"] #[]
graph.adjacencyList["B"] #[]
graph.adjacencyList["C"] #[]
```
## Section 26: Binary Heap

#### Table of Contents
- What is Binary Heap? Why do we need it?
- Common operations (Creation, Peek, sizeofheap) on Binary Heap
- Insert a node in Binary Heap
- Extract a node from Binary Heap
- Delete entire Binary Heap
- Time and space complexity of Binary Heap

### What is Binary Heap? Why do we need it?
A Binary Heap is a Binary Tree with the following properties.
- A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at root must be minimum along all keys in Binary Heap. The same property must be recursively true for all nodes in Binary Tree.
- It's a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This property of Bineary Heap makes them suitable to be stored in an array.

#### Binary Heap Tree
```
                   5
                 /   \  
               /       \  
             /           \  
           /               \  
         10                 20
        /  \               /  \ 
      /      \           /      \ 
    30        40       50        60
   /  \       
 70    80
```


#### Why do we need it?
Find the minimum or maximum number among a set of numbers in logN time. We also want to make
sure that inserting additional numbers does not take more than **O(logN)** time

<u>Possible Solutions</u>
- Store the numbers in sorted Array
  - `[10, 20, 30, 40, 50]`
  - Find minimum: O(1)
  - Insertion O(n)
- Store the numbers in Linked List in stored manner
  - `[Head, 111] --> [(1,111), 222] --> [(2,222), 333] --> [(3,333), null] `
  - `[Tail, null]`

<u>Practical Use</u>
- Prim's Algorithm
- Heap Sort
- Priority Queue

#### Types of Binary Heap
**Minimum heap** - the value of each node is less than or equal to the value of both its children.

**Maximum heap** - it is exactly the opposite of min heap. The value of each node is more than or
equal to the value of both of its children.

Minimum Heap
```
                   5
                 /   \  
               /       \  
             /           \  
           /               \  
         10                 20
        /  \               /  \ 
      /      \           /      \ 
    30        40       50        60
   /  \       
 70    80
```

Minimum Heap
```
                   80
                 /   \  
               /       \  
             /           \  
           /               \  
         70                 60
        /  \               /  \ 
      /      \           /      \ 
    50        40       30        20
   /  \       
  5    10
```

### Common operations (Creation, Peek, sizeofheap) on Binary Heap

- Creation of Binary Heap
- Peek top of Binary Heap
- Extract Min / Extract Max
- Traversal of Binary Heap
- Size of Binary Heap
- Insertion of Binary Heap
- Deletion of the entire Binary Heap

<u>Implementation Options</u>
- Array implementation
- Reference / pointer implementation

#### Array implementation
```
                   5
                 /   \  
               /       \  
             /           \  
           /               \  
         10                 20
        /  \               /  \ 
      /      \           /      \ 
    30        40       50        60
```
```
  0   1    2   3    4    5    6    7    8 
[ x | 5 | 10 | 20 | 30 | 40 | 50 | 60 |   ]
```
Left child = cell[2x]

Right child = cell[2x + 1]

#### Creation of Binary Heap
- Initialize fixed size List
- Set size of Binary Heap to 0
```
  0   1   2   3   4   5   6   7   8
[   |   |   |   |   |   |   |   |   ]
```


### Time and space complexity of Binary Heap
|                           | Time Complexity  | Space Complexity |
|---------------------------|------------------|------------------|
| Create Binary Heap        | O(1)             | O(n)             |
| Peak of Binary Heap       | O(1)             | O(1)             |
| Size of Binary Heap       | O(1)             | O(1)             |
| Traversal of Binary Heap  | O(n)             | O(1)             |
| Insertion of Binary Heap  | O(logN)          | O(logN)          |
| Extraction of Binary Heap | O(logN)          | O(logN)          |
| Deletion of Binary Heap   | O(1)             | O(1)             |
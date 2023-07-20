## Section 19: Queue

#### Table of Contents
- What is Queue?
- Queue using Python List - no size limit
- Queue using Python List - no size limit , operations (enqueue, dequeue, peek)
- Circular Queue - Python List
- Circular Queue - Python List, Operations (enqueue, dequeue, peek, delete)
- Queue - Linked List
- Queue - Linked List, Operations (Create, Enqueue)
- Queue - Linked List, Operations (Dequeue(), isEmpty, Peek)
- Time and Space complexity of Queue using Linked List
- List vs Linked List Implementation
- Python Collections Module
- Queue Module
- Multiprocessing module


### What is a Queue?

Queue is a data structure that stores items in a First-In/First-Out manner.

A new addition to this queue happens at the end of the queue.
First person in the queue will be served first.
FIFO method 
- First In First Out
- two ways open
- one way in / one way out

What we need Queue Data Structure?
- Utilize first coming data first, while others wait for their turn.
- FIFO method - First In First Out
- Point sale system of a restaurant
- Printer queue
- Call center phone systems



### Queue Operations
- Create queue
- Enqueue
- Dequeue
- Peek
- isEmpty
- isFull
- deleteQueue

Implementation
1. Python List
   - Queue without capacity
   - Queue with capacity (Circular Queue)
2. Linked List

### Queue - List
#### Time and Space Complexity of Queue
|                         | Time Complexity  | Space Complexity |
|-------------------------|------------------|------------------|
| CreatE Queue            | O(1)             | O(1)             |
| Enqueue                 | O(n)             | O(1)             |
| Dequeu                  | O(n)             | O(1)             |
| Peek                    | O(1)             | O(1)             |
| isEmpty                 | O(1)             | O(1)             |
| Delete Entire Queue     | O(1)             | O(1)             |


### Queue - Linked List
#### Time and Space Complexity of Queue
|                         | Time Complexity  | Space Complexity |
|-------------------------|------------------|------------------|
| CreatE Queue            | O(1)             | O(1)             |
| Enqueue                 | O(1)             | O(1)             |
| Dequeu                  | O(1)             | O(1)             |
| Peek                    | O(1)             | O(1)             |
| isEmpty                 | O(1)             | O(1)             |
| Delete Entire Queue     | O(1)             | O(1)             |


### List vs Linked List Implementation
|                     | List No          | Capacity Limit   | List with       | Capacity         | Linked          | List             |
|---------------------|------------------|------------------|-----------------|------------------|-----------------|------------------|
|                     | Time Complexity  | Space Complexity | Time Complexity | Space Complexity | Time Complexity | Space Complexity |
| Create Queue        | O(1)             | O(1)             | O(1)            | O(n)             | O(1)            | O(1)             |
| Enqueue             | O(n)             | O(1)             | O(1)            | O(1)             | O(1)            | O(1)             |
| Dequeue             | O(n)             | O(1)             | O(1)            | O(1)             | O(1)            | O(1)             |
| Peek                | O(n)             | O(1)             | O(1)            | O(1)             | O(1)            | O(1)             |
| isEmpty             | O(n)             | O(1)             | O(1)            | O(1)             | O(1)            | O(1)             |
| isFull              | -                | -                | O(1)            | O(1)             | -               | -                |
| Delete Entire Queue | O(1)             | O(1)             | O(1)            | O(1)             | O(1)            | O(1)             |


### Python Collections Module
```python
from collections import deque
```

Methods
- dequeue()
- append()
- popleft()
- clear()


### Python Dequeue Module
```python
from queue import q
```
FIFO queue - `q.Queue(maxsize)`
LIFO queue - Stack
Priority queue

Methods
- qsize()
- empty()
- full()
- put()
- get()
- task_done()
- join()


### Python Multiprocessing module
```python
from multiprocessing import Queue
```
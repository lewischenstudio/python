"""
Python Queue Module

FIFO queue          -----> Queue(maxSize = 0)
LIFO queue - Stack
Priority queue

End           Front
- - - - 4 2 5 3 2 1

Methods
- qsize()
- empty()
- full()
- put()
- get()
- task_done()
- join()
"""

import queue as q

customQueue = q.Queue(maxsize=3)
print(customQueue.empty())
print(customQueue.qsize())

customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.qsize())
print(customQueue.full())

print(customQueue.get())
print(customQueue.qsize())

"""
Python Queue Modules
- Collection module
- Queue module
- Multiprocessing Module

Python Collection Module
- The collections.deque Class

End           Front
- - - - 4 2 5 3 2 1

Methods
- deque()
- append()
- popleft()
- clear
"""

from collections import deque

customQueue = deque(maxlen=3)
print(customQueue)

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
customQueue.append(4)
print(customQueue)
print(customQueue.popleft())
print(customQueue)
print(customQueue.clear())
print(customQueue)

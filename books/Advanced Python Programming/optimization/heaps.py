"""
Heaps are data structures designed to quickly find and extract the maximum (or minimum) value in a collection.
    - order of maximum priority insertion with O(log(N)) time complexity
    - heapq module
    - queue.PriorityQueue clas
"""
import heapq
from queue import PriorityQueue

# Heaps
collection = [10, 3, 3, 4, 5, 6]
heapq.heapify(collection)
heapq.heappop(collection)  # extract the minium value
# Returns: 3
heapq.heappush(collection, 1)  # push the integer 1

# queue for Heaps
queue = PriorityQueue()
for element in collection:
    queue.put(element)
queue.get()
# Returns: 3

# Use of tuples
queue = PriorityQueue()
queue.put((3, "priority 3"))
queue.put((2, "priority 2"))
queue.put((1, "priority 1"))
queue.get()
# Returns: (1, "priority 1")

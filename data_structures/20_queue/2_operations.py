"""
Queue operations
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

                                Time complexity             Space complexity
Create Queue                        O(1)                            O(1)
Push                                O(n)                            O(1)
Pop                                 O(1)                            O(1)
Peek                                O(1)                            O(1)
isEmpty                             O(1)                            O(1)
Delete Entire Queue                 O(1)                            O(1)

"""

class Queue:
    def __init__(self) -> None:
        self.items = []
    
    def __str__(self) -> str:
        if self.isEmpty():
            return 'The Queue is empty.'
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, value):
        self.items.append(value)
        return 'The element is inserted at the end of Queue'

    def dequeue(self):
        if self.isEmpty():
            return 'There is no element in this Queue.'
        return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return 'There is no element in this Queue.'
        return self.items[0]

    def delete(self):
        self.items = []



customQueue = Queue()
print(customQueue.isEmpty())
print('\n')

customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue)
print('\n')

customQueue.dequeue()
print(customQueue)
print('\n')

print(customQueue.peek())
print('\n')

customQueue.delete()
print(customQueue)

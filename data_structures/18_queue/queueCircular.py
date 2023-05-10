"""
Circular Queue operations
"""


class QueueCircular:
    def __init__(self, maxSize) -> None:
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self) -> str:
        if self.isEmpty():
            return "The Queue is empty."
        values = [str(x) for x in self.items]
        return " ".join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        return False

    def isEmpty(self):
        return self.top == -1

    def enqueue(self, value):
        # enqueue is to update self.top
        if self.isFull():
            return "The queue is full."
        if self.top + 1 == self.maxSize:
            self.top = 0
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
        self.items[self.top] = value
        return "The element is inserted at the end of Queue"

    def dequeue(self):
        # dequeue is to update self.start
        if self.isEmpty():
            return "There is no element in this Queue."
        first_element = self.items[self.start]
        start = self.start
        if self.start == self.top:
            self.start = -1
            self.top = -1
        elif self.start + 1 == self.maxSize:
            self.start = 0
        else:
            self.start += 1
        self.items[start] = None
        return first_element

    def peek(self):
        if self.isEmpty():
            return "There is no element in this Queue."
        return self.items[self.start]

    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1


customQueue = QueueCircular(3)
print(customQueue.isFull())
print(customQueue.isEmpty())
print("\n")

customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print("\n")

customQueue.dequeue()
print(customQueue)
print("\n")

customQueue.enqueue(2)
print(customQueue)
print("\n")

print(customQueue.peek())
print("\n")

customQueue.dequeue()
print(customQueue)
print("\n")

print(customQueue.peek())
print("\n")

customQueue.delete()
print(customQueue)

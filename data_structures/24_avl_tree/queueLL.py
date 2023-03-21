"""
Linked List Queue

                                Time complexity             Space complexity
Create Queue                        O(1)                            O(1)
Push                                O(1)                            O(1)
Pop                                 O(1)                            O(1)
Peek                                O(1)                            O(1)
isEmpty                             O(1)                            O(1)
Delete Entire Queue                 O(1)                            O(1)
"""


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def __str__(self) -> str:
        return str(self.value)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class LLQueue:
    def __init__(self) -> None:
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = new_node
            self.linkedList.tail = new_node
        else:
            self.linkedList.tail.next = new_node
            self.linkedList.tail = new_node
    
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        return False
    
    def dequeue(self):
        if self.isEmpty():
            return 'There is no node in the Queue.'
        temp_node = self.linkedList.head
        if self.linkedList.head == self.linkedList.tail:
            self.linkedList.head = None
            self.linkedList.tail = None
        else:
            self.linkedList.head = self.linkedList.head.next
        return temp_node

    def peek(self):
        if self.isEmpty():
            return 'There is no node in the Queue.'
        return self.linkedList.head

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None



customQueue = LLQueue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print('\n')

print(customQueue.dequeue())
print('\n')

print(customQueue)
print('\n')

print(customQueue.peek())
print('\n')

customQueue.delete()
print(customQueue)
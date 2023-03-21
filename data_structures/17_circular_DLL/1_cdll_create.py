"""
Singly Linked List

[Head|111] ---> Node: [1|null]
                        111
[Tail:]

Create Head and Tail, initialize with null

Create a blank Node and assign a value to it
and reference to null.

Link Head and Tail with these Node
"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    # Create CDLL
    def create_DSLL(self, value):
        node = Node(value)
        node.prev = node
        node.next = node
        self.head = node
        self.tail = node
        return 'The CSLL has been created'


circular_CSLL = CircularDoublyLinkedList()

circular_CSLL.create_DSLL(1)
print([node.value for node in circular_CSLL])

circular_CSLL.create_DSLL(2)
print([node.value for node in circular_CSLL])

circular_CSLL.create_DSLL(3)
print([node.value for node in circular_CSLL])
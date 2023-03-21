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
        self.next = None
        self.prev = None


class DoublyLinkedList:

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

    # Create DLL
    def create_DLL(self, value):
        node = Node(value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return 'The DLL has been created successfully.'


doublyLL = DoublyLinkedList()
doublyLL.create_DLL(1)

print([node.value for node in doublyLL])

doublyLL.create_DLL(5)

print([node.value for node in doublyLL])
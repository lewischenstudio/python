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


class SLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None


singly_linked_list = SLinkedList()
node1 = Node(1)
node2 = Node(2)

singly_linked_list.head = node1
singly_linked_list.head.next = node2
singly_linked_list.tail = node2
print(singly_linked_list.head)
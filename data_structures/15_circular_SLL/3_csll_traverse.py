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


class CircularSinglyLinkedList:

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

    # Create CSLL
    def create_CSLL(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        return 'The CSLL has been created'
    
    # insert in CSLL
    def insert_SLL(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # insert at the beginning
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            # insert at the end
            elif location == 1:
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node
            # insert at the index
            else:
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                next_node = current_node.next
                current_node.next = new_node
                new_node.next = next_node
            return 'The node has been successfully inserted'

    # Traverse through a CSLL
    def traverse_CSLL(self):
        if self.head is None:
            print('There is not any element for trasversal.')
        else:
            current_node = self.head
            while current_node:
                print('current_node: ', current_node.value)
                current_node = current_node.next
                if current_node == self.tail.next:
                    break


circular_CSLL = CircularSinglyLinkedList()
circular_CSLL.create_CSLL(1)

circular_CSLL.insert_SLL(0, 0)
circular_CSLL.insert_SLL(2, 1)
circular_CSLL.insert_SLL(3, 1)
circular_CSLL.insert_SLL(4, 1)

circular_CSLL.insert_SLL(2, 2)
print(circular_CSLL.insert_SLL(0, 4))

circular_CSLL.traverse_CSLL()
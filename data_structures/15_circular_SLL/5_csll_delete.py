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
    
    # Search an element in CSLL
    def search_CSLL(self, value):
        if self.head is None:
            print('There is no element in this CSLL.')
        else:
            current_node = self.head
            index = 0
            while current_node:
                if current_node.value == value:
                    return f'Index for {value} is {index}'
                current_node = current_node.next
                index += 1
                if current_node == self.tail.next:
                    return 'The node does not exist in this CSLL.'

    # Delete an element in CSLL
    def delete_CSLL(self, location):
        if self.head is None:
            print('There is no node in this CSLL.')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    current_node = self.head
                    while current_node:
                        if current_node.next == self.tail:
                            break
                        current_node = current_node.next
                    self.tail = current_node
                    current_node.next = self.head
            else:
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                next_node = current_node.next
                current_node.next = next_node.next
                    
                




circular_CSLL = CircularSinglyLinkedList()
circular_CSLL.create_CSLL(1)

circular_CSLL.insert_SLL(0, 0)
circular_CSLL.insert_SLL(2, 1)
circular_CSLL.insert_SLL(3, 1)
circular_CSLL.insert_SLL(4, 1)

print([node.value for node in circular_CSLL])

circular_CSLL.delete_CSLL(0)
print('Deleted index = 0: ', [node.value for node in circular_CSLL])

circular_CSLL.delete_CSLL(1)
print('Deleted index = 1: ', [node.value for node in circular_CSLL])

circular_CSLL.delete_CSLL(2)
print('Deleted index = 2: ', [node.value for node in circular_CSLL])
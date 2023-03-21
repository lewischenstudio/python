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
    def create_CDLL(self, value):
        node = Node(value)
        node.prev = node
        node.next = node
        self.head = node
        self.tail = node
        return 'The CSLL has been created'

    # Insert CDLL
    def my_insert_CDLL(self, value, location):
        if self.head == self.tail is None:
            self.create_CDLL(value)
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif location == -1:
                new_node.prev = self.tail
                new_node.next = self.head
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                index = 0
                current_node = self.head
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                    if current_node.next == self.head and index < location:
                        print(f'Inserting {value} to the last position.')
                        # break
                        new_node.prev = self.tail
                        new_node.next = self.head
                        self.tail.next = new_node
                        self.tail = new_node
                        return None
                print('current node: ', current_node.value)
                new_node.next = current_node.next
                new_node.prev = current_node
                current_node.next.prev = new_node
                current_node.next = new_node
            return 'The node has been inserted.'

    def insert_CDLL(self, value, location):
        if self.head is None:
            return 'The CDLL does not exist.'
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                new_node.next = current_node.next
                new_node.prev = current_node
                current_node.next.prev = new_node
                current_node.next = new_node
            return 'The node has been successfully inserted.'

    def traverse_CDLL(self):
        if self.head is None:
            print('There is no node in this list.')
            return None
        current_node = self.head
        while current_node:
            print('current_node: ', current_node.value)
            if current_node.next == self.head:
                break
            current_node = current_node.next
        return None

    def reverse_CDLL(self):
        if self.head is None:
            print('There is no node in this list.')
            return None
        current_node = self.tail
        while current_node:
            print('current_node: ', current_node.value)
            if current_node == self.head:
                break
            current_node = current_node.prev
        return None


circular_CDLL = CircularDoublyLinkedList()
circular_CDLL.create_CDLL(5)
circular_CDLL.insert_CDLL(0,0)
circular_CDLL.insert_CDLL(1,1)
circular_CDLL.insert_CDLL(2,2)

print([node.value for node in circular_CDLL])

circular_CDLL.reverse_CDLL()

print('\n')
circular_CDLL.create_CDLL(0)
circular_CDLL.my_insert_CDLL(2,0)
circular_CDLL.my_insert_CDLL(1,0)
circular_CDLL.my_insert_CDLL(3,-1)
circular_CDLL.my_insert_CDLL(4,-1)
circular_CDLL.my_insert_CDLL(5,3)
circular_CDLL.my_insert_CDLL(6,6)
circular_CDLL.my_insert_CDLL(7,9)
print([node.value for node in circular_CDLL])
circular_CDLL.reverse_CDLL()
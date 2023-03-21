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
    
    # Search CDLL
    def search_CDLL(self, value):
        if self.head is None:
            return 'There is not any node in CDLL.'
        else:
            current_node = self.head
            index = 0
            while current_node:
                if current_node.value == value:
                    print(f'The index is {index} for {value}.')
                    return current_node.value
                if current_node == self.tail:
                    print('The value does not exist in CDLL.')
                    return 'The value does not exist in CDLL.'
                current_node = current_node.next
                index += 1

    # Delete CDLL
    def delete_CDLL(self, location):
        if self.head is None:
            print('There is no node in this CDLL.')
            return None
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    next_node = self.head.next
                    next_node.prev = self.tail
                    self.head = next_node
                    self.tail.next = next_node
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                index = 0
                current_node = self.head
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                    if current_node.next == self.tail and index < location:
                        print('This value doesn\'t exist in the CDLL.')
                        return None
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
            return 'The node is successfully deleted.'



circular_CDLL = CircularDoublyLinkedList()
circular_CDLL.create_CDLL(5)
circular_CDLL.insert_CDLL(0,0)
circular_CDLL.insert_CDLL(1,1)
circular_CDLL.insert_CDLL(2,2)
circular_CDLL.insert_CDLL(3,2)
circular_CDLL.insert_CDLL(4,2)

print([node.value for node in circular_CDLL])

circular_CDLL.delete_CDLL(0)
print([node.value for node in circular_CDLL])

circular_CDLL.delete_CDLL(-1)
print([node.value for node in circular_CDLL])

circular_CDLL.delete_CDLL(-1)
print([node.value for node in circular_CDLL])

circular_CDLL.delete_CDLL(1)
print([node.value for node in circular_CDLL])

circular_CDLL.delete_CDLL(3)
print([node.value for node in circular_CDLL])

circular_CDLL.delete_CDLL(1)
print([node.value for node in circular_CDLL])
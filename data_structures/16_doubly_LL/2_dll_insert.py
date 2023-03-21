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

    # Insert DLL
    def insert_DLL(self, value, location):
        if self.head is None:
            print('The node cannot be inserted.')
        else:
            new_node = Node(value)
            if location == 0:
                new_node.prev = None
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif location == 1:
                new_node.next = None
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                index = 0
                current_node = self.head
                # loop until index before location
                while index < location - 1:
                    if current_node.next is None:
                        print('Maximum location is reached.')
                        return None
                    current_node = current_node.next
                    index += 1
                # insert new node after the current node
                print(f'For index {index}, current node is {current_node.value}')
                new_node.next = current_node.next
                new_node.prev = current_node
                new_node.next.prev = new_node
                current_node.next = new_node



doublyLL = DoublyLinkedList()
doublyLL.create_DLL(5)

print([node.value for node in doublyLL])

doublyLL.insert_DLL(0,0)
doublyLL.insert_DLL(2,1)
doublyLL.insert_DLL(6,2)

print([node.value for node in doublyLL])
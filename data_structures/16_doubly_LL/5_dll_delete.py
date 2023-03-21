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

    # Traverse DLL
    def traverse_DLL(self):
        if self.head is None:
            print('There is no node in this DLL.')
            return None
        current_node = self.head
        while current_node:
            print('current_node: ', current_node.value)
            current_node = current_node.next

    # Reverse traverse DLL
    def reverse_traverse_DLL(self):
        if self.head is None:
            print('There is no node in this DLL.')
            return None
        current_node = self.tail
        while current_node:
            print('current_node: ', current_node.value)
            current_node = current_node.prev

    # Search through DLL
    def serach_DLL(self, value):
        if self.head is None:
            print('There is no node in this DLL.')
            return value
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == value:
                print(f'For {value}, the index is {index}')
                return current_node.value
            index += 1
            current_node = current_node.next
        print('The node does not exist in this list.')
        return value

    # Delete a node from DLL
    def delete_node(self, location):
        if self.head is None:
            print('There is no node in this DLL')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
                self.tail = current_node
                self.tail.next = None
            print('The node has been successfully deleted.')

    # My delete through DLL
    def my_delete_DLL(self, location):
        if self.head is None:
            print('There is no node in this DLL.')
            return None
        else:
            if location == 0:
                if self.head.next is None:
                    print(f'Deleted {self.head.value} from index {location}.')
                    self.head = None
                    self.tail = None
                else:
                    print(f'Deleted {self.head.value} from index {location}.')
                    next_node = self.head.next
                    self.head = self.head.next
                    next_node.prev = None
            elif location == -1:
                if self.head.next is None:
                    self.head = None
                    self.tail = None
                else:
                    print(f'Deleted {self.tail.value} from index {location}.')
                    self.tail = self.tail.prev
                    self.tail.next = None
                    return None
            else:
                index = 0
                current_node = self.head
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                    if current_node.next is None:
                        print('This node does not exist in this list.')
                        return None
                next_node = current_node.next
                next_next_node = next_node.next
                if next_next_node is None:
                    self.tail = current_node
                    current_node.next = None
                    print(f'Deleted {next_node.value} from index {location}.')
                    return None
                current_node.next = next_next_node
                next_next_node.prev = current_node
                print(f'Deleted {next_node.value} from index {location}.')
                return None


doublyLL = DoublyLinkedList()
doublyLL.create_DLL(5)

print([node.value for node in doublyLL])

doublyLL.insert_DLL(0,0)
doublyLL.insert_DLL(1,1)
doublyLL.insert_DLL(2,1)
doublyLL.insert_DLL(3,1)
doublyLL.insert_DLL(4,1)
doublyLL.insert_DLL(5,1)

print([node.value for node in doublyLL])

doublyLL.my_delete_DLL(3)
print([node.value for node in doublyLL])

doublyLL.my_delete_DLL(5)
print([node.value for node in doublyLL])

doublyLL.my_delete_DLL(2)
print([node.value for node in doublyLL])

doublyLL.my_delete_DLL(0)
print([node.value for node in doublyLL])

doublyLL.my_delete_DLL(-1)
print([node.value for node in doublyLL])
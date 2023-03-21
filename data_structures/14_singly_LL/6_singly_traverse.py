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
    
    # iteration to the next element
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in Linked List
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
            # insert at the end
            elif location == 1:
                self.tail.next = new_node
                self.tail = new_node
            # insert at the index
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
                if temp_node == self.tail:
                    self.tail = new_node

    # traverse Singly Linked List
    def traverse_SLL(self):
        if self.head is None:
            print('The Singly Linked List does not exist.')
        else:
            node = self.head
            while node is not None:
                print('value: ', node.value)
                node = node.next


singly_linked_list = SLinkedList()
singly_linked_list.insert_SLL(1, 1)
singly_linked_list.insert_SLL(2, 1)
singly_linked_list.insert_SLL(3, 1)
singly_linked_list.insert_SLL(4, 1)

singly_linked_list.insert_SLL(0, 0)
singly_linked_list.insert_SLL(0, 4)
print([node.value for node in singly_linked_list])
singly_linked_list.traverse_SLL()


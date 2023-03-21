"""
Create three classes for Linked List in Python
"""

from random import randint, choice


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.value)



class LinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
    
    def __str__(self) -> str:
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    
    def add(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self
    
    def repeated(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        rand_list = []
        for i in range(int(n / 2)):
            rand_int = randint(min_value, max_value)
            self.add(rand_int)
            rand_list.append(rand_int)
        for i in range(int(n/ 2)):
            self.add(choice(rand_list))
        if n % 2 == 1:
            self.add(randint(min_value, max_value))
        return self

customLL = LinkedList()
customLL.generate(10, 0, 99)

print(customLL)
print(len(customLL))

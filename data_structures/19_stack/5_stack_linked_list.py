"""
Stack creation

Stack using List
    - Easy to implement
    - Speed problem when it grows

Stack using Linked List
    - Fast performance
    - Implementation is not easy

Time and Space complexity of Stack operations with List

                                Time complexity             Space complexity
Create Stack                        O(1)                            O(1)
Push                                O(1)                            O(1)
Pop                                 O(1)                            O(1)
Peek                                O(1)                            O(1)
isEmpty                             O(1)                            O(1)
Delete Entire Stack                 O(1)                            O(1)
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class StackLL:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return 'There is no element in the stack.'
        node_value = self.LinkedList.head.value
        self.LinkedList.head = self.LinkedList.head.next
        return node_value
    
    def peek(self):
        if self.isEmpty():
            return 'There is no element in the stack.'
        node_value = self.LinkedList.head.value
        return node_value
    
    def delete(self):
        self.LinkedList.head = None


customStack = StackLL()

print(customStack.isEmpty())

customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

print('-----------')
customStack.pop()
print(customStack)

print('-----------')
print(customStack.peek())

print('-----------')
print(customStack.delete())
print(customStack)

# print(customStack.traverse())
# print('isEmpty: ', customStack.isEmpty())

# customStack.pop()
# print('pop: ', customStack.traverse())

# customStack.peek()
# print('peek: ', customStack.traverse())

# customStack.delete()
# print('delete: ', customStack.traverse())
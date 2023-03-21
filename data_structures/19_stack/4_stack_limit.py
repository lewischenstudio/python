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
Push                             O(1) / O(n^2)                      O(1)
Pop                                 O(1)                            O(1)
Peek                                O(1)                            O(1)
isEmpty                             O(1)                            O(1)
Delete Entire Stack                 O(1)                            O(1)
"""

class Stack:
    def __init__(self, max_size) -> None:
        self.list = []
        self.max_size = max_size
    
    def __str__(self) -> str:
        if self.list == []:
            return ''
        values = [str(self.list[i]) for i in range(len(self.list) - 1, -1, -1)]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    def isFull(self):
        if len(self.list) == self.max_size:
            return True
        return False

    # Push
    def push(self, value):
        if self.isFull():
            return 'The stack is full'
        self.list.append(value)
        return 'The element is inserted'

    # Pop the top element
    def pop(self):
        if self.isEmpty():
            return 'There is no element in the stack'
        return self.list.pop(-1)

    # Peek the bottom element
    def peek(self):
        if self.isEmpty():
            return 'There is no element in the stack'
        return self.list[-1]

    # Delete
    def delete(self):
        self.list = None


customStack = Stack(4)

print(customStack.isEmpty())
print(customStack.isFull())

customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

customStack.push(4)
print(customStack.push(5))
print(customStack)
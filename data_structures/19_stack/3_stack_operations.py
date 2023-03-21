"""
Stack creation

Stack using List
    - Easy to implement
    - Speed problem when it grows

Stack using Linked List
    - Fast performance
    - Implementation is not easy
"""

class Stack:
    def __init__(self) -> None:
        self.list = []
    
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

    # Push
    def push(self, value):
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


customStack = Stack()
print(customStack)
print('\n')

print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

print('\n')
print('pop: ', customStack.pop())
print(customStack)

print('\n')
customStack.push(3)
print('peek: ', customStack.peek())
print(customStack)
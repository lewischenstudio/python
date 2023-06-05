"""
Interview Questions - 1: Three in One

Describe how you could use a single Python list to implement three stacks.
"""


class MultiStack:
    def __init__(self, stacksize) -> None:
        self.numberstacks = 3
        self.custList = [0] * (stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize

    def __str__(self) -> str:
        stack_values = []
        for i in range(self.numberstacks):
            stack_msg = f"stack {i}: "
            first_index = int(self.stacksize * i)
            last_index = self.indexOfTop(i) + 1
            stack_val = []
            for j in range(first_index, last_index, 1):
                stack_val.append(str(self.custList[j]))
            stack_add = "None" if stack_val == [] else " ".join(stack_val)
            stack_values.append(stack_msg + stack_add)
        return ("\n").join(stack_values)

    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        return False

    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        return False

    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return "The stack is full"
        self.sizes[stacknum] += 1
        self.custList[self.indexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty():
            return "The stack is empty."
        value = self.custList[self.indexOfTop(stacknum)]
        self.custList[self.indexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty."
        value = self.custList[self.indexOfTop(stacknum)]
        return value


customStack = MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
print("\n")

customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(3, 2)
print(customStack)

print(customStack.peek(1))

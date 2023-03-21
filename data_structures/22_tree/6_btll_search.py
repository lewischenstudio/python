"""
Searching for a node in Binary Tree using Linked List

Level Order Search - search level by level

"""
from queueLL import LLQueue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode('Drinks')
N2 = TreeNode('Hot')
N3 = TreeNode('Cold')
newBT.leftChild = N2
newBT.rightChild = N3

N4 = TreeNode('Tea')
N5 = TreeNode('Cofee')
N2.leftChild = N4
N3.rightChild = N5

N8 = TreeNode('Red Tea')
N9 = TreeNode('Green Tea')
N4.leftChild = N8
N4.rightChild = N9

N6 = TreeNode('Cola')
N7 = TreeNode('Fanta')
N3.leftChild = N6
N3.rightChild = N7


# LevelOrder Search
def searchBT(rootNode, nodeValue):
    if not rootNode:
        return 'The BT does not exist.'
    customQueue = LLQueue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        if root.value.data == nodeValue:
            return 'Success'
        if root.value.leftChild:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild:
            customQueue.enqueue(root.value.rightChild)
    return 'Not Found'

print('LevelOrder Search')
print(searchBT(newBT, 'Tea'))
print('\n')

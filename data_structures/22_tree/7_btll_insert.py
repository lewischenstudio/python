"""
Insert a node in Binary Tree using Linked List

- A root node is blank
- The tree exists and we have to look for a first vacant place


Traversal of Binary Tree
                 N1
               /   \  
             /       \  
           /           \  
         N2             N3  
        /  \           /  \ 
      N4    N5       N6    N7
     /  \     
   N8    N9     

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
N2.rightChild = N5

N8 = TreeNode('Red Tea')
N9 = TreeNode('Green Tea')
N4.leftChild = N8
N4.rightChild = N9


# LevelOrder Traversal
def levelOrderTraversal(rootNode):
    if not rootNode:
        return None
    customQueue = LLQueue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftChild:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild:
            customQueue.enqueue(root.value.rightChild)

# Insert
def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
        return newNode
    customQueue = LLQueue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        if root.value.leftChild:
            customQueue.enqueue(root.value.leftChild)
        else:
            root.value.leftChild = newNode
            return 'Successfully inserted'
        if root.value.rightChild:
            customQueue.enqueue(root.value.rightChild)
        else:
            root.value.rightChild = newNode
            return 'Successfully inserted'

newNode = TreeNode('Cola')
print(insertNodeBT(newBT, newNode))
print(levelOrderTraversal(newBT))
print(N3.leftChild.data == newNode.data)

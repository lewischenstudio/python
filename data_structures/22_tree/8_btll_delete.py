"""
Delete a node in Binary Tree using Linked List

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

N6 = TreeNode('Cola')
N7 = TreeNode('Fanta')
N3.leftChild = N6
N3.rightChild = N7


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



# Get Deepest Node
def getDeepestNode(rootNode):
    if not rootNode:
        return None
    customQueue = LLQueue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
        root = customQueue.dequeue()
        if root.value.leftChild:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild:
            customQueue.enqueue(root.value.rightChild)
    deepestNode = root.value
    return deepestNode

deepestNode = getDeepestNode(newBT)
print('deepestNode: ', deepestNode.data)
print('\n')


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return None
    customQueue = LLQueue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
        root = customQueue.dequeue()
        if root.value is dNode:
            root.value = None
            return 
        if root.value.rightChild:
            if root.value.rightChild is dNode:
                print('Successfully deleted %s' % dNode.data)
                root.value.rightChild = None
                return
            else:
                customQueue.enqueue(root.value.rightChild)
        if root.value.leftChild:
            if root.value.leftChild is dNode:
                print('Successfully deleted %s' % dNode.data)
                root.value.leftChild = None
                return
            else:
                customQueue.enqueue(root.value.leftChild)


# deepestNode = getDeepestNode(newBT)
# deleteDeepestNode(newBT, deepestNode)
# levelOrderTraversal(newBT)
# print('\n')


def deleteNodeBT(rootNode, dNode):
    if not rootNode:
        return None
    customQueue = LLQueue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
        root = customQueue.dequeue()
        if root.value.data == dNode:
            dNode = getDeepestNode(rootNode)
            root.value.data = dNode.data
            deleteDeepestNode(root.value, dNode)
            return 'The node has been successfully deleted'
        if root.value.leftChild:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild:
            customQueue.enqueue(root.value.rightChild)
    return 'Failed to delete'

# deleteNodeBT(newBT, 'Tea')
# levelOrderTraversal(newBT)
# print('\n')


# Delete My Method: delete a designated node or the last node
def myDeleteNodeBT(rootNode, deleteNode=None):
    if not rootNode:
        return None
    customQueue = LLQueue()
    customQueue.enqueue(rootNode)
    thisNode = None
    lastNode = None
    while not customQueue.isEmpty():
        root = customQueue.dequeue()
        if root.value.data == deleteNode:
            thisNode = root.value
        if root.value.leftChild:
            customQueue.enqueue(root.value.leftChild)
            lastNode = root
        if root.value.rightChild:
            customQueue.enqueue(root.value.rightChild)
            lastNode = root
    if thisNode and deleteNode:
        thisNode.data = None
        thisNode.leftChild = None
        thisNode.rightChild = None
        print('Successfully deleted %s' % deleteNode)
        return None
    if lastNode:
        if lastNode.value.rightChild:
            print('Successfully deleted %s' % lastNode.value.rightChild.data)
            lastNode.value.rightChild = None
            return None
        elif lastNode.value.leftChild:
            print('Successfully deleted %s' % lastNode.value.leftChild.data)
            lastNode.value.leftChild = None
            return None
    return 'Failed to delete'


myDeleteNodeBT(newBT)
print(levelOrderTraversal(newBT))
print('\n')

myDeleteNodeBT(newBT, 'Tea')
print(levelOrderTraversal(newBT))



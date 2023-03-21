"""
Create Binary Tree using Linked List

- Creation of Tree
- Insertion of a node
- Deletion of a node
- Search for a value
- Traverse all nodes
- Deletion of tree

Traversal of Binary Tree
                 N1
               /   \  
             /       \  
           /           \  
         N2            N3  
        /  \          /  \ 
      N4    N5      N6    N7
     /        \ 
   N8          N9

Depth first search
- Preorder traversal
  - Root node -> Left Subtree -> Right Subtree
  - N1 -> N2 -> N4 -> N8 -> N9 -> N5 -> N3 -> N6 -> N7

- Inorder traversal
  - Left Subtree -> Root Node -> Right Subtree
  - N8 -> N4 -> N9 -> N2 -> N5 -> N1 -> N6 -> N3 -> N7

- Post order traversal
  - Left Subtree -> Right Subtree -> Root Node
  - N8 -> N9 -> N4 -> N5 -> N2 -> N6 -> N3 -> N7 -> -> N1

Breadth first search
- Level order traversal
  - Level by level: level 1 -> level 2 -> level 3 -> ...
  - N1 -> N2 -> N3 -> N4 -> N5 -> N6 -> N7 -> N8 -> N9

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

# Preorder Traversal
def preOrderTraversal(rootNode):
    if not rootNode:
        return None
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

print('Preorder Traversal')
preOrderTraversal(newBT)
print('\n')

# Inorder Traversal
def inOrderTraversal(rootNode):
    if not rootNode:
        return None
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

print('Inorder Traversal')
inOrderTraversal(newBT)
print('\n')

# PostOrder Traversal
def postOrderTraversal(rootNode):
    if not rootNode:
        return None
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

print('Postorder Traversal')
postOrderTraversal(newBT)
print('\n')

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

print('LevelOrder Traversal')
levelOrderTraversal(newBT)
print('\n')



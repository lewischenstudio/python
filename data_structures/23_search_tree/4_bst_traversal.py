"""
Traversal of Binary Search Tree
                70
              /   \  
            /       \  
          /           \  
         50            90
        /  \          /  \ 
      /      \      /      \ 
    30        60   80       100
   /  \      / 
 20    40  

Depth first search
- Preorder traversal:   root node --> left subtree --> right subtree
- Inorder traversal:    left subtree --> root node --> right subtree
- Post order traversal: left subtree --> right subtree --> root node

Breath first search
- Level order traversal

"""
from queueLL import LLQueue

class BSTNode:
  def __init__(self, data) -> None:
    self.data = data
    self.leftChild = None
    self.rightChild = None

def insertNode(rootNode, nodeValue: int):
    if rootNode.data is None:
      rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
      if rootNode.leftChild is None:
        rootNode.leftChild = BSTNode(nodeValue)
      else:
        insertNode(rootNode.leftChild, nodeValue)
    else:
      if rootNode.rightChild is None:
        rootNode.rightChild = BSTNode(nodeValue)
      else:
        insertNode(rootNode.rightChild, nodeValue)
    return 'The node has been successfully inserted'

def preOrderTraversal(rootNode):
  if not rootNode:
    return
  print(rootNode.data)
  preOrderTraversal(rootNode.leftChild)
  preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
  if not rootNode:
    return
  inOrderTraversal(rootNode.leftChild)
  print(rootNode.data)
  inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
  if not rootNode:
    return
  postOrderTraversal(rootNode.leftChild)
  postOrderTraversal(rootNode.rightChild)
  print(rootNode.data)
  

def levelOrderTraversal(rootNode):
  if not rootNode:
    return
  customQue = LLQueue()
  customQue.enqueue(rootNode)
  while not (customQue.isEmpty()):
    root = customQue.dequeue()
    print(root.value.data)
    if root.value.leftChild:
      customQue.enqueue(root.value.leftChild)
    if root.value.rightChild:
      customQue.enqueue(root.value.rightChild)


newBST = BSTNode(None)
print(insertNode(newBST, 70))
print(insertNode(newBST, 50))
print(insertNode(newBST, 90))
print(insertNode(newBST, 30))
print(insertNode(newBST, 60))
print(insertNode(newBST, 80))
print(insertNode(newBST, 100))
print(insertNode(newBST, 20))
print(insertNode(newBST, 40))
print('\n')

print('Preorder Traversal')
preOrderTraversal(newBST)
print('\n')

print('Inorder Traversal')
inOrderTraversal(newBST)
print('\n')

print('Postorder Traversal')
postOrderTraversal(newBST)
print('\n')

print('Levelorder Traversal')
levelOrderTraversal(newBST)
print('\n')

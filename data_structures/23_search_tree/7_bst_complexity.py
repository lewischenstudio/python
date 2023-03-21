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
     
                                            Time complexity     Space complexity
Create BST                                      O(1)                   O(1)        
Insert a node to BST                            O(logN)                O(logN)
Traverse BST                                    O(logN)                O(logN)
Search for a node in BST                        O(N)                   O(N)
Delete a node from BST                          O(logN)                O(logN)
Delete entire BST                               O(1)                   O(1)

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


def searchNode(rootNode, nodeValue):
  if rootNode.data == nodeValue:
    print('The value is found')
  elif nodeValue < rootNode.data:
    if rootNode.leftChild.data == nodeValue:
      print('The value is found')
    else:
      searchNode(rootNode.leftChild, nodeValue)
  else:
    if rootNode.rightChild.data == nodeValue:
      print('The value is found')
    else:
      searchNode(rootNode.rightChild, nodeValue)

def minValue(bstNode):
  current = bstNode
  while current.leftChild is not None:
    current = current.leftChild
  return current


def maxValue(bstNode):
  current = bstNode
  while current.rightChild:
    current = current.rightChild
  return current


def deleteNode(rootNode, nodeValue):
  if rootNode is None:
    return rootNode
  if nodeValue < rootNode.data:
    rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
  elif nodeValue > rootNode.data:
    rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
  else:
    if rootNode.leftChild is None:
      temp = rootNode.rightChild
      rootNode = None
      return temp
    if rootNode.rightChild is None:
      temp = rootNode.rightChild
      rootNode = None
      return temp
    
    temp = minValue(rootNode.rightChild)
    rootNode.data = temp.data
    rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
  return rootNode


def entireNode(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return 'The BST has been successfully deleted.'


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

searchNode(newBST, 30)

deleteNode(newBST, 100)
levelOrderTraversal(newBST)

entireNode(newBST)
levelOrderTraversal(newBST)
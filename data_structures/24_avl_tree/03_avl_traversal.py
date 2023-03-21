"""
AVL Tree
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

"""
from queueLL import LLQueue

class AVLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


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


newAVL = AVLNode(10)

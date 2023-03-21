"""
Binary Search Tree
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

class BSTNode:
  def __init__(self, data) -> None:
    self.data = data
    self.leftChild = None
    self.rightChild = None

  # my solution
  @classmethod
  def insert(cls, rootNode, nodeValue: int):
    if nodeValue is None:
      print(f'Node value cannot be none')
      return
    if rootNode.data is None:
      rootNode.data = nodeValue
      print(f'Inserted root {nodeValue}\n')
    elif nodeValue <= rootNode.data:
      if rootNode.leftChild is None:
        rootNode.leftChild = BSTNode(nodeValue)
        print(f'Inserted {nodeValue} as the left child of node {rootNode.data}\n')
      else:
        cls.insert(rootNode.leftChild, nodeValue)
    else:
      if rootNode.rightChild is None:
        rootNode.rightChild = BSTNode(nodeValue)
        print(f'Inserted {nodeValue} as the right child of node {rootNode.data}\n')
      else:
        cls.insert(rootNode.rightChild, nodeValue)
    return

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


newBST = BSTNode(None)
# newBST.insert(newBST, 70)
# newBST.insert(newBST, 50)
# newBST.insert(newBST, 90)
# newBST.insert(newBST, 30)
# newBST.insert(newBST, 60)
# newBST.insert(newBST, 80)
# newBST.insert(newBST, 100)
# newBST.insert(newBST, 20)
# newBST.insert(newBST, 40)

print(insertNode(newBST, 70))
print(insertNode(newBST, 50))
print(insertNode(newBST, 90))
print(insertNode(newBST, 30))
print(insertNode(newBST, 60))
print(insertNode(newBST, 80))
print(insertNode(newBST, 100))
print(insertNode(newBST, 20))
print(insertNode(newBST, 40))
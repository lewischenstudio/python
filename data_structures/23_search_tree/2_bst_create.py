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


newBST = BSTNode(None)

"""
Search a node in Binary Tree using Python List


Binary Tree
                  N1
                /   \  
              /       \  
            /          \  
          N2           N3  
        /  \          /  \ 
      /      \      /      \ 
    N4        N5   N6       N7
   /  \      /   
 N8    N9  new   


0   1   2   3   4   5   6   7   8   9   10    11
x   N1  N2  N3  N4  N5  N6  N7  N8  N9  new

Left child = cell[2x]       ---->     x = 3, cell[2x3 = 6]
Right child = cell[2x+1]    ---->     x = 3, cell[2x3+1=7]

Time complexity:  O(1)
Space complexity: O(n)
"""


class BinaryTree:
  def __init__(self, size):
    self.customList = size * [None]
    self.lastUsedIndex = 0
    self.maxSize = size

  def insertNode(self, value):
    if self.lastUsedIndex + 1 == self.maxSize:
      return 'The Binary Tree is full.'
    self.customList[self.lastUsedIndex + 1] = value
    self.lastUsedIndex += 1
    return 'The value has been successfully inserted'

  def searchNode(self, nodeValue):
    for i in range(len(self.customList)):
      if self.customList[i] == nodeValue:
        return 'Success'
    return 'Not found'


newBT = BinaryTree(8)
print(newBT.insertNode('Drinks'))
print(newBT.insertNode('Hot'))
print(newBT.insertNode('Cold'))

print(newBT.searchNode('Tea'))
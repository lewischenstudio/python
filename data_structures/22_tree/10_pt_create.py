"""
Create Binary Tree using Python List


Binary Tree
         N1
       /   \  
     /       \  
    N2        N3  
   /  \      /  \ 
 N4    N5  N6    N7


0   1   2   3   4   5   6   7   8
x   N1  N2  N3  N4  N5  N6  N7  N8

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


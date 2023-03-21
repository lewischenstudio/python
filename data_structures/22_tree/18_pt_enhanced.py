"""
Binary Tree using Python List

Binary Tree
                Drinks
               /    \  
             /        \  
           /            \  
         Hot            Cold
        /  \            /  \ 
      /      \        /      \ 
    Tea     Coffee   N6       N7



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

  def insertNode(self, value, parent=None):
    if self.lastUsedIndex + 1 == self.maxSize:
      return 'The Binary Tree is full.'
    self.lastUsedIndex += 1
    parent_node = 0
    for i in range(len(self.customList)):
      if self.customList[i] and \
        self.customList[i].get('value') == parent:
        parent_node = i
    self.customList[self.lastUsedIndex] = {
      'node': self.lastUsedIndex if parent_node == 0 else parent_node,
      'value': value
    }
    return 'The value has been successfully inserted'

  def searchNode(self, nodeValue):
    for i in range(len(self.customList)):
      if self.customList[i].get('value') == nodeValue:
        return 'Success'
    return 'Not found'
  
  def preOrderTraversal(self, index, arr):
    if index > self.lastUsedIndex:
      return
    print(self.customList[index].get('value'))
    arr.append(self.customList[index].get('value'))
    self.preOrderTraversal(index*2, arr)
    self.preOrderTraversal(index*2 + 1, arr)

  def inOrderTraversal(self, index, arr):
    if index > self.lastUsedIndex:
      return
    self.inOrderTraversal(index*2, arr)
    print(self.customList[index].get('value'))
    arr.append(self.customList[index].get('value'))
    self.inOrderTraversal(index*2 + 1, arr)

  def postOrderTraversal(self, index, arr):
    if index > self.lastUsedIndex:
      return
    self.postOrderTraversal(index*2, arr)
    self.postOrderTraversal(index*2 + 1, arr)
    print(self.customList[index].get('value'))
    arr.append(self.customList[index].get('value'))

  def levelOrderTraversal(self, index, arr):
    if index > self.lastUsedIndex:
      return
    for i in range(index, self.lastUsedIndex + 1):
      print(self.customList[i])
      arr.append(self.customList[i].get('value'))

  def deleteNode(self, value):
    if self.lastUsedIndex == 0:
      return 'There is not any node to delete'
    for i in range(1, self.lastUsedIndex + 1):
      node_i = self.customList[i]
      node_value = node_i.get('node')
      if node_i.get('value') == value:
        if node_value < i:
          for j in range(i, len(self.customList) - 1):
            self.customList[j] = self.customList[j + 1]
          self.lastUsedIndex -= 1
        else:
          for j in range(i, len(self.customList)):
            if self.customList[j]['node'] == node_value:
              self.customList[j]['value'] = None
          if self.customList[i + 1].get('node') != self.customList[i].get('node'):
            next_val = self.customList[i + 1].get('value')
            self.customList[i + 1]['value'] = None
            self.customList[i] = {**self.customList[i + 1], 'value': next_val}
    self.re_insert()
    return 'The node has been successfully deleted'
  
  def re_insert(self):
    new_customList = [None]
    lastUsedIndex = 0
    for i in range(self.lastUsedIndex + 1):
      this_node = self.customList[i]
      if this_node and this_node.get('value'):
        new_customList.append({
          'node': this_node.get('node'),
          'value': this_node.get('value')
        })
        lastUsedIndex += 1
    self.customList = new_customList
    self.lastUsedIndex = lastUsedIndex

  def entire(self):
    self.customList = None
    self.lastUsedIndex = 0
    return 'The BT has been successfully deleted.'


newBT = BinaryTree(8)
print(newBT.insertNode('Drinks'))
print(newBT.insertNode('Hot'))
print(newBT.insertNode('Cold'))
print(newBT.insertNode('Tea', 'Hot'))
print(newBT.insertNode('Coffee', 'Hot'))
print(newBT.insertNode('Cola', 'Cold'))
print(newBT.insertNode('Sprite', 'Cold'))


arr = []
newBT.levelOrderTraversal(1, arr)
print('\n')

arr = []
newBT.deleteNode('Hot')
newBT.deleteNode('Cold')
newBT.levelOrderTraversal(1, arr)
print('arr: ', arr)
print('\n')

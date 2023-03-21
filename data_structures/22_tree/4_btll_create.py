"""
Create Binary Tree using Linked List

- Creation of Tree
- Insertion of a node
- Deletion of a node
- Search for a value
- Traverse all nodes
- Deletion of tree

"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode('Drinks')
N2 = TreeNode('Hot')
N3 = TreeNode('Cold')
print(newBT)
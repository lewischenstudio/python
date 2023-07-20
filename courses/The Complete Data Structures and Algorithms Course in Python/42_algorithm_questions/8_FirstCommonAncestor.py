"""
Question 8: First Common Ancestor - LeetCode 236

Design an algorithm and write code to find the first common ancestor of two
nodes in a binary tree. Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.


firstCommonAncestor works for the following binary search tree
           55
          /  \ 
         /    \ 
       /        \ 
     44          88
    /  \        /  \ 
   33  54      77   95
  / \               / \ 
 22  35            90   99

           55
          /  \ 
         /    \ 
       /        \ 
     35          70
    /  \        /  \ 
   22  44      60   88
    \    \          / \    
     33   54       75 95 
"""  # noqa

import unittest


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        self.parent = None
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


def first_common_ancestor(node1: Node, node2: Node):
    """
    1. append current node to adjacent node list
    2. assign current node to the parent node until it reaches the root node
    """
    search1, search2 = node1, node2
    ancestors1, ancestors2 = [], []
    while search1 or search2:
        if search1:
            if search1 in ancestors2:
                return search1
            ancestors1.append(search1)
            search1 = search1.parent
            print(ancestors1)
        if search2:
            if search2 in ancestors1:
                return search2
            ancestors2.append(search2)
            search2 = search2.parent
            print(ancestors2)
    return None


def insertNode(rootNode, nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue
        return rootNode
    elif nodeValue <= rootNode.data:
        if rootNode.left is None:
            rootNode.left = Node(nodeValue)
            return rootNode.left
        else:
            insertNode(rootNode.left, nodeValue)
    else:
        if rootNode.right is None:
            rootNode.right = Node(nodeValue)
            return rootNode.right
        else:
            insertNode(rootNode.right, nodeValue)


# My method for binary search tree
def binarySearchNode(rootNode, nodeValue, arr):
    arr.append(rootNode.data)
    if rootNode.data == nodeValue:
        return
    elif nodeValue < rootNode.data:
        if not rootNode.left:
            arr.append(nodeValue)
            return
        if rootNode.left.data != nodeValue:
            binarySearchNode(rootNode.left, nodeValue, arr)
    else:
        if not rootNode.right:
            arr.append(nodeValue)
            return
        if rootNode.right.data != nodeValue:
            binarySearchNode(rootNode.right, nodeValue, arr)


def firstCommonAncestor(node, value1, value2):
    arr1 = []
    arr2 = []
    binarySearchNode(node, value1, arr1)
    binarySearchNode(node, value2, arr2)
    if value1 in arr1 or value2 in arr2:
        return None
    common_nodes = [item for item in arr2 if item in arr1]
    if len(common_nodes) == 0:
        return None
    if max(common_nodes) > node.data:
        return max(common_nodes)
    return min(common_nodes)


class Test(unittest.TestCase):
    def test_first_common_ancestor(self):
        node1 = Node(11, Node(55), Node(77, Node(44)))
        node2 = Node(22, Node(99))
        self.assertEqual(first_common_ancestor(node1, node2), None)
        node3 = Node(33, node1, Node(88, Node(123, None, node2)))
        self.assertEqual(first_common_ancestor(node1, node2), node3)

    def test_firstCommonAncestor_1(self):
        newBST = Node(None)
        binary_list = [55, 44, 33, 22, 35, 54, 88, 77, 95, 90, 99]
        for value in binary_list:
            insertNode(newBST, value)
        self.assertEqual(firstCommonAncestor(newBST, 22, 35), 33)
        self.assertEqual(firstCommonAncestor(newBST, 33, 54), 44)
        self.assertEqual(firstCommonAncestor(newBST, 77, 95), 88)
        self.assertEqual(firstCommonAncestor(newBST, 22, 99), 55)
        self.assertEqual(firstCommonAncestor(newBST, 44, 100), None)
        self.assertEqual(firstCommonAncestor(newBST, 3, 99), None)
        self.assertEqual(firstCommonAncestor(newBST, 100, 89), None)

    def test_firstCommonAncestor_2(self):
        newBST = Node(None)
        binary_list = [55, 35, 22, 33, 44, 54, 70, 60, 88, 75, 95]
        for value in binary_list:
            insertNode(newBST, value)
        self.assertEqual(firstCommonAncestor(newBST, 33, 54), 35)
        self.assertEqual(firstCommonAncestor(newBST, 22, 44), 35)
        self.assertEqual(firstCommonAncestor(newBST, 75, 95), 88)
        self.assertEqual(firstCommonAncestor(newBST, 60, 88), 70)
        self.assertEqual(firstCommonAncestor(newBST, 35, 70), 55)
        self.assertEqual(firstCommonAncestor(newBST, 44, 100), None)
        self.assertEqual(firstCommonAncestor(newBST, 3, 88), None)
        self.assertEqual(firstCommonAncestor(newBST, 100, 89), None)


if __name__ == "__main__":
    unittest.main()

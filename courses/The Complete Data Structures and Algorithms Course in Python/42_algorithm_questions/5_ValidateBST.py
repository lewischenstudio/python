"""
Question 5: Validate BST - LeetCode 98

Implement a function to check if a binary tree is a Binary Search Tree.

Invalid BST 
      4
    /   \ 
   /     \ 
  2       5 
 / \     / \ 
1   3   6   3
"""  # noqa


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def helper(node, minValue=float("-inf"), maxValue=float("inf")):
    if not node:
        return True
    val = node.val
    if val <= minValue or val >= maxValue:
        return False

    if not helper(node.right, val, maxValue):
        return False

    if not helper(node.left, minValue, val):
        return False

    return True


def isBSTHelper(root):
    if root is None:
        return 0
    left = isBSTHelper(root.left)
    if left != 0 and left > root.val:
        return -1
    right = isBSTHelper(root.right)
    if right != 0 and right < root.val:
        return -1
    return root.val


def isValidBST(root):
    return isBSTHelper(root) > -1
    # return helper(root)


root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)

print(isValidBST(root1))

root2 = TreeNode(4)
root2.left = TreeNode(1)
root2.right = TreeNode(3)

print(isValidBST(root2))

root3 = TreeNode(4)
N2 = TreeNode(2)
N3 = TreeNode(5)
N4 = TreeNode(1)
N5 = TreeNode(3)
N6 = TreeNode(6)
N7 = TreeNode(3)
root3.left = N2
root3.right = N3
N2.left = N4
N2.right = N5
N5.left = N6
N3.right = N7

print(isValidBST(root3))

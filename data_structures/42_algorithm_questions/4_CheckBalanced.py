"""
Question 4: Check Balanced - LeetCode 110

Implement a function to check if a binary tree is balanced. For the purposes
of this question, a balanced tree is defined to be a tree such that the
heights of the two subtrees of any node never differ by more than one.
"""


def isBalancedHelper(root):
    if root is None:
        return 0
    leftHeight = isBalancedHelper(root.left)
    if leftHeight == -1:
        return -1
    rightHeight = isBalancedHelper(root.right)
    if rightHeight == -1:
        return -1
    if abs(leftHeight - rightHeight) > 1:
        return -1
    return max(leftHeight, rightHeight) + 1


def isBalanced(root):
    return isBalancedHelper(root) > -1


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


N1 = Node("N1")
N2 = Node("N2")
N3 = Node("N3")
N4 = Node("N4")
N5 = Node("N5")
N6 = Node("N6")
N7 = Node("N7")
N8 = Node("N8")
N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N3.right = N6
N5.left = N7
N7.left = N8

print(isBalanced(N1))

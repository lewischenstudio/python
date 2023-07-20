"""
Question 6: In-order Successor in BST - LeetCode 285

Write an algorithm to find the next node (i.e in-order successor) of given
node in a binary search tree. You may assume that each node has a link to
its parent.
       4
      / \ 
    /     \ 
  2        8
 / \      / \ 
1   3    5   9
"""  # noqa


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
        return node


def minValue(node):
    current = node
    while current is not None:
        if current.left is None:
            break
        current = current.left
    return current


def inOrderSuccessor(root, n):
    if n.right is not None:
        return minValue(n.right)

    p = n.parent
    while p is not None:
        if n != p.right:
            break
        n = p
        p = p.parent
    return p


root = None
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 8)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 5)
root = insert(root, 9)

temp = root.left  # 2

successor = inOrderSuccessor(root, temp)

if successor is not None:
    print("Inorder successor of %d is %d" % (temp.data, successor.data))
else:
    print("Inorder successor does not exist")

next = inOrderSuccessor(root, successor)

if successor is not None:
    print("Inorder successor of %d is %d" % (successor.data, next.data))
else:
    print("Inorder successor does not exist")


def inOrderTraversalList(root, arr):
    if not root:
        return
    inOrderTraversalList(root.left, arr)
    arr.append(root.data)
    inOrderTraversalList(root.right, arr)


def inOrderSuccessor(root, value):
    inorder_list = []
    inOrderTraversalList(root, inorder_list)
    index = inorder_list.index(value)
    if index == len(inorder_list) - 1:
        return "Inorder successor does not exist"
    return "Inorder successor of %d is %d" % (value, inorder_list[index + 1])


print("\ninorder traversal list method with a given value: ")
print(inOrderSuccessor(root, 2))
print(inOrderSuccessor(root, 3))

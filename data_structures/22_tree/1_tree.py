"""
Tree Data Structure

What is a Tree?
A tree is a nonlinear data structure with hierarchical relationships between its elements
without having any cycle. It is basically reversed from a real life tree.

Properties:
- Represent hierarchical data
- Each node has two components: data and a link to its sub category
- Base category and sub category under it


Why a tree?
- Qucker and easier access to the data
- Store hierarchical data, like folder structure, organization structure, XML/HTML data.
    - The file system on a computer
- There are many different types of data structures which performs better in various 
    situations 
    - Binary Search Tree, AVL, Red Black Tree, Trie


Tree Terminology
Root: top node without parent
Edge: a link between parent and child
Parent: a node (excluding a root) connected to every other nodes
Children: arbitrary number of nodes connected to a parent node
External node: a node with no children, also called a leaf
Internal node: a node that is not a leaf
Ancestor: parent, grandparent, great grandparent of a node
Depth of node: the number of edges from the root to the node
Height of node: the number of edges from the node to the deepest leaf
Depth of tree: depth of root node
Height of tree: height of root node
"""
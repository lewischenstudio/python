## Section 23: Tree / Binary Tree

#### Table of Contents
- What is a Tree?
- Why Tree?
- Tree Terminology
- How to create basic tree in Python?
- Binary Tree
- Types of Binary Tree
- Binary Tree Representation
- Create Binary Tree (Linked List)
- PreOrder Traversal Binary Tree (Linked List)
- InOrder Traversal Binary Tree (Linked List)
- PostOrder Traversal Binary Tree (Linked List)
- LevelOrder Traversal Binary Tree (Linked List)
- Searching for a node in Binary Tree (Linked List)
- Inserting a node in Binary Tree (Linked List)
- Delete a node from Binary Tree (Linked List)
- Delete entire Binary Tree (Linked List)
- Create Binary Tree (Python List)
- Insert a value Binary Tree (Python List)
- Search for a node in Binary Tree (Python List)
- PreOrder Traversal Binary Tree (Python List)
- InOrder Traversal Binary Tree (Python List)
- PostOrder Traversal Binary Tree (Python List)
- Level Order Traversal Binary Tree (Python List)
- Delete a node from Binary Tree (Python List)
- Delete Entire Binary Tree (Python List)
- Linked List vs Python List Binary Tree



### What is a Tree
A tree is a nonlinear data structure with hierarchical relationships between its elements without having any cycle. It is basically reversed from a real life tree.
```
                N1
               /   \  
             /       \  
           /           \  
         N2            N3  
        /  \             \ 
      N4    N5            N6
     /        \ 
   N7          N8
```

Properties:
- Represent hierarchical data
- Each node has two components: data and a link to its sub category
- Base category and sub category under it


### Why a tree?
- Qucker and easier access to the data
- Store hierarchical data, like folder structure, organization structure, XML/HTML data.
  - The file system on a computer
- There are many different types of data structures which performs better in various situations 
  - Binary Search Tree, AVL, Red Black Tree, Trie


### Tree Terminology
```
                N1
               /   \  
             /       \  
           /           \  
         N2            N3  
        /  \             \ 
      N4    N5            N6
     /        \ 
   N7          N8
```
- Root: top node without parent
- Edge: a link between parent and child
- Parent: a node (excluding a root) connected to every other nodes
- Children: arbitrary number of nodes connected to a parent node
- External node: a node with no children, also called a leaf
- Internal node: a node that is not a leaf
- Ancestor: parent, grandparent, great grandparent of a node
- Depth of node: the number of edges from the root to the node
- Height of node: the number of edges from the node to the deepest leaf
- Depth of tree: depth of root node
- Height of tree: height of root node


### Linked List vs Python List Binary Tree
|                                  | Python List      | with Capacity    | Linked          | List             |
|----------------------------------|------------------|------------------|-----------------|------------------|
|                                  | Time Complexity  | Space Complexity | Time Complexity | Space Complexity |
| Create Binary Tree               | O(1)             | O(n)             | O(1)            | O(1)             |
| Inset a node to Binary Tree      | O(1)             | O(1)             | O(n)            | O(n)             |
| Delete a node from Binary Tree   | O(n)             | O(1)             | O(1)            | O(n)             |
| Search for a node in Binary Tree | O(n)             | O(1)             | O(1)            | O(n)             |
| Traverse Binary Tree             | O(n)             | O(1)             | O(1)            | O(n)             |
| Delete entire Binary Tree        | O(1)             | O(1)             | O(1)            | O(1)             |
| Space Sufficient                 |                  | No               |                 | Yes              |
"""
What is an AVL Tree?

An AVL tree is a self-balancing Binary Search Tree (BST) where the difference between
heights of left and right subtrees cannot be more than one for all nodes

AVL Tree
                70
              /   \  
            /       \  
          /           \  
         50            90
        /             /  \ 
      /             /      \ 
    30            80       100
   /  \       
 20    40  

For Node 70
Height of leftSubtree = 3
Height of rightSubtree = 2
difference = 1

For Node 90
Height of leftSubtree = 1
Height of rightSubtree = 1
difference = 0

For Node 50
Height of leftSubtree = 2
Height of rightSubtree = 0
difference = 2

If at any time heights of left and right subtrees differ by more than one, then 
balancing is done to restore AVL property, this process is called rotation

Examples

Example 1
                70
              /   \  
            /       \  
          /           \  
         50            90
        / \           /  \ 
      /     \       /      \ 
     30     60     80      100


Example 2
                70
              /   \  
            /       \  
          /           \  
         50            90
        / \           /  \ 
      /     \       /      \ 
     30     60     80      100
    / 
   20

For Node 70
Height of leftSubtree = 3
Height of rightSubtree = 2
difference = 1

For Node 90
Height of leftSubtree = 1
Height of rightSubtree = 1
difference = 0

For Node 50
Height of leftSubtree = 2
Height of rightSubtree = 1
difference = 1

For Node 30
Height of leftSubtree = 1
Height of rightSubtree = 0
difference = 1


Example 3
                70
              /   \  
            /       \  
          /           \  
         50            90
        / \           /  \ 
      /     \       /      \ 
     30     60     80      100
    / 
   20
  /
 10

For Node 70
Height of leftSubtree = 4
Height of rightSubtree = 2
difference = 2

--------------------------------------------------------------------------------

Why do we need AVL Tree?

10, 20, 30, 40, 50, 60, 70 
10
  \ 
   20
    \ 
     30 
      \ 
       40 
        \ 
         50
          \ 
           60 
            \ 
             70 
The search speed is slow for the above tree


                40
              /   \  
            /       \  
          /           \  
         20            60
        / \           /  \ 
      /     \       /      \ 
     10     30     50      70

- Search for 60
- Time complexity is O(LogN)

--------------------------------------------------------------------------------

Common Operations on AVL Trees
- Creation of AVL trees
- Search for a node in AVL trees
- Traverse all nodes in AVL trees 
- Insertion of a node in AVL trees
- Deletion of a node from AVL trees
- Deletion of entire AVL trees

Depth first search
- Preorder traversal:
root node --> left subtree --> right subtree
Time complexity: O(n)
Space complexity: O(n)

- Inorder traversal:
left subtree --> root node --> right subtree
Time complexity: O(n)
Space complexity: O(n)

- Post order traversal:
left subtree --> right subtree --> root node
Time complexity: O(n)
Space complexity: O(n)

- Level order traversal
Time complexity: O(n)
Space complexity: O(n)

- Search for a node in AVL Trees
Time complexity: O(LogN)
Space complexity: O(LogN)
"""
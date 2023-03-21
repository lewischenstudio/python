"""
Binary Tree

- Binary trees are the data structures in which each node has at most two children,
  often referred to as the left and the right children
- Binary tree is a family of data structure (BST, Heap tree, AVL, red black trees, Syntax tree)
- Huffman coding problem, heap priority problem and expression parsing problems can be solved 
  efficiently using binary trees.


Types of Binary Tree
- Full Binary Tree
  - A full Binary tree is a special type of binary tree in which every parent node/internal node 
    has either two or no children. It is also known as a proper binary tree.

               18
           /       \  
         15         30  
        /  \        /  \ 
      40    50    100   40

             18
           /    \   
         15     20    
        /  \       
      40    50   
    /   \ 
   30   50

               18
            /     \  
          40       30  
                   /  \ 
                 100   40

- Complete Binary Tree
  - All the levels are completely filled except possibly the last level and the last level has 
    all keys as left as possible.
  - It is just like a full binary tree with two major differences:
    - Every level must be completely filled
    - All the leaf elements must lean towards the left.
    - The last leaf element might not have a right sibling

               18
           /       \  
         15         30  
        /  \        /  \ 
      40    50    100   40


               18
           /       \  
         15         30  
        /  \        /  \ 
      40    50    100   40
     /  \   /
    8   7  9 

- Perfect Binary Tree
  - Every internal node has exactly two child nodes and all the leaf nodes are at the same level.
  - The number of leaf nodes is the number of internal nodes plus 1.
  - A Perfect Binary Tree of height h (where the height of the binary tree is the number of edges 
    in the longest path from the root node to any leaf node in the tree, height of root node is 0) 
    has 2^(h+1) - 1 node. 
  - An example of a Perfect binary tree is ancestors in the family. Keep a person at root, parents 
    as children, parents of parents as their children. 

               18
           /       \  
         15         30  
        /  \        /  \ 
      40    50    100   40


               18
           /       \  
         15         30  

- Balanced Binary Tree
  - A binary tree is balanced if the height of the tree is O(Log n) where n is the number of nodes. 
  - For Example, the AVL tree maintains O(Log n) height by making sure that the difference between 
    the heights of the left and right subtrees is at most 1. 
  - Red-Black trees maintain O(Log n) height by making sure that the number of Black nodes on every 
    root to leaf paths is the same and there are no adjacent red nodes.
  - Balanced Binary Search trees are performance-wise good as they provide O(log n) time for search, insert and delete. 
  - It is a type of binary tree in which the difference between the height of the left and the right subtree for each 
    node is either 0 or 1. In the figure above, the root node having a value 0 is unbalanced with a depth of 2 units.

            18
        /    \   
        15     20    
    /  \       
    40    50   


Binary Tree
- Linked List
- Python List (array)

Linked List
                                222|Drinks|333
                                    /       \ 
                                /               \ 
                            /                       \ 
                444|Hot|555                         666|Cold|777
                    /  \                                /  \ 
                  /      \                            /      \ 
                /          \                        /          \ 
              /              \                    /              \ 
      null|Tea|null    null|Coffee|null    null|Cola|null   null|Fanta|null


Python List
                       Drinks
                    /          \ 
                 /                \  
              /                     \  
            Hot                     Cold 
           /  \                     /  \ 
         /      \                 /      \ 
      Tea     Coffee    Non alcoholic   Alcoholic

Index:  0       1           2       3       4      5       6               7  
Item:   Null    Drinks      Hot     Cold    Tea    Cofee   Non acoholic    Acoholic

x = 0                       ---->       cell[1] = Drinks

x = 1
Left child = cell[2x]       ---->       index = 2x1 = 2     ---->   cell[2] = Hot
Right child = cell[2x+1]    ---->       index = 2x1+1 = 3   ---->   cell[3] = Cold

x = 2
Left child = cell[2x]       ---->       index = 2x2 = 4     ---->   cell[4] = Tea
Right child = cell[2x+1]    ---->       index = 2x2+1 = 5   ---->   cell[5] = Coffee

x = 3
Left child = cell[2x]       ---->       index = 2x3 = 6     ---->   cell[6] = Non acoholic
Right child = cell[2x+1]    ---->       index = 2x3+1 = 7   ---->   cell[7] = Acoholic

"""
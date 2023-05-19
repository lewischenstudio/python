## Section 23: Binary Search Tree

#### Table of Contents
- What is a Binary Search Tree? Why do we need it?
- Create a Binary Search Tree
- Insert a node to BST
- Traverse BST
- Search in BST
- Delete a node from BST
- Delete entire BST
- Time and Space complexity of BST



### What is a Binary Search Tree
- In the left subtree the value of a node is less than or equal to its parent node's value.
- In the right subtree the value of a node is greater than its parent's node value


#### Binary Search Tree
```
                70
              /   \  
            /       \  
          /           \  
         50            90
        /  \          /  \ 
      /      \      /      \ 
    30        60   80       100
   /  \      / 
 20    40  
```


#### Why Binary Search Tree?
- It performs faster than Binary Tree when inserting and deleting nodes

--------------------------------------------------------------------------------

#### Common Operations on Binary Search Tree
- Creation of Tree
- Insertion of a node
- Deletion of a node
- Search for a value
- Traverse all nodes
- Deletion of tree


### Time and Space complexity of BST
|                       | Time Complexity | Space Complexity |
|-----------------------|-----------------|------------------|
| Create BST            | O(1)            | O(1)             |
| Insert a node BST     | O(logN)         | O(logN)          |
| Traverse BST          | O(N)            | O(N)             |
| Search for a node BST | O(logN)         | O(logN)          |
| Delete node from BST  | O(logN)         | O(logN)          |
| Delete entire BST     | O(1)            | O(1)             |
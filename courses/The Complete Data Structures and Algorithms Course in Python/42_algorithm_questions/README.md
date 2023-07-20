## Section 42: Cracking Trees and Graphs Top Interview Questions

#### Table of Contents
- Question 1: Route Between Nodes
- Question 2: Minimal Tree
- Question 3: List of Depths
- Question 4: Check Balanced - LeetCode 110
- Question 5: Validate BST - LeetCode 98
- Question 6: In-order Successor in BST - LeetCode 285
- Question 7: Build Order
- Question 8: First Common Ancestor - LeetCode 236


### Question 1: Route Between Nodes

Given a directed graph and two nodes (S and E), design an algorithm to find
out whether there is a route from S to E.

#### Pseudocode
- Create function with two parameters start and end nodes
- Create queue and enqueue start node to it
- Find all the neighbors of the just enqueued node and enqueue them into the queue
- Repeat this process until the end of the elements in graph
- If we encounter the destination node during the above process, we return True
- Mark visited nodes as visited

![Route Between Nodes](https://github.com/lcycstudio/python/tree/master/data_structures/42_interview_questions/1_RouteBetweenNodes.png)



### Question 2: Minimal Tree

Given a sorted (increasing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.

#### Approach
Recursively add value to the binary search tree node class using the left subtree and right subtree.



### Question 3: List of Depths

Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth (ie , if you have a tree with depth D, you’ll have D linked lists)

![List of Depths](https://github.com/lcycstudio/python/tree/master/data_structures/42_interview_questions/3_ListofDepth.png)



### Question 4: Check Balanced - LeetCode 110

Implement a function to check if a binary tree is balanced. For the purposes
of this question, a balanced tree is defined to be a tree such that the
heights of the two subtrees of any node never differ by more than one.

The Binary Tree is Balanced if
- The right subtree is balanced
- The left subtree is balanced
- The difference between the height of the left subtree and the right
subtree is at most 1


### Question 5: Validate BST - LeetCode 98
Implement a function to check if a binary tree is a Binary Search Tree.


### Question 6: In-order Successor in BST - LeetCode 285
Write an algorithm to find the next node (i.e in-order successor) of given node in a binary search tree. You may assume that each node has a link to its parent.

![In-order Successor in BST](https://github.com/lcycstudio/python/tree/master/data_structures/42_interview_questions/6_Successor.png)



### Question 7: Build Order

You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.


### Question 8: First Common Ancestor - LeetCode 236

Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.

![In-order Successor in BST](https://github.com/lcycstudio/python/tree/master/data_structures/42_interview_questions/8_FirstCommonAncestor.png)

## Section 33: Graph Traversal - Breadth First Search and Depth First Search

#### Table of Contents
- Graph traversal - BFS
- BFS Traversal in Python
- Graph Traversal - DFS
- DFS Traversal in Python
- BFS Traversal vs DFS Traversal


### Graph traversal - BFS

Graph Traversal is a process of visiting all vertices in a given Graph.
- Breadth First Search
- Depth First Search

#### Breadth First Search (BFS) 
BFS is an algorithm for traversing Graph data structure.
It starts at some arbitrary node of a graph and explores the neighbor nodes
(which are at current level) first, before moving to the next level neighbors.


#### Breadth First Search Algorithm

BFS Algorithm with Queue
```
enqueue any starting vertex
while queue is not empty
  p = dequeue()
  if p is unvisited
    mark it visited
    enqueue all adjacent unvisited vertices of p
```
```
A -- B
|\   |\
| \  | \
|  \ |  \
C -- D   G
|    |  /
|    | /
|    |/
E -- F
```
Order: A B C D G E F

Queue [A, B, C, D, G, E, F, F, F ]


### Graph Traversal - DFS

#### Depth First Search (DFS)

DFS is an algorithm for traversing a graph data structure which starts selecting
some arbitrary node and explores as far as possible along each edge before
backtracking.

#### Depth First Search Algorithm

DFS Algorithm with Stack
```
push any startingg vertex
while stack is not empty
  p = pop()
  if p is unvisited
    mark it visited
    push all adjacent unvisited vertices of p
```
```
A -- B
|\   |\
| \  | \
|  \ |  \
C -- D   G
|    |  /
|    | /
|    |/
E -- F
```
Order: A C E F D B G

Stack
G B D G F E D C B A 


### BFS Traversal vs DFS Traversal
```
Level 1   A -- B
          |\   |\
          | \  | \
          |  \ |  \
Level 2   C -- D   G
          |    |  /
          |    | /
          |    |/
Level 3   E -- F
```
BFS Order: A B C D G E F

DFS Order: A C E F D B G

|                                  | **BFS**                                    | **DFS**                               |
|----------------------------------|--------------------------------------------|---------------------------------------|
| How does it work internally?     | It goes in breadth first                   | It goes in depth first                |
| Which DS does it use internally? | Queue                                      | Stack                                 |
| Time Complexity                  | O(V+E)                                     | O(V+E)                                |
| Space Complexity                 | O(V+E)                                     | O(V+E)                                |
| When to use?                     | The target is close to  the starting point | The target vertex is buried very deep |

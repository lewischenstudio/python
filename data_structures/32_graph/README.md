## Section 32: Graph Algorithms

#### Table of Contents
- What is a Graph? Why Graph?
- Graph Terminology
- Types of Graph
- Graph Representation
- Create a graph using Python
- Create Graph using Python - Add Vertex
- Add Edge
- Remove Edge
- Remove Vertex

### What is a Graph? Why Graph?
A graph consists of a finite set of verticies (or nodes) and a set of edges 
which connect a pair of nodes. We use graph structure to solve the shortest path problem.


### Graph Terminology
- Verticies (vertex): verticies are the nodes of the graph
- Edge: the edge is the line that connects pairs of vertices
- Unweighted graph: a graph which does not have a weight associated with any edge
- Weighted graph: a graph which has a weight associated with any edge
- Undirected graph: in case of the edges of the graph do not have a direction associated with them
- Directed graph: if the edges in a graph have a direction associated with them
- Cyclic graph: a graph which has at least one loop
- Acyclic graph: a graph without a loop
- Tree: it is a special case of directed acyclic graphs
```
V1 ------------ V3
| \               \
|   \               \
|     \              V5
|       \          / 
|         \      /  
|           \  /
V2 --------- V4
```

### Types of Graph
6 types of graphs
- Unweighted, undirected
- Unweighted, directed
- Positive, weighted, undirected
- Positive, weighted, directed
- Negative, weighted, undirected
- Negative, weighted, directed

### Graph Representation

```
A ------------- B
| \              \
|   \              \
|     \              E
|       \           / 
|         \       /  
|           \   /
C ----------- D
```

**Adjacency Matrix**: an adjacency matrix is a square matrix or a 2D array. The elements of the matrix indicate whether pairs of vertices are adjacent or not in the graph.


**Adjacency Matrix**
|       | **A** | **B** | **C** | **D** | **E** |
|-------|-------|-------|-------|-------|-------|
| **A** | 0     | 1     | 1     | 1     | 0     |
| **B** | 1     | 0     | 0     | 0     | 1     |
| **C** | 1     | 0     | 0     | 1     | 0     |
| **D** | 1     | 0     | 1     | 0     | 1     |
| **E** | 0     | 1     | 0     | 1     | 0     |


**Adjacency List**: an adjacency list is a collection of unordered list used to represent a graph. 
Each list describes the set of neighbors of a vertex in the graph.
We are storing the vertices in the array and the edges in the **linked list**.
```
A  -->  B  -->  C  -->  D 
B  -->  A  -->  E         
C  -->  A  -->  D         
D  -->  A  -->  C  -->  E 
E  -->  B  -->  D         
```

#### Which one to use?
- If a graph is complete or almost complete, we should use **Adjacency Matrix**.
- If the number of edges are few, then we should use **Adjacency List**.

#### Python Dictionary Implementation
```python
{
  A: [B, C, D],
  B: [A, E],
  C: [A, D],
  D: [A, C, E],
  E: [B, D]
}
```


### Create a graph using Python
```
   A
  / \
 /   \
B     C
| \   |
|  \  |  
|   \ |  
|    \|  
D     E 
 \   /
  \ /
   F
```
```python
{
  A: [B, C],
  B: [A, D, E],
  C: [A, E],
  D: [B, E, F],
  E: [B, C, D, F],
  F: [D, E]
}
```

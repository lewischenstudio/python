## Section 37: Graph Algorithms - Bellman Ford Algorithm

#### Table of Contents
- Bellman Ford Algorithm
- Bellman Ford Algorithm with negative cycle
- Why Bellman Ford runs V-1 times?
- Bellman Ford in Python
- BFS vs Dijkstra vs Bellman Ford

### Bellman Ford Algorithm

Single Source Shortest Path Algorithm

| **Graph Type**                 | **BFS** | **Dijkstra** | **Bellman Ford** |
|--------------------------------|---------|--------------|------------------|
| Unweighted, undirected         | OK      | OK           | OK               |
| Unweighted, directed           | OK      | OK           | OK               |
| Positive, weighted, undirected | X       | OK           | OK               |
| Positive, weighted, directed   | X       | OK           | OK               |
| Negative, weighted, undirected | X       | OK           | OK               |
| Negative, weighted, directed   | X       | OK           | OK               |
| Negative Cycle                 | X       | X            | OK               |

Bellman Ford algorithm is used to solve the single source shortest path problem.
If there is a negative cycle, it catches and reports its existence.

```
   inf    3   inf
   A  <------ B
   | \        |\
   |  \       | \ 4
   |    \     |  \ 
6  |    6\   1|   E 0
   |      \   |  /
   |        \ | / 2
   |     1   \|/
   C  ------> D
  inf <----- inf
         2
```

#### Bellman Ford Algorithm
If the distance of destination vertex is greater than distance of source vertex + weight
between source and destination, then update distance of destination vertex to distance
of source vertex + weight between source and destination vertex.


| **Edge** | **Weight** |
|----------|------------|
| A --> C  | 6          |
| A --> D  | 6          |
| B --> A  | 3          |
| C --> D  | 1          |
| D --> C  | 2          |
| D --> B  | 1          |
| E --> B  | 4          |
| E --> D  | 2          |


**Distance Matrix Iterations**
|        |          | Iteration | 1      | Iteration | 2      | Iteration | 3      | Iteration | 4      |
|--------|----------|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|
| Vertex | Distance | Distance  | Parent | Distance  | Parent | Distance  | Parent | Distance  | Parent |
| A      | inf      | inf       | -      | 4+3=7     | B      | 3+3=6     | B      | 6         | B      |
| B      | inf      | 4         | E      | 2+1=3     | D      | 3         | D      | 3         | D      |
| C      | inf      | inf       | -      | 2+2=4     | D      | 4         | D      | 4         | D      |
| D      | inf      | 2         | E      | 2         | E      | 2         | E      | 2         | E      |
| E      | 0        | 0         | -      | 0         | -      | 0         | -      | 0         | -      |


**Final Solution**
| Vertex | Distance from E | Path from E      |
|--------|-----------------|------------------|
| A      | 6               | E -> D -> B -> A |
| B      | 3               | E -> D -> B      |
| C      | 4               | E -> D -> C      |
| D      | 2               | E -> D           |
| E      | 0               | 0                |


### Bellman Ford Algorithm with negative cycle

```
   inf    3   inf
   A  <------ B
   | \        |\
   |  \       | \ 4
   |    \     |  \ 
6  |   -6\   1|   E 0
   |      \   |  /
   |        \ | / 2
   |     1   \|/
   C  ------> D
  inf <----- inf
         2
```


| **Edge** | **Weight** |
|----------|------------|
| A --> C  | 6          |
| A --> D  | -6         |
| B --> A  | 3          |
| C --> D  | 1          |
| D --> C  | 2          |
| D --> B  | 1          |
| E --> B  | 4          |
| E --> D  | 2          |


**Distance Matrix Iterations**
|        |          | Iteration | 1      | Iteration | 2      | Iteration | 3      | Iteration | 4      | Iteration | 5      |
|--------|----------|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|
| Vertex | Distance | Distance  | Parent | Distance  | Parent | Distance  | Parent | Distance  | Parent |Distance | Parent |
| A      | inf      | inf       | -      | 4+3=7     | B      | 3+3=6     | B      | 6         | B      |6        | B      |
| B      | inf      | 4         | E      | 2+1=3     | D      | 3         | D      | 3         | D      |0        | D      |
| C      | inf      | inf       | -      | 2+2=4     | D      | 4         | D      | 4         | D      |0        | D      |
| D      | inf      | 2         | E      | 2         | E      | 7+(-6)=1  | A      | 6+(-6)=0  | A      |1        | A      |
| E      | 0        | 0         | -      | 0         | -      | 0         | -      | 0         | -      |-        | -      |


**Final Solution**
| Vertex | Distance from E | Path from E      |
|--------|-----------------|------------------|
| A      | 6               | E -> D -> B -> A |
| B      | 3               | E -> D -> B      |
| C      | 4               | E -> D -> C      |
| D      | 2               | E -> D           |
| E      | 0               | 0                |


### Why Bellman Ford runs V-1 times?
- If any node is achieved better distance in previous iteration, then the better distance
is used to improve distance of other vertices
- Identify worst case graph that can be given to us


### BFS vs Dijkstra vs Bellman Ford

| **Graph Type**                 | **BFS** | **Dijkstra** | **Bellman Ford** |
|--------------------------------|---------|--------------|------------------|
| Unweighted, undirected         | OK      | OK           | OK               |
| Unweighted, directed           | OK      | OK           | OK               |
| Positive, weighted, undirected | X       | OK           | OK               |
| Positive, weighted, directed   | X       | OK           | OK               |
| Negative, weighted, undirected | X       | OK           | OK               |
| Negative, weighted, directed   | X       | OK           | OK               |
| Negative Cycle                 | X       | X            | OK               |

|                  |                            **BFS**                           |                   **Dijkstra**                  |                **Bell Ford**                |
|------------------|:------------------------------------------------------------:|:-----------------------------------------------:|:-------------------------------------------:|
| Time complexity  | O(V^2)                                                       | O(V^2)                                          | O(VE)                                       |
| Space complexity | O(E)                                                         | O(V)                                            | O(V)                                        |
| Implementation   | Easy                                                         | Moderate                                        | Moderate                                    |
| Limitation       | Not work for weighted graph                                  | Not work for negative cycle                     | N/A                                         |
| Unweighted graph | Use it because time complexity is good and easy to implement | Don't use it because implementation is not easy | Don't use it because time complexity is bad |
| Weighted         | X                                                            | OK                                              | OK                                          |
| graph            | Not Supported                                                | Use it because time complexity is good          | Don't use it because time complexity is bad |
| Negative         | X                                                            | X                                               | OK                                          |
| Cycle            | Not supported                                                | Not supported                                   | Use this because others don't support       |
|                  |                                                              |                                                 |                                             |
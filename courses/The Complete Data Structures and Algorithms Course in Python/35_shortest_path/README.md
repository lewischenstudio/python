## Section 35: Single Source Shortest Path

#### Table of Contents
- Single Source Shortest Path Problem (SSSPP)
- BFS for SSSPP
- BFS for SSSPP in Python
- Why does BFS not work with weighted Graph?
- Why does DFS not work for SSSP?


### Single Source Shortest Path Problem (SSSPP)

A single source problem is about finding a path between a given vertex (called
source) to all other vertices in a graph such that the total distance between
them (source and destination) is minimum.

#### The problem
- Five offices in different cities
- Travel costs between these cities are known
- Find the cheapest way from head office to branches in different cities

#### Single Source Shortest Path Problem (SSSPP)
- BFS
- Dijkstra's Algorithm
- Bellman Ford
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


### BFS for SSSP
BFS
```
enqueue any starting vertex
while queue is not empty
  p = dequeue()
  if p is unvisited:
    mark it visited
    enqueue all adjacent unvisited vertices of p
    update parent of adjacent vertices to currentVertex
```

Order: A B C D G E F

Queue: A B C D G E F F F



### Why does BFS not work with weighted Graph?

| **Graph Type**                 | **BFS** |
|--------------------------------|---------|
| Unweighted, undirected         | OK      |
| Unweighted, directed           | OK      |
| Positive, weighted, undirected | X       |
| Positive, weighted, directed   | X       |
| Negative, weighted, undirected | X       |
| Negative, weighted, directed   | X       |

![Why does BFS not work with weighted Graph](https://github.com/lcycstudio/python/blob/master/data_structures/35_shortest_path/bfs_not_work.png)


### Why does DFS not work for SSSP?

DFS has the tendency to go "as far as possible" from the source, so it can never
find the shortest path.

![Why does DFS not work for SSSP](https://github.com/lcycstudio/python/blob/master/data_structures/35_shortest_path/dfs_not_work.png)



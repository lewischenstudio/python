## Section 38: All Pairs Shortest Path

#### Table of Contents
- All pairs shortest path problem
- Dry run for all pairs shortest path problem


### All pairs shortest path problem

All pairs shortest path problem is about finding a path between **every vertex** to all other
vertices in a graph such that the total distance between them (source and destination) is
minimum.

#### The problem
- Five offices in different cities
- Travel costs between these cities are known
- Find the cheapest way to reach each office from **every other office**

Run BFS, Dijkstra's or Bellman Ford algorithms V times, where V is the number of vertices,
for all pairs shortest path problems.


### Dry run for all pairs shortest path problem

```
         3   
   A  <------ B
   | \        |\
   |  \       | \ 4
   |    \     |  \ 
6  |    6\   1|   E 0
   |      \   |  /
   |        \ | / 2
   |     1   \|/
   C  ------> D
      <----- 
         2
```

**Run Bellman Ford algorithm five times**

| **Source Vertex E** | **Path**   |
|---------------------|------------|
| A                   | E->D->B->A |
| B                   | E->D->B    |
| C                   | E->D->C    |
| D                   | E->D       |
| E                   | -          |

| **Source Vertex D** | **Path**   |
|---------------------|------------|
| A                   | D->B->A    |
| B                   | D->B       |
| C                   | D->C       |
| D                   | -          |
| E                   | N/A        |

| **Source Vertex C** | **Path**   |
|---------------------|------------|
| A                   | C->D->B->A |
| B                   | C->D->B    |
| C                   | E->D->C    |
| D                   | C->D       |
| E                   | N/A        |


| **Source Vertex B** | **Path**   |
|---------------------|------------|
| A                   | B->A       |
| B                   | -          |
| C                   | B->A->C    |
| D                   | A->D       |
| E                   | N/A        |


| **Source Vertex A** | **Path**   |
|---------------------|------------|
| A                   | A          |
| B                   | A->D->B    |
| C                   | A->D->C    |
| D                   | A->D       |
| E                   | N/A        |

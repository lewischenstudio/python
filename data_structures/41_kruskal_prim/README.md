## Section 41: Graph Algorithms - Kruskal and Prim's Algorithms

#### Table of Contents
- Kruskal Algorithm
- Kruskal Algorithm in Python
- Prim's Algorithm
- Prim's Algorithm in Python
- Prim's vs Kruskal


### Kruskal Algorithm

It is a greedy algorithm. It finds a minimum spanning tree for weighted undirected
graphs in two ways:
- adding increasing cost edges at each step
- avoid any cycle at each step

```
              5
       A ----------- B
     / |            /|
15 /   |          /  |
 /     |         /   |
E   13 |    10 /     | 8
 \     |     /       |
20 \   |   /         |
     \ | /           |
       C ----------- D
              6
```

```
              5
       A ----------- B
     /               |
15 /                 |
 /                   |
E                    | 8
                     |
                     |
                     |
       C ----------- D
              6
```

#### Kruska's Algorithm Pseudocode
```python
Kruskal(G)
for each vertex: # O(v)
    makeSet(v)
sort each edge in non decreasing order by weight # O(ElogE)
for each edge (u, v): # O(e)
    if findSet(u) != findSet(v):
        union(u, v) # O(v)
        cost = cost + edge(u, v)
```

#### Steps
- Initialize vertices = A B C D E, cost = 0, set = []
- Edge AB = 5, cost = 0 + 5, union = (A, B)
- Edge CD = 6, cost = 0 + 5 + 6, union = (C, D)
- Edge BD = 8, cost = 0 + 5 + 6 + 8, union = (A,B,C,D)
- Edge BC = 10 and AC = 13 cause a cycle, ignore them
- Edge AE = 15, cost = 0 + 5 + 6 + 8 + 15 = 34, union = (A,B,C,D,E)


Time complexity: O(V + ElogE + EV) = O(ElogE) \
Space complexity: O(V+E)


### Prim's Algorithm

It is a greedy algorithm. It finds minimum spanning tree for weighted undirected
graphs in the following way:
- Take any vertex as a source and set its weight to 0 and all other vertices' weights to inifinty
- For every adjacent vertices, if the current weight is more than the current edge,
then we set it to current edge
- Then we mark current vertex as visited
- Repeat these steps for all vertices in increasing order of weight

```
       10      5       5
       B - - - - - - - D
     / |             / |
10 /   |           /   |
 /     |         /     |
A   30 |    15 /     8 |
 \     |     /         | 
20 \   |   /           | 
     \ | /             | 
       C - - - - - - - E
               6
```
```
     10              5
     B - - - - - - - D
    /                |
   /                 |
0 /                  |
A                    |
                     | 
                     | 
                     | 
     C - - - - - - - E
     6               8
```


### Prim's vs Kruskal

#### Kruskal
- Focuses on edges
- Finalize edge in each iteration

#### Prim's
- Focuses on vertices
- Finalize vertex in each iteration

#### Kruskal Application
- Landing cables
- TV network
- Tour operations
- LAN networks
- A network of pipes of drinking water or natural gas
- An electric grid
- Single-link cluster


### Prim's Applications
- Network for roads and Rail tracks connecting all the cities
- Irrigation channels and placing microwave towers
- Designing a fiber-optic grid or ICs
- Traveling salesman problem
- Cluster analysis
- Pathhfinding algorithms used in Artificial Intelligence
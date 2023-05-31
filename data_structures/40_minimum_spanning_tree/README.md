## Section 40: Minimum Spanning Tree (Disjoint Set)

#### Table of Contents
- Minimum Spanning Tree
- Disjoint Set
- Disjoint Set in Python


### Minimum Spanning Tree

A Minimum Spanning Tree (MST) is a subset of the edges of connected, weighted and 
undirected graph which connects all vertices together, has no cycle and has a 
minimum total edge.


#### Reat life problem
- Connect five island with bridges
- The cost of bridges between island varies based on different factors
- Which bridge should be constructed so that all islands are accessible and 
the cost is minimum

![Minimum Spanning Tree](https://github.com/lcycstudio/python/blob/master/data_structures/40_minimum_spanning_tree/mst.png)


### Disjoint Set

It is a data structure that keeps track of set of elements which are partitioned
into a number of disjoint and non overlapping sets and each sets have representative
which helps in identifying that sets. There are three standard operations:
- Make Set
- Union
- Find Set

### Standard Operations

makeSet(N): used to create initial set
union(x, y): merge two given sets
findSet(x): returns the set name in which this element is there



### Disjoint Set in Python
## Section 39: Gralph Algorithms - Floyd Warshall Algorithm

#### Table of Contents
- Floyd Warshall Algorithm
- Why Floyd Warshall?
- Floyd Warshall with negative cycle
- Floyd Warshall in Python
- BFS vs Dijkstra vs Bellman Ford vs Floyd Warshall


### Floyd Warshall Algorithm
```
     8
  A ---> B
  |\    /|
  | \4 / |
1 |  \/  | 1
  |  /\  |
  | /2 \ |
  |/    \|
  D ---> C
     9
```

A -> B \
A -> D \
B -> C \
C -> A \
D -> C 

**Given**
|   | **A** | **B** | **C** | **D** |
|---|-------|-------|-------|-------|
| A | 0     | 8     | inf   | 1     |
| B | inf   | 0     | 1     | inf   |
| C | 4     | inf   | 0     | inf   |
| D | inf   | 2     | 9     | 0     |


```
If D[u][v] > D[u][viaX] + D[viaX][v]:
   D[u][v] = D[u][viaX] + D[viaX][v]
```

**C -> B**
```
If D[C][B] > D[C][A] + D[A][B]:
   D[C][B] = D[C][A] + D[A][B]
```

**C -> D**
```
If D[C][D] > D[C][A] + D[A][D]:
   D[C][D] = D[C][A] + D[A][D]
```

**Iteration 1**
|**via A**   | **A** | **B** | **C** | **D** |
|---|-------|-------|-------|-------|
| A | 0     | 8     | inf   | 1     |
| B | inf   | 0     | 1     | inf   |
| C | 4     | 4+8=12| 0     | 4+1=5 |
| D | inf   | 2     | 9     | 0     |

**Iteration 1**
|**via A**   | **A** | **B** | **C** | **D** |
|---|-------|-------|-------|-------|
| A | 0     | 8     | inf   | 1     |
| B | inf   | 0     | 1     | inf   |
| C | 4     | 4+8=12| 0     | 4+1=5 |
| D | inf   | 2     | 9     | 0     |

**Iteration 2**
|**via A**   | **A** | **B** | **C** | **D** |
|---|-------|-------|-------|-------|
| A | 0     | 8     | 8+1=9 | 1     |
| B | inf   | 0     | 1     | inf   |
| C | 4     | 12    | 0     | 5     |
| D | inf   | 2     | 2+1=3 | 0     |

**Iteration 3**
|**via A**   | **A** | **B** | **C** | **D** |
|---|-------|-------|-------|-------|
| A | 0     | 8     | 9     | 1     |
| B | 1+4=5 | 0     | 1     | 1+4+1=5|
| C | 4     | 12    | 0     | 5     |
| D | 3+4=7 | 2     | 3     | 0     |

**Iteration 4**
|**via A**   | **A** | **B** | **C** | **D** |
|---|-------|-------|-------|-------|
| A | 0     | 1+2=3 | 3+1=4 | 1     |
| B | 5     | 0     | 1     | 6     |
| C | 4     | 5+2=7 | 0     | 5     |
| D | 7     | 2     | 3     | 0     |

**Final Answer**
|   | **A** | **B** | **C** | **D** |
|---|-------|-------|-------|-------|
| A | 0     | 3     | 4     | 1     |
| B | 5     | 0     | 1     | 6     |
| C | 4     | 7     | 0     | 5     |
| D | 7     | 2     | 3     | 0     |



### Why Floyd Warshall?
- The vertex is not reachable
- Two vertices are directly connected
  - This is the best solution
  - It can be improved via other vertex
- Two vertices are connected via other vertex


### Floyd Warshall with negative cycle

To go through cycle, we need to go via negative cycle participating vertex at least
twice. FW never runs loop twice via same vertex, so FW can never detect a negative cycle.


### BFS vs Dijkstra vs Bellman Ford vs Floyd Warshall

| **Graph Type**                 | **BFS** | **Dijstra** | **Bellman Ford** | **Floyd Warshall** |
|--------------------------------|:-------:|:-----------:|:----------------:|:------------------:|
| unweighted, undirected         | OK      | OK          | OK               | OK                 |
| Unweighted, directed           | OK      | OK          | OK               | OK                 |
| Positive, weighted, undirected | X       | OK          | OK               | OK                 |
| Positive, weighted, directed   | X       | OK          | OK               | OK                 |
| Negative, weighted, undirected | X       | OK          | OK               | OK                 |
| Negative, weighted, directed   | X       | OK          | OK               | OK                 |
| Negative Cycle                 | X       | X           | OK               | X                  |


|                  |         **BFS**        |      **Dijkstra**      | **Bellman Ford** |   **Floyd Warshall**   |
|------------------|:----------------------:|:----------------------:|:----------------:|:----------------------:|
| Time complexity  | O(V^3)                 | O(V^3)                 | O(EV^2)          | O(V^3)                 |
| Space complexity | O(EV)                  | O(EV)                  | O(V^2)           | O(V^2)                 |
| Implementation   | Easy                   | Moderate               | Moderate         | Moderate               |
| Limitation       | Not for weighted graph | Not for negative cycle | N/A              | Not for negative cycle |
| Unweighted graph | OK                     | OK                     | OK               | OK                     |
| Unweighted graph | Use                    | Don't use              | Don't use        | Can be used            |
| Weighted graph   | X                      | OK                     | OK               | Ok                     |
| Weighted graph   | Not supported          | Can be used            | Don't use        | Can be used            |
| Negative cycle   | X                      | X                      | OK               | X                      |
|                  | Not supported          | Not supported          | Use              | Not supported          |
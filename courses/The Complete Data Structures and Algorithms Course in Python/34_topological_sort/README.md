## Section 34: Topological Sort Algorithm

#### Table of Contents
- Topological Sort
- Topological Sort Algorithm
- Topological Sort in Pythont
- Download Resources


### Topological Sort

**Topological Sort** is a sorting algorithm that sorts actions in such a way that
if there is a dependency of one action on another, then the dependent action
always comes later than its parent action.

```
Exercise        Buy breakfast fruits
  |                     |
  |                     |
Bath            Prepare breakfast
  |            /        |
  |          /          |
  |        /            |
  |      /              |
Breakfast       Wash dishes
  |
  |
Work
```
**Question**: if all these actions are given and how we will identify order of actions?

**Answer**: Topological Sort. It will identify the dependencies between these actions, 
and we will start from the parent and continue to the children. There might be a 
different order of actions from the topological sort, but the dependencies will 
never be violated.



### Topological Sort Algorithm
```
A    B
|  / |
| /  |
C    D
|    |
|    |
E    |
| \  |
|  \ |
H    F --- G
```
A has children C
B has children C and D
C has children E
D has children F
E has children H and F
F has children G

#### Possible orders
- A B C D E H F G
- B A C D E H F G

```
if a vertex depends on currentVertex:
  go to that vertex and then come back to currentVertex
else
  push currentVertex to Stack
```

#### Stack
B D A C E F G H
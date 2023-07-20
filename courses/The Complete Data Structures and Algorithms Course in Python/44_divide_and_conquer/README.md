## Section 44: Divide and Conquer Algorithms

#### Table of Contents
- What is a Divide and Conquer Algorithm?
- Common Divide and Conquer algorithms
- How to solve Fibonacci series using Divide and Conquer approach?
- Number Factor
- Number Factor in Python
- House Robber
- House Robber Problem in Python
- Convert one string to another
- Convert One String to another in Python
- Zero One Knapsack problem
- Zero One Knapsack problem in Python
- Longest Common Sequence Problem
- Longest Common Subsequence in Python
- Longest Palindromic Subsequence Problem
- Longest Palindromic Subsequence in Python
- Minimum cost to reach the Last cell problem
- Minimum Cost to reach the Last Cell in 2D array using Python
- Number of Ways to reach the Last Cell with given Cost
- Number of Ways to reach the Last Cell with given Cost in Python


### What is a Divide and Conquer Algorithm?

Divide and conquer is an algorithm design paradigm which works by recursively breaking down
a problem into subproblems of similar type, until these become simple enough to be solved
directly. The solutions to the subproblems are then combined to give a solution to the 
original problem.

**Example: Developing a website**

```
                          Problem
                          /    \
                      /           \
                  /                   \
              /                           \
    Sub problem                            Sub problem
      /    \                                 /      \
    /        \                             /          \
subproblem subproblem               subproblem      subproblem
    \          /                           \          /
      \      /                               \      /
solution to sub problem                 solution to sub problem
              \                           /
                  \                     /
                      \              /
                      Solution to Probelm
```

#### Optimal Substructure
If any problem's overall optimal solution can be constructed from the optimal solutions
of its subproblem, then this problem has optimal substructure

Example: Fib(n) = Fib(n-1) + Fib(n-2)

#### Why we need it?

It is very effective when the problem has optimal structure property.


### Common Divide and Conquer algorithms

- Merge Sort
- Quick Sort


### How to solve Fibonacci series using Divide and Conquer approach?

**Definition**: a series of numbers in which each number is the sum of the two
preceding numbers. First two numbers by definition are 0 and 1.

**Example**: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

Fibonacci(N) = Fibonacci(N-1) + Fibonacci(N-2)

#### Pseudocode
```
Fibonacci(N):
  If n < 1 return error message
  If n = 1 return 0
  If n = 2 return 1
  Else
    return Fibonacci(N-1) + Fibonacci(N-2)
```


### Number Factor

#### Problem Statement
Given N, find the number of ways to express N as a sum of 1, 3, and 4.

**Example 1**
- N = 4
- Number of ways = 4
- Explanation: {4}, {1,3}, {3,1}, {1,1,1,1}

**Example 2**
- N = 5
- Number of ways = 6
- Explanation: {4,1}, {1,4}, {1,3,1}, {3,1,1}, {1,1,3}, {1,1,1,1,1,1}

f(4): {4}, {1,3}, {3,1}, {1,1,1,1}

f(4) + 1: {4,1}, {1,4}, {1,3,1}, {3,1,1}, {1,1,1,1,1,1}

f(2) + 3: {1,1}, {1,1,3}

f(1) + 4: {1}, {1,4}

```
                                      NumberFactor(6)
                                      /     |       \
                                    /       |         \ 
                                  /         |           \               
                                /           |             \             
                              /             |               \
                NumberFactor(5)       NumberFactor(3)       Numberfactor(2)
               /       |       \
             /         |         \
           /           |           \ 
         /             |             \
NumberFactor(4)  NumberFactor(2)  NumberFactor(1)
```

#### Pseudocode
```
NumberFactor(N):
  If N in (0,1,2) return 1
  If N = 3 return 2
  Else
    return NumberFactor(N-1) + NumberFactor(N-3) + NumberFactor(N-4)
```
### House Robber

#### Problem Statement
- Given N number of houses along the street with some amount of money
- Adjacent houses cannot be stolen
- Find the maximum amount that can be stolen

**Example 1**
6, 7, 1, 30, 8, 2, 4

**Answer**
- Maximum amount = 41
- Houses that are stolen: 7, 30, 4

Option 1 = 6 + f(5) \
Option 2 = 0 + f(0) \
Max(Option1, Option2)

```
                                    maxValueHouse(0)
                                    /            \
                                  /                \ 
                                /                    \               
                              /                        \             
                            /                            \
            maxValueHouse(2)                              maxValueHouse(1)
              /        \                                      /       \
             /          \                                    /         \
            /            \                                  /           \
           /              \                                /             \ 
maxValueHouse(4)         maxValueHouse(3)       maxValueHouse(3)      maxValueHouse(2)
```

#### Pseudocode
```
maxValueHouse(houses, currentHouse):
  If currentHouse > length of houses
    return 0
  Else
    stealFirstHouse = currentHouse + maxValueHouse(houses, currentHouse+2)
    skipFirstHouse = maxValueHouse(houses, currentHouse + 1)
    return max(stealFirstHouse, skipFirstHouse)
```

### Convert one string to another

#### Problem Statement
- S1 and S2 are given strings
- Convert S2 to S1 using delete, insert or replace operations
- Find the minimum count of edit operations

**Example 1**
- S1 = "catch"
- S2 = "carch"
- Output = 1
- Explanation: Replace "r" with "t"

**Example 2**
- S1 = "table"
- S2 = "tbres"
- Output = 3
- Explanation: Insert "a" to second position, replace "r" with "l" and delete "s"


**Example**
- S1 = "table"
- S2 = "tgable"

Delete "g" --> S2 = "tble" \
Insert "c" --> S2 = "tcble" \
Replace "a" --> S2 = "table"

Delete --> f(2,3)
Insert --> f(3,2)
Replace --> f(3,3)


#### Pseudocode
```
findMinOperation(s1, s2, index1, index2):
  If index1 == len(s1):
    return len(s2) - index2
  If index2 == len(s2)
    return len(s1) - index1
  If s1[index1] == s2[index2]
    return findMinOperation(s1, s2, index1+1, index2+1)
  Else
    deleteOp = 1 + findMinOperation(s1, s2, index1, index2+1)
    insertOp = 1 + findMinOperation(s1, s2, index1+1, index2)
    replaceOp = 1 + findMinOperation(s1, s2, index1+1, index2+1)
    return min(deleteOp, insertOp, replaceOp)
```

### Zero One Knapsack problem

#### Problem Statement
- Given the weights and profits of N items
- Find the maximum profit within given capacity of C
- Items cannot be broken

**Example 1**
| **Mango**  | **Apple**  | **Orange** | **Banana** |
|------------|------------|------------|------------|
| Weight: 3  | Weight: 1  | Weight: 2  | Weight: 5  |
| Profit: 31 | Profit: 26 | Profit: 17 | Profit: 72 |

**Knapsack Capacity**: 7

**Possible Combinations**:
- Mango (W:3, P:31) + Apple (W:1, P:26) + Orange (W:2, P:17) = W:6, Profit: 74
- Apple (W:1, P:26) + Banana (W:5, P:72) = W:6, Profit: 98
- Orange (W:2, P:17) + Banana (W:5, P:72) = W:7, Profit: 89

#### Subproblems:
Option 1 = 31 + f(2, 3, 4) \
Option 2 = 0 + f(2, 3, 4) \
Max(Option1, Option2)

#### Pseudocode
```
zoKnapsack(items, capacity, currentIndex):
  If capacity <= 0 or currentIndex < 0 or currentIndex > len(items):
    return 0
  Elif currentItemWeight <= capacity:
    Profit1 = currentItemProfit + zoKnapsack(items, capacity - currentItemsWeight, nextItem)
    Profit2 = zoKnapsack(items, capacity - currentItemsWeight, nextItem)
  Else
    return 0
```



### Longest Common Sequence Problem

#### Problem Statement
- S1 and S2 are given strings
- Find the length of the longest subsequence which is common to both strings
- Subsequence: a sequence that can be driven from another sequence by deleting some
elements without changing the order of them

| ABCDE | ACE | ABCE |
|-------|-----|------|
|       | ADE | ABDE |
|       | ACB |      |

**Example**
- S1 = "elephant"
- S2 = "erepat"
- Output = 5
- Longest String: "eepat"

#### Subproblems:
Option 1 = 1 + f(2,len(S1) : 2,len(S2))
Option 2 = 0 + f(3,len(S1) : 2,len(S2))
Option 3 = 0 + f(2,len(S1) : 3,len(s3))
Max(Option1, Option2, Option3)

#### Pseudocode
```
findCLS(s1, s2, index1, index2):
  If index1 == len(s1) or index2 == len(s2):
    return 0
  If s1[index1] == s2[index2]:
    op1 = 1 + findCLS(s1, s2, index1+1, index2+1)
    return op1
  Else
    op2 = findCLS(s1, s2, index1+1, index2)
    op3 = findCLS(s1, s2, index1, index2+1)
  return max(op2, op3)
```


### Longest Palindromic Subsequence Problem

#### Problem Statement
- S is a given string
- Find the longest palindromic subsequence (LPS)
- Subsequence: a sequence that can be driven from another sequence by deleting some
elements without changing the order of them
- Palindrome is a string that reads the same backward as well as forward

MADAM

**Example 1**
- S = "ELRMENMET"
- Output = 5
- LPS: "EMEME
- Length of S = 9

**Example 2**
- S = "AMEEWMEA"
- Output = 6
- LPS: "AMEEMA"
- Length of S = 8

#### Subproblems:
Option 1 = 2 + f(2,8)
Option 2 = 0 + f(1,8)
Option 3 = 0 + f(2,9)
Max(Option1, Option2, Option3)

#### Pseudocode
```
findLPS(s, startIndex, endIndex):
  If startIndex > endIndex:
    return 0
  If s[startIndex] == s[endIndex]:
    return 2 + findLPS(s, startIndex+1, endIndex-1)
  Else
    op1 = findLPS(s, startIndex, endIndex-1)
    op2 = findLPS(s, startIndex+1, endIndex)
  return max(op1, op2)
```



### Minimum cost to reach the Last cell problem

#### Problem Statement
- 2D Matrix is given
- Each cell has a cost associated with it for accessing
- We need to start from (0,0) cell and go until (n-1, n-1) cell
- We can go only to right or down cell from current cell
- Find the way in which the cost is minimum

#### Matrix
|   |   |   |   |   |
|---|---|---|---|---|
| 4 | 7 | 8 | 6 | 4 |
| 6 | 7 | 3 | 9 | 2 |
| 3 | 8 | 1 | 2 | 4 |
| 7 | 1 | 7 | 3 | 7 |
| 2 | 9 | 8 | 9 | 3 |

Find the path from 3 to 4 in which the cost is minimum

#### Path
|     |     |     |     |     |
|-----|-----|-----|-----|-----|
| *4* | 7   | 8   | 6   | 4   |
| *6* | *7* | *3* | 9   | 2   |
| 3   | 8   | *1* | *2* | 4   |
| 7   | 1   | 7   | *3* | *7* |
| 2   | 9   | 8   | 9   | *3* |

Minimum Cost: 36

#### Subproblems:
Option 1 = y + 9 + 3  f(4,3)
Option 2 = z + 7 + 3  f(3,4)
Max(Option1, Option2)


#### Pseudocode
```
findMinCost(twoDArray, row, col):
  If row == -1 or col == -1:
    return inf
  If row == 0 or col == 0:
    return twoDArray[row][col]
  Else
    op1 = findMinCost(twoDArray, row-1, col)
    op2 = findMinCost(twoDArray, row, col-1)
  return cost[row][col] + min(op1, op2)
```


### Number of Ways to reach the Last Cell with given Cost

#### Problem Statement
- 2D Matrix is given
- Each cell has a cost associated with it for accessing
- We need to start from (0,0) cell and go until (n-1, n-1) cell
- We can go only to right or down cell from current cell
- Find the number of ways to reach the end of the matrix with
a given "total cost"

#### Matrix
|   |   |   |   |
|---|---|---|---|
| 4 | 7 | 1 | 6 |
| 5 | 7 | 3 | 9 |
| 3 | 2 | 1 | 2 |
| 7 | 1 | 6 | 3 |

Find the path from 3 to 4 in which the given total cost

#### Path 1
|    |    |    |    |
|----|----|----|----|
| 4* | 7* | 1* | 6  |
| 5  | 7  | 3* | 9  |
| 3  | 2  | 1* | 2  |
| 7  | 1  | 6* | 3* |

#### Path 2
|    |    |    |    |
|----|----|----|----|
| 4* | 7* | 1* | 6  |
| 5* | 7* | 3* | 9  |
| 3  | 2  | 1* | 2* |
| 7  | 1  | 6  | 3* |

Minimum Cost: 36

#### Subproblems:
Option 1 = y + 2 + 22  f(3,4,22)
Option 2 = z + 6 + 22  f(4,3,22)
Sum(Option1, Option2)


#### Pseudocode
```
numberOfPaths(twoDArray, row, col, cost):
  If cost < 0:
    return 0
  If row == 0 or col == 0:
    If twoDArray[0][0] - cost == 0:
      return 1
    Else:
      return 0
  Elif row == 0:
    return numberOfPathhs(twoDArray, 0, col-1, cost-twoDArray[row][col])
  Elif col == 0:
    return numberOfPathhs(twoDArray, row-1, 0, cost-twoDArray[row][col])
  Else
    op1 = findMinCost(twoDArray, row-1, col, cost - twoDArray[row][col])
    op2 = findMinCost(twoDArray, row, col-1, cost - twoDArray[row][col])
  return op1 + op2
```


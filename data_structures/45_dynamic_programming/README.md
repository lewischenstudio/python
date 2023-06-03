## Section 45: Dynamic Programming

#### Table of Contents
- What is Dynamic Programming? (Overlapping property)
- Where does the name of DP come from?
- Top Down with Memoization
- Bottom Up with Tabulation
- Is Merge Sort Dynamic Programming?
- Number Factor Problem using Dynamic Programming
- House Robber Problem using Dynamic Programming
- Convert one string to another using Dynamic Programming
- Zero One Knapsack using Dynamic Programming


### What is Dynamic Programming? (Overlapping property)

Dynamic Programming (DP) is an algorithmic technique for solving an optimization problem
by breaking it down into simpler subproblems and utilizing the fact that the optimal
solution to the overall problem depends upon the optimal solution to its subproblems.

**Example 1**
```
1 + 1 + 1 + 1 + 1 + 1 + 1 = 7

1 + 1 + 1 + 1 + 1 + 1 + 1 + 2 = 9
|-----------------------|
          7
```

#### Optimal Substructure:

If any problem's overall optimal solution can be constructed from the optimal structure
of its subproblem, then this problem has optimal substructure.

Example: Fib(n) = Fib(n-1) + Fib(n-2)

#### Overlapping Subproblem

Subproblems are smaller versions of the original problem. Any problem has overlapping
sub-problems if finding its solution involves solving the same subproblem multiple times.


### Where does the name of DP come from?

The term **dynamic programming** was originally used in the 1940s by Richard Bellman to
describe the process of solving problems where one needs to find the best decisions
one after another. 



### Top Down with Memoization

Solve the bigger problem by recursively finding the solution to smaller subproblems.
Whenever we solve a sub-problem, we cache its result so that we don't end up solving
it repeatedly if it's called multiple times. This technique of storing the results of
already solved subproblems is called **memoization**.

**Example**: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...

Fibonacci(N) = Fibonacci(N-1) + Fibonnaci(N-2)

```python
def Fibonnaci(n):
  if n < 1 return error message
  if n = 1 return 0
  if n = 2 return 1
  if not in memo:
    memo[n] = Fibonacci(n-1, memo) + Fibonacci(n-2, memo)
  return memo[n] 
```
Time complexity: O(n) \
Space complexity: O(n) 

#### Top Down Recursion

| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      |        |        |        | F4+F5  |

| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      |        |        | F3+F4  | F4+F5  |

| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      |        | F2+F3  | F3+F4  | F4+F5  |

| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      | F1+F2  | F2+F3  | F3+F4  | F4+F5  |


#### Top Down Collection
| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      | 1      | F2+F3  | F3+F4  | F4+F5  |

| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      | 1      | 2      | F3+F4  | F4+F5  |

| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      | 1      | 2      | 3      | F4+F5  |

| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      | 1      | 2      | 3      | 5      |



### Bottom Up with Tabulation

Tabulation is the opposite of the top-down approach and avoids recursion. In this approach,
we sovle the problem "bottom-up" (i.e., by solving the related subproblems first). This is
done by filling up a table. Based on the results in the table, the solution to the 
top/original problem is then computed.

**Example**: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...

Fibonacci(N) = Fibonacci(N-1) + Fibonaaci(N-2)


#### Bottom Top Calculation

| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      | F1+F2  |        |        |        |

| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      | 1      |        |        |        |

| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      | 1      | F2+F3  |        |        |

| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      | 1      | 2      |        |        |

| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      | 1      | 2      | F3+F4  |        |

| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      | 1      | 2      | 3      |        |

| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      | 1      | 2      | 3      | F4+F5  |

| **F1** | **F2** | **F3** | **F4** | **F5** | **F6** |
|:------:|:------:|:------:|:------:|:------:|:------:|
| 0      | 1      | 1      | 2      | 3      | 5      |

```python
def fibonacciTab(n):
  tb = [0, 1]
  for i in range(2, n+1):
    tb.append(tb[i-1] + tb[i-2])
  return tb[n-1]
```

### Top Down vs Bottom Up

|                  | **Top Down**                    | **Bottom Up**              |
|------------------|---------------------------------|----------------------------|
| Easiness         | Easy, divide and conquer        | Difficult                  |
| Runtime          | Slow                            | Fast                       |
| Space efficiency | Unneccessary use of stack space | Stack is not used          |
| When to use      | Need a quick solution           | Need an efficient solution |


![Big O Complexity](https://github.com/lcycstudio/python/blob/master/data_structures/45_dynamic_programming/big_o_complexity.png)



### Is Merge Sort Dynamic Programming?

1. Does it have Optimal Substructure property?
2. Does it have Overlapping Subproblems property?

1. Yes, it does.
2. No, it doesn't. Not all subproblems are overlapping or repeating the same format.

![Merge Sort DP](https://github.com/lcycstudio/python/blob/master/data_structures/45_dynamic_programming/merge_sort.png)



### Number Factor Problem using Dynamic Programming

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

#### Pseudocode Top Down Approach
```
NumberFactor(N, memo):
  If N in (0,1,2) return 1
  If N = 3 return 2
  Elif N in memo return memo[n]
  Else
    rec1 = NumberFactor(N-1, memo)
    rec2 = NumberFactor(N-3, memo)
    rec3 = NumberFactor(N-4, memo)
    memo[n] = rec1 + rec2 + rec3
  return memo[n]
```

#### Pseudocode Bottom Up Approach
```python
def numberFactor(N):
  tb = [1,1,1,2]
  for i in range(4, n+1):
    tb.append(tb[i-1]+tb[i-3]+tb[i-4])
  return tb[n]
```


### House Robber Problem using Dynamic Programming

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

#### Pseudocode Top Down Approach
```
maxValueHouse(houses, currentHouse, memo):
  If currentHouse > length of houses
    return 0
  Else If currentHouse not in Memo:
    stealFirstHouse = currentHouse + maxValueHouse(houses, currentHouse+2)
    skipFirstHouse = maxValueHouse(houses, currentHouse + 1)
    memo[currentHouse] = max(stealFirstHouse, skipFirstHouse)
  return memo[currentHouse]
```


#### Pseudocode Bottom Up Approach
```python
def houseRobberBU(houses):
  tempArr = [0] * (len(houses)+2)
  for i in range(len(houses)-1,-1,-1):
    tempArr[i] = max(houses[i]+tempArr[i+2], tempArr[i+1])
  return tempArr[0]
```


### Convert one string to another using Dynamic Programming

#### Problem Statement
- S1 and S2 are given strings
- Convert S2 to S1 using delete, insert or replace operations
- Find the minimum count of edit operations

**Example**
- S1 = "table"
- S2 = "tgable"

Delete "g" --> S2 = "tble" \
Insert "c" --> S2 = "tcble" \
Replace "a" --> S2 = "table"

Delete --> f(2,3)
Insert --> f(3,2)
Replace --> f(3,3)


#### Pseudocode Top Down Approach
```
findMinOperation(s1, s2, index1, index2, memo):
  If index1 == len(s1):
    return len(s2) - index2
  If index2 == len(s2)
    return len(s1) - index1
  If s1[index1] == s2[index2]
    return findMinOperation(s1, s2, index1+1, index2+1, memo)
  Else
    dictKey = str(index1) + str(index2)
    If dictKey not in memo:
      deleteOp = 1 + findMinOperation(s1, s2, index1, index2+1, memo)
      insertOp = 1 + findMinOperation(s1, s2, index1+1, index2, memo)
      replaceOp = 1 + findMinOperation(s1, s2, index1+1, index2+1, memo)
      memo[dictKey] = min(deleteOp, insertOp, replaceOp)
    return memo[dictKey]
```

![String Conversion DP](https://github.com/lcycstudio/python/blob/master/data_structures/45_dynamic_programming/string_conversion_dp.png)



### Zero One Knapsack using Dynamic Programming

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

#### Pseudocode Top Down Approach
```
zoKnapsack(items, capacity, currentIndex, memo):
  dictKey = str(currentIndex) + str(capacity)
  If capacity <= 0 or currentIndex < 0 or currentIndex > len(items):
    return 0
  Elif dictKey in memo:
    return memo[currentIndex]
  Elif currentItemWeight <= capacity:
    Profit1 = currentItemProfit + zoKnapsack(items, capacity - currentItemsWeight, nextItem)
    Profit2 = zoKnapsack(items, capacity - currentItemsWeight, nextItem)
    memo[dictKey] = max(Profit1, Profit2)
    return memo[dictKey]
  Else
    return 0
```

#### Pseudocode Bottom Up Approach
```python
def zoKnapsackBU(profits, weights, capacity):
  if capacity <= 0 or len(profits) == 0 or len(weights) != len(profits):
    return 0
  numberOfRows = len(profits) + 1
  dp = [[0 for i in range(capacity+2)] for j in range(numberOfRows)]
  for row in range(numberOfRows-2,-1,-1):
    for column in range(1, capacity+1):
      profit1 = 0
      profit2 = 0
      if weights[row] <= column:
        profit1 = profits[row] + dp[row+1][column-weights[row]]
      profit2 = dp[row+1][column]
      dp[row][column] = max(profit1, profit2)
  return dp[0][capacity]
```

## Section 45: Dynamic Programming

#### Table of Contents
- What is Dynamic Programming? (Overlapping property)
- Where does the name of DP come from?
- Top Down with Memoization
- Bottom Up with Tabulation
- Top Down vs Bottom Up
- Is Merge Sort Dynamic Programming?
- Number Factor Problem using Dynamic Programming
- Number Factor : Top Down and Bottom Up
- House Robber Problem using Dynamic Programming
- House Robber : Top Down and Bottom Up
- Convert one string to another using Dynamic Programming
- Coding Exercise 45: Convert String using Bottom Up
- Solution to Convert String using Bottom Up
- Zero One Knapsack using Dynamic Programming
- Coding Exercise 46: Zero One Knapsack - Top Down
- Solution to Zero One Knapsack - Top Down
- Coding Exercise 47: Zero One Knapsack - Bottom Up
- Solution to Zero One Knapsack - Bottom Up


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


### House Robber : Top Down and Bottom Up



### Convert one string to another using Dynamic Programming



### Coding Exercise 45: Convert String using Bottom Up



### Solution to Convert String using Bottom Up



### Zero One Knapsack using Dynamic Programming



### Coding Exercise 46: Zero One Knapsack - Top Down



### Solution to Zero One Knapsack - Top Down



### Coding Exercise 47: Zero One Knapsack - Bottom Up



### Solution to Zero One Knapsack - Bottom Up



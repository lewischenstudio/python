## Section 1: Introduction

### What is a Data Structure?
Data structures are different ways of organizing data on your computer, that 
can be used effectively.

### What is an Algorithm?
It is a set of steps to accomplish a task.

### Algorithm in Computer Science
A set of rules for a computer program to accomplish a task
Input Data -> Calculation -> Stop when answer found


### Why are Data Structures and Algorithms in interviews?
- Problem solving skills
- Fundamental concepts of programming in limited time

### What makes a good algorithm?
1. Correctness
2. Efficiency

### Types of Data Structures

#### Primitive
- Integer
- Float
- Character
- String
- Boolean

#### Non Primitive
- Linear
  - List
  - Tuple
  - Array
  - Linked List
  - Stack
  - Queue
- Non-linear
  - Set
  - Dictionary
  - Tree
  - Graph

### Types of Algorithms
#### Sorting algorithms
- Sort data into ascending or descending order
- Examples: quick sort and merge sort

#### Search algorithms
- Find a specific value in a data set

#### Graph
- Work with data that can be represented as a graph

#### Dynamic programming algorithms
- Helps to efficiently solve a class of problems that have overlapping subproblems and optimal substructure property
- Find the best solution based on memonization

#### Divide and conquer algorithms
- Divide the problem into smaller subproblems of the same type, and solve these subproblems directly
- Combine the solutions to the subproblems into a solution to the original problem

#### Recursive algorithms
- Solve the problems by breaking them down into smaller sub-problems that are similar in nature
- Calls itself with smaller input values and returns the result for the current input by carrying out basic operations on the returned value for the smaller input
```python
Algorithm Sum(A, n)
  if n = 1
    return A[0]
  s = Sum(A, n-1) # recurse on all but last
  s = s + A[n-1]  # add last element
return s
```

#### Greedy algorithms
- We take the best we can without worrying about future consequences
- We hope that by choosing a local opitimum solution at each step, we will end up at a global optimum solution

#### Brute force algorithms
- It simply tries all possibilities until a satisfactory solution is found

#### Randomized algorithms
- Use a random number at least once during the computation to make a decision


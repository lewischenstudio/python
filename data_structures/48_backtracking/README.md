## Section 47: A Receipe for Problem Solving

#### Table of Contents
- What is Backtracking?
- Backtracking vs Brute Force Approach
- Backtracking Questions
- N - Queens Problem
- N - Queens Problem in Python


### What is Backtracking?

A backtracking algorithm is a problem-solving algorithm that uses a brute force
approach for finding the desired output.

```
              Brute Force Approach
                /           \
              /               \
            /                   \
Backtracking                    Dynamic Programming
    |                                   |
    |                                   |
    |                                   |
All Solutions                       Best Solution
```

There are 3 types of problems in backtracking:
- **Decision Problem** - search for a feasible solution
- **Optimization Problem** - search for the best solution
- **Enumeration Problem** - find all feasible solutions

#### State Space Tree

![State Space Tree](https://github.com/lcycstudio/python/tree/master/data_structures/48_backtracking/state_space_tree.png)


Steps in backtracking
1. Backtracking checks whether the given node is valid solution or not.
2. Discard several invalid solutions with one iteration.
3. Enumerate all subtree of the node to find the valid solution.

**Example** 3! = 6

![SST Example](https://github.com/lcycstudio/python/tree/master/data_structures/48_backtracking/sst_example.png)



### Backtracking vs Brute Force Approach

#### Brute Force

We are searching all available states to find the solution for the problem.

#### Backtracking

We are eliminating invalid solutions and find the next best solution.

![Backtracking vs Brute Force](https://github.com/lcycstudio/python/tree/master/data_structures/48_backtracking/backtracking_brute_force.png)


### Backtracking Questions

- Question 1: Which one is faster usually and why: brute-force approach or backtracking?
  - Backtracking because it skips (eliminates) multiple bad states in a single iteration
  (single recursive function call)
- Question 2: Backtracking is a form of recursion.
  - True
- Question 3: Why is it called backtracking?
  - The algorithm backtracks to the previous state if the actual one is not feasible
  (not good) - hence the name backtracking



### N - Queens Problem

Place **N** queens on an **NxN** chess board, in such a manner that no two queens can
attack each other.
- Not same column
- Not same row
- Not diagonal

![N Queens Problem](https://github.com/lcycstudio/python/tree/master/data_structures/48_backtracking/n_queens_problem.png)


#### Steps
1. Start in the leftmost column
2. If all queens are placed, return true
3. Try all rows in the current column. Do the following for every tried row.

   (a) If the queen can be placed safely in this row, then mark this `[row, column]`
   as part of the solution and recursively check if placing queen here leads to a
   solution.

   (b) If placing the queen in `[row, column]` leads to a solution then return true.

   (c) If placing queen doesn't lead to a solution, then unmark this `[row, column]`
   (Backtrack) and go to step (a) to try another row.
4. If all rows have been tried and nothing worked, 
return false to trigger backtracking.



### N - Queens Problem in Python




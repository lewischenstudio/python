# Recursion

## What is Recursion?
Recursion is a way of solving a problem by having a function calling itself.

## Why Recursion?
1. Recursive thinking is really important in programming and it helps you break down big problems into smaller ones and easier to use
2. The prominent usage of recursion in data structures like trees and graphs
3. Interviews
4. It is used in many algorithms (divide and conquer, greedy and dynamic programming)

## When to choose Recursion?
- If you can divide the problem into similar sub problems
- Design an algorithm to compute `nth` terms
- Write code to list the `n`
- Implement a method to compute all

## How Recursion works?
1. A method that calls itself
2. Exit from inifinite loop

## Recursive vs Iterative Solutions
| Points           | Recursion | Iteration |                                                                                                                                  |
|------------------|-----------|-----------|----------------------------------------------------------------------------------------------------------------------------------|
| Space efficient? | No        | Yes       | No stack memory require in case of iteration                                                                                     |
| Time efficient?  | No        | Yes       | In case of recursion system needs more time for pop and push elements to stack memory which makes  recursion less time efficient |
| Easy to code?    | Yes       | No        | We use recursion especially in the cases we know that a problem can be divided into similar sub- problems                        |


## When to use Recursion?
- When we can easily breakdown a problem into similar subproblem
- When we are fine with extra overhead (both time and space) that comes with it
- When we need a quick working solution instead of efficient one
- When traverse a tree
- When we use memoization in recursion

## When to avoid Recursion?
- If time and space complexity matters for us
- Recursion uses more memory. If we use embedded memory. For example an application
that takes more memory in the phone is not efficient
- Recursion can be slow

## How to write recursion in 3 steps?
- Step 1: Recursive case - the flow
- Step 2: Base case - the stopping criterion
- Step 3: Unintentional case - the constraint

## Factorial
### Step 1: Recursive case - the flow
- `n! = n * (n-1) * (n-2) * ... * 2 * 1`
- `n! = n * (n-1)!`

### Step 2: Base case - the stopping criterion
- 0! = 1
- 1! = 1

### Step 3: Unintentional case - the constraint
- positive integers only


## Fibonacci
### Step 1: Recursive case - the flow
- `5 = 3 + 2`
- `f(n) = f(n-1) + f(n-2)`

### Step 2: Base case - the stopping criterion
- 0, and 1

### Step 3: Unintentional case - the constraint
- positive integers only

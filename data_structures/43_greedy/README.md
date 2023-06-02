## Section 43: Greedy Algorithm

#### Table of Contents
- What is Greedy Algorithm?
- Greedy Algorithms (Insertion Sort, Selection Sort, Prim, Kruskal, Topological )
- Activity Selection Problem
- Activity Selection Problem in Python
- Coin Change Problem
- Coin Change Problem in Python
- Fractional Knapsack Problem
- Fractional Knapsack Problem in Python


### What is Greedy Algorithm?

A greedy algorithm is any algorithm that follows the problem-solving heuristic of
making the locally optimal choice at each stage.

- Insertion Sort
- Selection Sort
- Topological Sort
- Prim's Algorithm
- Kruskal Algorithm

- Activity Selection Problem
- Coin Change Problem
- Fractional Knapsack Problem


### Greedy Algorithms (Insertion Sort, Selection Sort, Prim, Kruskal, Topological )

#### Insertion Sort
Divide the given array into two part. Take first element from unsorted array and find
its correct position in sorted array Repeat until unsorted array is empty, in a way
that `sorted_list = []` and `unsorted_list = [5, 3, 4, 7, 2, 8, 6, 9, 1]`.


#### Selection Sort
It repeatedly finds the mimum element and move it to the sorted part of array 
to make unsorted part sorted, so that `sorted_list = []` and 
`unsorted_list = [5, 7, 4, 3, 8, 6, 1, 9, 2]`.


#### Topological Sort
Topological Sort is a sorting algorithm that sorts actions in such a way that
if there is a dependency of one action on another, then the dependent action
always comes later than its parent action.


#### Prim's Algorithm
- It finds a minimum spanning tree for weighted undirected graphs.

#### Kruskal Algorithm
It finds a minimum spanning tree for weighted undirected graphs.


### Activity Selection Problem

Given N number of activities with their start and end times. We need to select
the maximum number of activities that can be performed by a single person,
assuming that a person only work on a single activity at a time.

| **Activity** | **A1** | **A2** | **A3** | **A4** | **A5** | **A6** |
|--------------|--------|--------|--------|--------|--------|--------|
| **start**    | 0      | 3      | 1      | 5      | 5      | 8      |
| **Finish**   | 6      | 4      | 2      | 8      | 7      | 9      |

| **Activity** | **A3** | **A2** | **A1** | **A4** | **A5** | **A6** |
|--------------|--------|--------|--------|--------|--------|--------|
| **start**    | 1      | 3      | 0      | 5      | 5      | 8      |
| **Finish**   | 2      | 4      | 6      | 8      | 7      | 9      |


#### Pseudocode
- Sort activities based on finish time
- Select first activity from sorted array and print it
- For all remaining activities, if the start time of this activity is greater
or equal to the finish time of previously selected activity, then select this
activity and print it



### Coin Change Problem

You are given coins off different denominations and total amount of money. Find the
maximum number of coins that you need to make up the given amount.

Infinite supply of denominations: {1, 2, 5, 10, 20, 50, 1000, 1000}

| Total amount: 2035  | Result |
|:-------------------:|:------:|
| 2035 - 1000  = 1035 | 1000   |
| 1035 - 1000  = 35   | 1000   |
| 35 - 20  = 15       | 20     |
| 15 - 10  = 5        | 10     |
| 5 - 5  = 0          | 5      |

Answer: 5

#### Pseudocode
- Find the biggest coin that is less than given total number
- Add coin to the result and subtract coin from total number
- If V is equal to zero:
    Then print result
  else:
    Repeat step 2 and 3


### Fractional Knapsack Problem

Given a set of items, each with a weight and a value. Determine
the number of each item to include in a collection so that the
total weight is less than or equal to a given limit and the
total value is as large as possible.

A box = 50k \
item blue = 20kg, $100 \
item red = 30kg, $120 \
item green = 10kg, $60

The answer is 60 + 100 + 120*2/3 = 240

#### Greedy Approach
density of item blue = $100 / 20kg = 5 \
density of item red = $120 / 30kg = 4
density of item green = $60 / 10kg = 6 \

#### Reordering
density of item green = $60 / 10kg = 6 \
density of item blue = $100 / 20kg = 5 \
density of item red = $120 / 30kg = 4

- Take as much as we can from the highest density item, which is 10kg for $60.
- Take as much as we can from the second highest density item, which is 20kg for $100.
- Take as much as we can from the third highest density item, which is 20kg for $80.

#### Pseudocode
- Calculate the density or ratio for each item
- Sort items based on this ratio
- Take items with the highest ratio sequentially until weight allows
- Add the next item as much (fractional) as we can

## Section 2: Big O Notation

#### What is Big O?
Big O is the language and metric we use to describe the efficiency of algorithms.

Time complexity is a way of showing how the runtime of a function increases as the size of input increases.

#### Types of Runtimes
- O(N), O(N^2), O(2^N)
- Time complexity: O(wh)

- Big O: It is a complexity that is going to be <em>less or equal to the worst case</em>.
- Big Omega: It is a complexity that is going to be <em>at least more than the best case</em>.
- Big Theta: It is a complexity that is <em>within bounds of the worst and the best cases</em>.


#### Runtime Complexities
Number of operations vs number of elements

###### O(1)
- It is a constant time complexity
- It is a horizontal line on the graph
```python
def number_squared(n):
    return n * n
```
###### O(N)
- It is a proportional straight line on the graph
- Programs with parallel loops are also O(N)
```python
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
```

###### O(N^2)
- It is a proportional curved line on the graph, in the shape of exponential function.
```python
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```

###### O(LogN)
- It is a relatively flat line on the graph, although not as flat as O(1).
- O(LogN) is mathematically analogous to `log_2^N`, e.g., `log_2^8=3` and `log_2^1048576=20`.

###### Remarks
- It is very possible that O(N) code is faster than O(1) code for specific inputs
- Different computers with different architectures have different constant factors.
- Different algorithms with the same basic idea and computational complexity might have slightly different constants.
- As `n \to \infty`, constant factors are not really a big deal.
- Add the runtimes: we can merge constants for paraellel loops, e.g., O(A + B) --> O(N).
- Multiply the runtimes: we can merge constants for nested loops, e.g., O(A * B) --> O(N^2).
- Refactor the runtimes: we can drop non-dominant constants for paraellel loops, e.g., O(N^2 + N) --> O(N^2).


#### Space Complexity
The following function takes O(N) space complexity that consumes a large amount of memory over time. Memory added to the stack: sum(4), sum(3), sum(2), sum(1)
```python
def sum(n):
    if n <= 0:
        return 0
    return n + sum(n - 1)
```

The following function takes O(1) space complexity that saves memory. `pari_sum` function does not exist simultaneously on the call stack.
```python
def pair_sum_sequence(n):
    total = 0
    for i in range(0):
        total = total + pair_sum(i, i + 1)
    return total
def pair_sum(a, b):
    return a + b
```

#### How to measure code using Big O
| No     | Description                                                                                              | Complexity |
|--------|----------------------------------------------------------------------------------------------------------|------------|
| Rule 1 | Any assignment statements and if statements that are executed once regardless of the size of the problem | O(1)       |
| Rule 2 | A simple "for" loop from 0 to n (with no internal loops)                                                 | O(n)       |
| Rule 3 | A nested loop of the same type takes quadratic time complexity                                           | O(n^2)   |
| Rule 4 | A loop, in which the controlling parameter is divided by two at each step                                | O(log n)   |
| Rule 5 | When dealing with multiple statements, just add them up                                                  | depends    |

```python
def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0] # -----------------------------> O(1)
    for index in range(1, len(sampleArray)): # -------------------> O(n)
        if sampleArray[index] > biggestNumber: # -----------------> O(1)
            biggestNumber = sampleArray[index] # -----------------> O(1)
    print(biggestNumber) # ---------------------------------------> O(1)
```
- `if sampleArray[index] > biggestNumber`: O(1)
- `biggestNumber = sampleArray[index]`: O(1)
- O(1) + O(1) -> 2 O(1) -> O(1)
- `for index in range(1, len(sampleArray))`: O(n)
- O(n) + O(1) -> O(n + 1) -> O(n), because O(n) is the dominant term.
- Add final complexities: O(1) + O(n) + O(1) -> O(n)
- The time complexity for `findBiggestNumber` is O(n)

#### How to measure Recursive Algorithms?
```python
def findMaxNumRec(sampleArray, n): # -----------------------------------> M(n)
    if n = 1: # --------------------------------------------------------> O(1)
        return sampleArray[0] # ----------------------------------------> O(1)
    return max(sampleArray[n-1], findMaxNumRec(sampleArray, n-1)) # ----> M(n-1)
A = [11, 4, 12, 7]
n = 4 ## length of array
findMaxNumRec(A, 4)
```
- findMaxNumRec(A, 4) -> max(A[4-1], 12) -> max(7, 12) = 12
- findMaxNumRec(A, 3) -> max(A[3-1], 11) -> max(12, 11) = 12
- findMaxNumRec(A, 2) -> max(A[2-1], 11) -> max(4, 11) = 11
- findMaxNumRec(A, 1) -> A[0] = 11

###### Time complexity
```math
M(n) = O(1) + M(n-1)            (1)
M(1) = O(1)                     (2)
M(n-1) = O(1) + M((n-1) - 1)    (3)
M(n-2) = O(1) + M((n-2) - 1)    (4)
Let O(1) be 1. Substitute (3) into (1)
M(n) = 1 + M(n-1)
     = 1 + (1 + M((n-1) - 1))
     = 2 + M(n-2)
     = 2 + 1 + M((n-2) - 1)
     = 3 + M(n-3)
        .
        .
     = a + M(n - a)
Let a be n - 1.
M(n) = n - 1 + M(n - (n - 1))
     = n - 1 + M(1)
     = n - 1 + 1
     = n
```
The time complexity for recursive algorithms is usually O(n).

#### How to measure Recursive Algorithms that make multiple calls?
```python
def f(n):
    if n <= 1:
        return 1
    return f(n-1) + f(n-2)
```
```python
"""
                                                                       Level

                            f(4)   -----------------------------------> 0
                        /           \ 
                    /                   \ 
                /                           \ 
             f(3)                            f(3) --------------------> 1
          /       \                       /        \ 
        /           \                   /            \ 
     f(2)            f(2)            f(2)            f(2) ------------> 2
    /   \           /   \           /   \           /   \ 
f(1)    f(1)    f(1)    f(1)    f(1)    f(1)    f(1)    f(1) ---------> 3
"""
```
| N | Level | Node ## | Expression                         | Power |
|---|-------|--------|------------------------------------|-------|
| 4 | 0     | 1      |                                    | 2^0   |
| 3 | 1     | 2      | 2 * previous level = 2 * 2^0 = 2^1 | 2^1   |
| 2 | 2     | 4      | 2 * previous level = 2 * 2^1 = 2^2 | 2^2   |

###### Time complexity
```math
2^0 + 2^1 + 2^2 + ... = 2^n+1 - 1
                      = 2^n-1
                      -> O(2^n)
```
Time complexity is O(branches^(depth))

#### Exercises

###### The runtime of the code below is O(n)
```python
def f(n):
    if n <= 0:
        return 1
    return 1 + f(n-1)
```

###### The runtime of the code below is O(n)
```python
def f(n):
    if n <= 0:
        return 1
    return f + f(n - 5)
```

###### The runtime of the code below is O(n)
```python
def f(n):
    if n <= 0:
        return 1
    return 1 + f(n/5)
```

###### The runtime of the code below is O(2^n)
```python
def f(n, m, o):
    if n <= 0:
        print(n, m, o)
    f(n-1, m+1, o)
    f(n-1, m, o+1)
```

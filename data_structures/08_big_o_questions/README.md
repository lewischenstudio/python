## Interview Questions - 1
What is the runtime of the code below?

```python
def foo(array):
    sum = 0 # O(1)
    product = 1 # O(1)
    for i in array: # O(n)
        sum += i #O(1)
    
    for i in array: # O(n)
        product *= i # O(1)
    
    print("Sum = " + str(sum) + ", Product = " + str(product)) # O(1)
```
Time Complexity: O(N)


## Interview Questions - 2
What is the runtime of the code below?
```python
def printPairs(array):
    for i in array: # O(n^2)
        for j in array: # O(n)
            print(str(i) + "," + str(j)) # O(1)
```
Time Complexity: O(N^2)


## Interview Questions - 3
What is the runtime of the code below?
```python
def printUnorderedPairs(array):
    for i in range(0, len(array)): # O(n^2)
        for j in range(i+1, len(array)): # O(n)
            print(array[i] + "," + array[j]) # O(1)
```
1. Counting the iterations
```
1st --> n - 1
2nd --> n - 2
    .
    .
    1
(n - 1) + (n - 2) + (n - 3) + ... + 2 + 1
= 1 + 2 + ... + (n - 3) + (n - 2) + (n - 1)
= n (n - 1) / 2
= n^2 / 2 + n
= n^2
```
2. Average Work
Outer loop - N times\
Inner loop?
```
1st --> 10
2nd --> 9
    .
    .
    1
= 5 --> 10 / 2
= n --> n / 2

n * n / 2 = n^2 / 2 --> O(N^2)
```
Time Complexity: O(n^2)


## Interview Questions - 4
What is the runtime of the code below?
```python
def printUnorderedPairs(arrayA, arrayB):
    for i in range(0, len(arrayA)): # O(n^2)
        for j in range(i+1, len(arrayB)): # O(n)
            if arrayA[i] < arrayB[j]: # O(1)
                print(str(arrayA[i] + "," + str(arrayB[j]))) # O(1)
```
a = len(arrayA) \
b = len(arrayB) \
Time Complexity: O(ab)


## Interview Questions - 5
What is the runtime of the code below?
```python
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)): # O(ab)
        for j in range(len(arrayB)): 
            for k in range(0, 100000): # O(1)
                print(str(arrayA[i]) + "," + str(arrayB[j])) # O(1)
```
a = len(arrayA) \
b = len(arrayB) \
100,000 units of work is still constant \
Time Complexity: O(ab)


## Interview Questions - 6
What is the runtime of the code below?
```python
def reverse(array):
    for i in range(0, int(len(array)/2)): # O(n/2) -> O(n)
        other = len(array) - i - 1 # O(1)
        temp = array[i] # O(1)
        array[i] = array[other] # O(1)
        array[other] = temp # O(1)
    print(array) # O(1)
```
input: [1, 2, 3, 4, 5] \
output: [5, 4, 3, 2, 1] \
Time Complexity: O(N)



## Interview Questions - 7
Which of the following are equivalent to O(N)? Why?
```
1. O(N + P), where P < N/2
2. O(2N)
3. O(N + logN)
4. O(N + NlogN)
5. O(N + M)
```
1, 2, 3

The first one says that P is less than N divided by two, which means that N is greater than P. So if you go over here, N is dominant and P is non dominant term which means that we can drop P and make this O(N), which is equivalent to O(N).

In the second one, this is a quite easy one, because here we just need to drop constant from here. The constant is 2, if you drop it this becomes O(N), which is the answer that we are looking for.

In the third one, our Big O complexity chart might be useful because we need to identify which one is dominant temr O(N) or LogN. So if you look at the graph, we see that O(N) is over here and O(LogN) is over here, which means that O(N) is dominant term here. So according to our rules, we can drop non dominant term. So if we drop logN from here, this becomes O(N) which is the answer that we are looking for.

In the fourth one as well, we need to use graph again, from graph we see that O(NLogN) is over here, O(N) is over here, which means that in this case O(NLogN) is dominant term, so we need to drop O(N), if we drop O(N) we see that our complexity will become O(NLogN) which is not equivalent to O(N).

The last one is tricky one, many people tend to remove M from here and make it O(N). But this is not correct because there is no established relationship between N and M here. So we need to keep both variables here. So this is not equivalent to O(N).

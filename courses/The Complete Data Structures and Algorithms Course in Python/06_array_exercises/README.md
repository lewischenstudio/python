# Cracking Array/List Coding Exercises

- Coding Exercise 1: Find Missing Number
- Coding Exercise 2: Max Product of Two Integers
- Coding Exercise 3: Middle Function
- Coding Exercise 4: 2D Lists
- Coding Exercise 5: Best Score
- Coding Exercise 6: Duplicate Number
- Coding Exercise 7: Pairs
- Coding Exercise 8: Contains Duplicate
- Coding Exercise 9: Rotate Matrix/ Image - LeetCode 48
- Coding Exercise 10: Pairs / Two Sum - LeetCode 1
- Coding Exercise 11: Finding a number in an Array
- Coding Exercise 12: Permutation
- Coding Exercise 13: Missing Number


### Coding Exercise 1: Missing Number

Write a function to find the missing number in a given integer array of 1 to 100.

**Example**
```python
missing_number([1, 2, 3, 4, 6], 6) # 5
```

### Coding Exercise 2: Max Product of Two Integers


Max Product of Two Integers
Find the maximum product of two integers in an array where all elements are positive.

**Example**
```python
arr = [1, 7, 3, 4, 9, 5] 
max_product(arr) # Output: 63 (9*7)
```


### Coding Exercise 3: Middle Function

Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

**Example**
```python
myList = [1, 2, 3, 4]
middle(myList)  # [2,3]
```


### Coding Exercise 4: 2D Lists

Given 2D list calculate the sum of diagonal elements.

**Example**
```python
myList2D= [[1,2,3],[4,5,6],[7,8,9]]

sumDiagonal(myList2D) # 15
```



### Coding Exercise 5: Best Score

Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

**Example**
```python
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
firstSecond(myList) # 90 87
```



### Coding Exercise 6: Duplicate Number

Write a function to find the duplicate number on given integer array/list.

**Example**
```python
removeDuplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
```


### Coding Exercise 7: Pairs

Write a function to find all pairs of an integer array whose sum is equal to a given number.
Do not consider commutative pairs.

**Example**
```python
pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']
```


### Coding Exercise 8: Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

**Example** :
```python
Input: nums = [1,2,3,1]
Output: true
```



### Coding Exercise 9: Rotate Matrix/ Image - LeetCode 48

You are given an n x n 2D matrix representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image **in-place**, which means you have to modify the input 2D matrix directly.

**DO NOT** allocate another 2D matrix and do the rotation.

**Example**:

```python
# Input: 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 
[[7,4,1],[8,5,2],[9,6,3]]
```



### Coding Exercise 10: Pairs / Two Sum - LeetCode 1

Write a program to find all pairs of integers whose sum is equal to a given number
```
[2, 6, 3, 9, 11]    9    -----> [6,3]
```
- Does the array contain only positive or negative numbers?
- What is the same pair repeats twice, should we print it every time?
- If the reverse of the pair is acceptable, e.g., can we print (4,1) and (1,4) if the 
given sum is 5.
- Do we need to print only distinct pairs? Does (3,3) count as a valid pair for 6?
- How big is the array?



### Coding Exercise 11: Finding a number in an Array

Write a function to check if an array contains a number in an array.


### Coding Exercise 12: Permutation

Write a function to determine if two arrays are permutations of one another.



### Coding Exercise 13: Missing Number

Write a function to find the missing number in a given integer array of 1 to 100.

**Example**
```python
missingNumber([1, 2, 3, 4, 6], 6) # 5
```

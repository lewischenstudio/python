## Section 09: Math Question: Missing Number (Easy)

#### Table of Contents
- Introduction to the problem
- Approach 1: Brute Force Approach
- Approach 2: A Better Approach Explanation
- PseudoCode Walkthrough For Approach 2
- Implementing the code
- Approach 3: Optimal Approach
- Implementing the optimal approach
- [Custom Input - NEW] - Missing Number - Easy #268


### Introduction to the problem

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

[268. Missing Number](https://leetcode.com/problems/missing-number/)



### Approach 1: Brute Force Approach

- Sort the array first: `[5, 3, 2, 4, 0]` --> `[0, 2, 3, 4, 5]`
- Difference between every 2 consecutive elements is 1, except difference between the
  missing number and the next number is 2

```
missingNumber(input) {
    softedInput = sort(input)
    for i in range(1, sortedInput.length) {
        expectedNumber = sortedInput[i] - 1
        if (sortedInput[i - 1] != expectedNumber) {
            return expectedNumber
        }
    }
}
```
Time complexity: O(N)
Space complexity: O(1)


### Approach 2: A Better Approach Explanation

```
findMissing(input) {
    presentNumbers = {}
    for number in input {
        presentNumbers[number] = true
    }
    for i in range[0, n] {
        if (presentNumbers[i] is not true) {
            return i
        }
    }
}
```
Time complexity: O(N)
Space complexity: O(N)

### PseudoCode Walkthrough For Approach 2



### Implementing the code



### Approach 3: Optimal Approach



### Implementing the optimal approach



### [Custom Input - NEW] - Missing Number - Easy #268






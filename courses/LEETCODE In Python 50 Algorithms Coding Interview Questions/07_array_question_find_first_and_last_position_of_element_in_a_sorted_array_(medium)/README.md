## Section 07: Array Question: Find First and Last Position of Element in a Sorted Array (Medium)

#### Table of Contents
- Introduction to the problem and brute force approach
- Bruteforce Psuedo code walkthrough
- Approach 2: Optimal Approach intuition
- Psuedo code walkthrough part 1
- Psuedo code walkthrough part 2
- Implementing the code


### Introduction to the problem and brute force approach
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

Example 2:
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

Example 3:
```
Input: nums = [], target = 0
Output: [-1,-1]
```

#### Questions
- What if there is only one occurrence of the target?
  `[10, 11, 13, 15, 17, 18]` Target = 13
  return `[2, 2]`
- What if the target is not found?
  `[10, 11, 13, 15, 17, 18]` Target = 14
  return `[-1, -1]`


#### Brute Force
We can search from the first index of the input and
from the last index of the input using the left
and right loopers. Once the target is found, 
we put them in the array. 

```
searchRange(input, target) {
    first = findFirst(input, target)
    last = findLast(input, target)
    return [first, last]
}
findFirst(input, target) {
    n = input.length
    Loop as i in range[0: n ]{
        if (input[i] == target) {
            return i
        }
    }
    return -1
}
findLast(input, target) {
    n = input.length
    Loop as i in range[n-1: 0 ]{
        if (input[i] == target) {
            return i
        }
    }
    return -1
}
```
Time Complexity: O(n)
Space Complexity: O(1)


### Approach 2: Optimal Approach
Array is sorted: think Binary Search

`[10, 11, 11, 11, 14, 15]`

mid = (5 + 0) / 2 = 2

mid is equal to our target, but it is not the first
occurrence. The array is sorted, and we can check
whether mid-1 would be our target.

### getLeftPosition
```
left = 0
right = len(input) - 1
while (left <= right) {
    mid = (left + right) / 2
    if (input[mid] == target) {
        if (mid == 0 || input[mid-1] != target) {
            return mid
        }
        right = mid - 1
    } else if (input[mid] > target) {
        right = mid - 1
    } else {
        left = mid + 1
    }
}
return -1
```

#### getRightPosition
```
left = 0
right = len(input) - 1
while (left <= right) {
    mid = (left + right) / 2
    if (input[mid] == target) {
        if (mid == len(mid) - 1 || input[mid-1] != target) {
            return mid
        }
        left = mid + 1
    } else if (input[mid] > target) {
        right = mid - 1
    } else {
        left = mid + 1
    }
}
return -1
```

Time complexity: O(log(n))
Space complexity: O(1)
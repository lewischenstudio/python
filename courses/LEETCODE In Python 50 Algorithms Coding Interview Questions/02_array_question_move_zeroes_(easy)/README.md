## Section 02: Array Question: Move Zeroes (Easy)

#### Table of Contents
- Problem Introduction
- Brute force Intuition
- Brute force psuedo code walkthrough
- Better Approach Intuition
- Better Approach Psuedo code walkthrough
- Implementing the code


### Problem Introduction
Given an array of integers, write a function to move all 0's to the end of the array
while maintaining the relative order of the other elements

[283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)


### Brute force Intuition
#### Questions
- Are the elements sorted?
  No
- Can the entire array only consist of zeros?
  Yes

#### Brute Force
- Create new array with the same size as the input
- Loop over input array and push non-zero elements to new array
- Push zeroes for rest of the new array size

```
input = [0, 1, 0, 3, 12]
moveZeroes(input) {
    output = []
    n = input.length
    Loop as i in range(0, n) {  O(n)
        if (input[i] is non-zero) {
            output.add(input[i])
        }
        m = output.length
        Loop in range(m,n) { O(n-m)
            output.add(0)
        }
    }
}
```
#### Time complexity: 
O(n+n-m) = O(2n-m)
n: length of input
m: number of non-zero elements

#### Space Complexity
O(n)


### Better Approach Intuition
#### Approach Intuition
- Define a pointer `j` at the beginning of the array
- Loop over every element in the array
- If the current element is not zero, set the element at `j` to it
  and increment `j`
- After loop ends, set all elements from position `j` to the end of
  the array to zero

```
moveZeroes(input) {
    j = 0
    for each num in input {
        if (num! == 0) {
            input[j] = num
            j += 1
        }
    }
    for every position x starting from j until input end {
        input[x] = 0
    }
}   
```
#### Time complexity: 
O(n+m)
n: length of input
m: number of non-zero elements

#### Space Complexity
O(1)

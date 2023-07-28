## Section 04: Array Question: Void Mountain Array (Easy)

#### Table of Contents
- Introduction to the problem
- How to think about this problem
- Psuedo code Walkthrough
- Implementing the code

Given an array of integers, return true if the following conditions are fulfilled
- Length of the array is bigger than or equal to 3
- There exists some index `i` such that:
  a[0] < a[1] < ... < a[i]
  a[i] > a[i+1] > ... > a[a.size - 1]


[941. Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/)


#### Questions
- Can we receive an empty array?
  No.
- What should we return in case we have only 1 element in the array?
  Return false.
- Should we return false if the input size is 2?
  Yes, return false. You need 3 elements at least.


### How to think about this problem

#### What do we need to keep track of?
Where the increasing subsequence ends

#### Why do we need to keep track of it?
To know where to start checking for a decreased sequence

#### How do we keep track of it?
Use a pointer.

#### When would we return false before even checking for a decreasing subsequence?
- If we didn't move from our location
- If we already reached the end of the array

#### Steps
- Loop over an array starting from loop index as long as it is increasing
- If loop index didn't move or reached the end of the array, we return false
- Loop over array starting from the loop index for the decreasing sequence
- If loop index is at the end of the array, return false

```
i = 1
while (i < A.length and A[i] > A[i-1]) {
    i += 1
}
if (i == 1 or i == len(A)) {
    return false
}
while (i < A.length and A[i] < A[i-1]) {
    i += 1
}
return i == len(A)
```

# Time Complexity
O(N)

# Space Complexity
O(1)


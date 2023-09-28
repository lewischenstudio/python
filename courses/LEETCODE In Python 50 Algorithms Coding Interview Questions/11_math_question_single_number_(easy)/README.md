## Section 11: Math Question: Single Number (Easy)

#### Table of Contents

- Introduction to the problem and brute force approach
- Pseudocode walkthrough for brute approach
- Approach 2: better Approach
- Implementing the code
- Approach 3: optimal approach
- Implementing the optimal approach

### Introduction to the problem and brute force approach

Given a non-empty array of integers, every element appears twice except for one, find it.

(136. Single Number)[https://leetcode.com/problems/single-number/]

Example 1:

- Input: nums = [2,2,1]
- Output: 1

Example 2:

- Input: nums = [4,1,2,1,2]
- Output: 4

Example 3:

- Input: nums = [1]
- Output: 1

#### Is the given array sorted?

No, there is no guarantee that the array is sorted.

#### What do we know?

- All elements will occur twice except for a single element, we are guaranteed that.
- If we can track all of the elements alongside their occurences in the array, we can easily
  find which element occured only once.

#### What can we use for this?

We'll use hash maps to keep track of our elements

### Pseudocode walkthrough for brute approach

```
singleNumber(input) {
    m = {}
    for num in input {
        m[num] += 1
    }
    for key in m {
        if (m[key] == 1) {
            return key
        }
    }
}
```

Time complexity: O(N)

Space complexity: O(N)

### Approach 2: better Approach

#### What do we know?

Each element occurs twice except for the one element.

2(a + b + c) = 2a + 2b + 2c is what we would've had if all elements
occurred twice.

2a + 2b + c is what we actually have.

Our answer should be c, which is what we would get if we did: (2a + 2b + 2c) - (2a + 2b + c)

(2a + 2b + 2c) - (2a + 2b + c) = c

- (a + b + c) => summatiopn of the unique elements that you have
- (a + a + b + b + c) => summation of all elements you have

```
singleNumber(input) {
    return 2 * sum(set(input)) - sum(input)
}
```

Time complexity: O(2\*N) = O(N)

Space complexity: O(N)

### Implementing the code

### Approach 3: optimal approach

#### Number representation in binary

```
8   4   3   1
0   1   0   1
```

Binary string "0101" represents 5.

Binary string "1101" represents 11.

We can mainupulate these bits individually to give us different numbers using
bit maninpulation operations, such as `or`, `and`, `xor`.

`XOR` compares two input bits and generates one output bit.

- If the bits are the same, the result is 0.
- If the bits are different, the result is 1.

For number = 11

```
    8   4   2   1
xor 1   0   1   1
    1   0   1   1
    -------------
    0   0   0   0
```

When there is a duplicate, the xor operation will "cancel" the numbers,
leading to a zero.

For number = 2

```
    8   4   2   1
xor 0   0   1   0
    0   0   1   0
    -------------
    0   0   0   0
```

Input: [4, 4, 2, 2, 1], if we xor `2, 2` together, this gives us 0.

For number = 1

```
    8   4   2   1
xor 0   0   0   0
    0   0   0   1
    -------------
    0   0   0   0
```

Input: [4, 4, 2, 2, 1], if we xor `0, 1` together, this gives us 1.

Go over the input, number by number, and xor the inputs together, the
number we get at the end is the number that occurred only once, since
duplicates would just return 0

```
singleNumber(nums) {
    final = 0
    for (num in nums) {
        final ^= num
    }
    return final
}
```

Time complexity: O(N)

Space complexity: O(1)

### Implementing the optimal approach

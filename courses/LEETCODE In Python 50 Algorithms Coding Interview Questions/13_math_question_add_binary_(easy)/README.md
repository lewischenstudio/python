## Section 13: Math Question: Add Binary (Easy)

#### Table of Contents

- Introduction to the problem
- Examples of binary additions
- Pseudocode Implementation
- Pseudocode Walkthrough
- Implementing the code

### Introduction to the problem

Given 2 binary strings, return their sum

[67. Add Binary](https://leetcode.com/problems/add-binary/)

#### Can we receive empty strings?

No, both our input strings will not be empty

#### Decimal Numbers Recap

| 1      | 9     | 9    | 6   |
| ------ | ----- | ---- | --- |
| 1000's | 100's | 10's | 1's |

1996 = 1\*1000 + 9\*100 + 9\*10 + 6\*1

#### Binary Numbers Recap

|  1  |  0  |  1  |  1  |
| :-: | :-: | :-: | :-: |
| 8's | 4's | 2's | 1's |

1011 = 1\*8 + 0\*4 + 1\*2 + 1\*1 = 11

#### Binary Addition

|  A  |  B  | A+B | Sum | Carry |
| :-: | :-: | :-: | :-: | :---: |
|  0  |  0  | 0+0 |  0  |   0   |
|  0  |  1  | 0+1 |  1  |   0   |
|  1  |  0  | 1+0 |  1  |   0   |
|  1  |  1  | 1+1 |  0  |   1   |

### Examples of binary additions

```
1   0   1   1   =   11
1   1   0   1   =   13
-------------

```

1 + 1 = `10`

- carry = 2 / 2 = 1
- result = 2 % 2 = 0

```
        1
1   0   1   1
1   1   0   1
-------------
            0
```

1 + 1 + 0 = `10`

```
    1
1   0   1   1
1   1   0   1
-------------
        0   0
```

1 + 0 + 1 = `10`

```
1
1   0   1   1
1   1   0   1
-------------
    0   0   0
```

1 + 1 + 1 = `11`

- carry = 3 / 2 = 1
- result = 3 % 2 = 1

```
1
    1   0   1   1
    1   1   0   1
------------------
1   1   0   0   0
```

### Pseudocode Implementation

- We want to traverse the 2 strings from right to left, and corresponding elements
- Initially, our result is empty, and our carry is zero
- We can go on as long as we still have bits to operate on
- Initially, sum of current "column" would be equal to the carry to that column
  before we add the bits
- If the first string, a, still have bits, then the i would be still bigger than 0,
  so we add current bit
- Same for the second string, b. If the j is still not 0, that means there is a
  bit at the current position, so we add current bit
- Add what we can get from summing our current bits (`sum % 2`) to the left side
  of the result string

```
addBinary(a, b) {
    i = length(a) - 1
    j = length(b) - 1
    carry = 0
    result = ""
    while (i >= 0 or j >= 0 or carry == 1) {
        sum = carry
        if (i >= 0) {
            sum += a[i]
            i -= 1
        }
        if (j >= 0) {
            sum += a[j]
            j -= 1
        }
        result.addLeft(sum % 2)
        carry = sum / 2
    }
    return result
}
```

Time complexity: O(N)

Space complexity: O(N)

### Pseudocode Walkthrough

### Implementing the code

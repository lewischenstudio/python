## Section 08: Array Question: First Bad Version (Easy)

#### Table of Contents
- Introduction To The Problem And Brute Force Approach
- Optimal Solution Intuition
- Optimal solution pseudocode walkthrough
- Implementing the code



### Introduction To The Problem And Brute Force Approach

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool `isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

[278. First Bad Version](https://leetcode.com/problems/first-bad-version/)


```
isBadVersion(num) {
    return num >= 3
}
solution(n) {
    for i in range[1: n] {
        if (isBadVersion(i) == true) {
            return i
        }
    }
}
```
Time complexity: O(N)
Space complexity: O(1)


### Optimal Solution Intuition
`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

What we know:
- We know that we can determine if a version is bad or not using our given
  "isBadVersion" method
- All version after the first bad version will also be bad

For example, 5. At this point, we know for a fact that all element after current
position version (5) are bad, so we can just ignore all version after that.

`[1, 2, 3, 4, 5]`
3 is a bad version, and we are not sure if it is the first bad version. We do know
that all elements after it won't be the first bad version.

`[1, 2, 3]`
2 is a good version. That means the middle of the versions to be the second element,
and also 2 is a good version so we'll ignore it as well.

#### Solution
- Find the middle between L and R
- If mid is a bad version, then all versions after it are also bad, so we ignore
  them by setting R to be mid
- If mid wasn't a bad version, we would've modified our search range by instead
  setting left to mid + 1
- We want this search to happen as long as we still have elements in our range to
  search in, so as long as L < R

```
solution(n) {
    L = 1
    R = n
    while (L < R) {
        mid = (L + R) / 2
        if (isBadVersion(mid)) {
            R = mid
        } else {
            L = mid + 1
        }
    }
    return L
}
```

### Optimal solution pseudocode walkthrough


### Implementing the code






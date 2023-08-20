## Section 05: Array Question: Container Without Most Water (Medium)

#### Table of Contents
- Problem Introduction
- Brute Force solution Intuition
- psuedo code walkthrough
- Better Approach intuition
- Approach 2 Psuedo code walkthrough
- Implementing the code


### Problem Introduction
Given `n` non-negative integers where each integer represent the height of a vertical
line on a chart. Find two lines, which together with x-axis forms a container, that
holds the biggest amount of water. Return the area of that water.

[11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)


### Brute Force solution Intuition
```
maxArea(heights) {
    max_area = 0
    n = heights.length
    for (i = 0, i < n, i++) {
        for (j = i + 1, j < n, j++) {
            length = min(heights[i], heights[j])
            width = j - 1
            area = length * width
            max_area = max(max_area, area)
        }
    }
}
```

### Better Approach intuition

```
area = min(a, b) * (bi - ai)
```

#### Steps
- Set two pointers at the two ends of the array
- Initialize `max_area = 0`
- Find the area at the current pointers positions
- Update max_area 
- Move the pointer pointing to the smaller value for a shot at a bigger area
- Loop as long as the left pointer is smaller than the right pointer

```
l = 0
r = input length - 1
maxarea = 0
while (l < r) {
    length = min(height[l], height[r])
    width = r - l
    area = length * width
    maxarea = max(maxarea, area)
    if (height[l] < height[r]) {
        l += 1
    } else {
        r -= 1
    }
}
```




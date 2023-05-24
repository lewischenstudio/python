## Section 31: Searching Algorithm

#### Table of Contents
- Introduction to Searching Algorithms
- Linear Search
- Linear Search in Python
- Binary Search
- Binary Search in Python
- Time Complexity of Binary Search


### Introduction to Searching Algorithms
- Linear Search
- Binary Search

### Linear Search

Also known as sequential search. It is the algorithm that searches elements one by one.

Time complexity: O(N)

Space complexity: O(1)

### Linear Search in Python
#### Linear Search Pseudocode
- Create function with two parameters which are an array and a value
- Loop through the array and check if the current array element is equal to the value
- If the element is found, return the index at which the element is found
- If the value is never found, return -1


### Binary Search


### Binary Search in Python
#### Bineary Search Pseudocode
- Create function with two parameters which are sorted array and a value
- Create two pointers: a left pointer at the start of the array and a
right pointer at the end of the array
- Based on left and right pointers calculate middle pointer
- While middle is not equal to the value and start <= end loop:
  - If the middle is greater than the value, move the right pointer down
  - If the middle is less than the value, move the right pointer up
- If the value is never found, return -1


### Time Complexity of Binary Search
- Time complexity: O(LogN)
- Space complexity: O(1)
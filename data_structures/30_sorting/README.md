## Section 30: Sorting

#### Table of Contents
- What is Sorting?
- Types of Sorting
- Sorting Terminologies
- Bubble Sort
- Selection Sort
- Insertion Sort
- Bucket Sort
- Merge Sort
- QuickSort Overview
- Pivot Function Overview
- Pivot Function Implementation
- QuickSort Algorithm Implementation
- Heap Sort
- Comparison of Sorting Algorithms


### What is Sorting?

By definition, sorting refers to arranging data in a particular format: either
ascending or descending.

**Practical Use of Sorting**
- **Microsoft Excel**: Built in functionality to sort data
- **Online Stores**: Online shopping websites generally have option to filter or
sort items by price, review, rating, etc.



### Types of Sorting
```
                      Sorting
                    /         \
                  /             \
                /                 \
              /                     \
            /                         \
          /                             \
     Space Used                     Stability
    /         \                   /           \
   /           \                 /             \
In place   Out of place      Stable        Unstable
```

```
[ 70, 10, 80, 30, 20, 40, 60, 50, 90 ]
[ 10, 20, 30, 40, 50, 60, 70, 80, 90 ]
```

#### Space Used
**In place sorting**: Sorting algorithms which does not require any extra space for sorting

Example: Bubble Sort

**Out of place sorting**: Sorting algorithms which require an extra space for sorting

Example: Merge Sort

#### Stability
**Stable sorting**: If a sorting algorithm after sorting the contents does not
change the sequence of similar content in which they appear, then this sorting is 
call stable sorting.

```
[ 70, 10, 80, 40, 20, 40, 60, 50, 90 ]
               x      y
[ 10, 20, 40, 40, 50, 60, 70, 80, 90 ]
          x   y
```

Example: Insertion Sort

**Unstable sorting**: If a sorting algorithm after sorting the content changes the
sequence of similar content in which they appear, then it is called unstable sort.

```
[ 70, 10, 80, 40, 20, 40, 60, 50, 90 ]
               x      y
[ 10, 20, 40, 40, 50, 60, 70, 80, 90 ]
          y   x
```

Example: Quick Sort

#### Unstable sorting example

**Unsorted Data**
| **Name** | **Age** |
|:--------:|:-------:|
|   Renad  |    7    |
|   Nick   |    6    |
|  Richard |    6    |
|  Parker  |    7    |
|   Sofia  |    7    |

**Sorted by name**
| **Name** | **Age** |
|:--------:|:-------:|
|   Nick   |    6    |
|  Parker  |    7    |
|   Renad  |    7    |
|  Richard |    6    |
|   Sofia  |    7    |

**Sorted by age (stable)**
| **Name** | **Age** |
|:--------:|:-------:|
|   Nick   |    6    |
|  Richard |    6    |
|  Parker  |    7    |
|   Renad  |    7    |
|   Sofia  |    7    |

**Sorted by age (unstable)**
| **Name** | **Age** |
|:--------:|:-------:|
|   Nick   |    6    |
|  Richard |    6    |
|   Renad  |    7    |
|  Parker  |    7    |
|   Sofia  |    7    |

### Sorting Teminologies

#### Increasing Order
- If successful element is greater than the previous one
- Example: 1, 3, 5, 7, 9, 11

#### Decreasing Order
- If successive element is less than the previous one
- Example: 11, 9, 7, 5, 3, 1

#### Non Increasing Order
- If successive element is less than or equal to its previous element in the sequence
- Example: 11, 9, 7, 5, 5, 3, 1

#### Non Decreasing Order
- If successive element is greater than or equal to its previous element in the sequence
- Example: 1, 3, 5, 5, 7, 9, 11

#### Sorting Alogirthms
- Bubble sort
- Selection sort
- Insertion sort
- Bucket sort
- Merge sort
- Quick sort
- Heap sort


#### Which one to select?
- Stability
- Space efficient
- Time efficient


### Bubble Sort
- Bubble sort is also referred as Sinking sort
- We repeatedly compare each pair of adjacent items and
swap them if they are in the wrong order
- We repeatedly go to the beginning and do the comparison
until all items in the correct order

#### When to use Bubble Sort?
- When the input is already sorted
- Space is a concern
- Easy to implement

#### When to avoid Bubble Sort?
- Average time is an issue


### Selection Sort
- In case of selection sort, we repeatedly find the mimum element and
move it to the sorted part of array to make unsorted part sorted
- `sorted_list = []`
- `unsorted_list = [5, 7, 4, 3, 8, 6, 1, 9, 2]`

#### Steps
- Swap 5 and 1 and put 1 into `sorted_list`
  - `sorted_list = [1]`
  - `unsorted_list = [7, 4, 3, 8, 6, 5, 9, 2]`
- Swap 7 and 2 and put 2 into `sorted_list`
  - `sorted_list = [1, 2]`
  - `unsorted_list = [4, 3, 8, 6, 5, 9, 7]`
- Swap 4 and 3 and put 3 into `sorted_list`
  - `sorted_list = [1, 2, 3]`
  - `unsorted_list = [4, 8, 6, 5, 9, 7]`
- Put 4 into `sorted_list`
  - `sorted_list = [1, 2, 3, 4]`
  - `unsorted_list = [8, 6, 5, 9, 7]`
- Repeat the steps above until `sorted_list` is full and `unsorted_list` is empty
  - `sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]`
  - `unsorted_list = []`

#### When to use Selection Sort?
- When we have insufficient memory
- Easy to implement

#### When to avoid Selection Sort?
- Average time is an issue


### Insertion Sort
- Divide the given array into two part
- Take first element from unsorted array and find its correct position in sorted array
- Repeat until unsorted array is empty
- `sorted_list = []`
- `unsorted_list = [5, 3, 4, 7, 2, 8, 6, 9, 1]`

#### Steps
- Put 5 into `sorted_list`
  - `sorted_list = [5]`
  - `unsorted_list = [3, 4, 7, 2, 8, 6, 9, 1]`
- Compare 3 and 5 and put 3 before 5 in `sorted_list`
  - `sorted_list = [3, 5]`
  - `unsorted_list = [4, 7, 2, 8, 6, 9, 1]`
- Compare 4 with `[3, 5]` and put 4 before 5 in `sorted_list`
  - `sorted_list = [3, 4, 5]`
  - `unsorted_list = [7, 2, 8, 6, 9, 1]`
- Compare 7 with `[3, 4, 5]` and put 7 after 5 in `sorted_list`
  - `sorted_list = [3, 4, 5, 7]`
  - `unsorted_list = [2, 8, 6, 9, 1]`
- Repeat the above steps until `unsorted_list` is empty
  - `sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]`
  - `unsorted_list = []`

#### When to use Insertion Sort?
- When we have insufficient memory
- When we have continuous inflow of numbers and we want to keep them sorted
- Easy to implement

#### When to avoid Insertion Sort?
- Average time is an issue


### Bucket Sort
- Create buckets and distribute elements of array into buckets 
- Sort buckets individually
- Merge buckets after sorting
- Number of buckets = round(Sqrt(number of elements))
  - `round(sqrt(9)) = 3`
  - we have 3 buckets: `bucket_1`, `bucket_2`, `bucket_3`
- Appropriate bucket = ceil(value * number buckets / max value)


#### Steps
- Use the formula above to assign each element into its corresponding bucket
  - `unsorted_list = [5, 3, 4, 7, 2, 8, 6, 9, 1]`
  - `ceil(5 * 3 / 9) = ceil(1.6) = 2`
  - `ceil(3 * 3 / 9) = ceil(1) = 1`
  - `ceil(4 * 3 / 9) = ceil(1.3) = 2`
  - `ceil(7 * 3 / 9) = ceil(2.3) = 3`
  - `ceil(2 * 3 / 9) = ceil(0.6) = 1`
  - `ceil(8 * 3 / 9) = ceil(2.6) = 3`
  - `ceil(6 * 3 / 9) = ceil(2) = 2`
  - `ceil(9 * 3 / 9) = ceil(3) = 3`
  - `ceil(1 * 3 / 9) = ceil(0.3) = 1`
- Buckets:
  - `bucket_1 = [3, 2, 1]`
  - `bucket_2 = [5, 4, 6]`
  - `bucket_3 = [7, 8, 9]`
- Use any algorithm to sort each bucket
  - `bucket_1 = [1, 2, 3]`
  - `bucket_2 = [4, 5, 6]`
  - `bucket_3 = [7, 8, 9]`
- Merge all the buckets into a new list
  - `merged_list = bucket_1 + bucket_2 + bucket_3`
  - `merged_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]`

#### When to use Bucket Sort?
- When input uniformly distributed over range, meaning that we should not have
various differences between elements of the array
- The `max value` in ceil(value * number buckets / max value) makes it impossible
for non-uniformly distributed arrays
- Uniformly distributed: 1, 2, 4, 3, 8, 7, 9
- Non-uniformly distributed: 1, 2, 4, 91, 93, 95

#### When to avoid Bucket Sort?
- Average space is an issue



### Merge Sort
- Merge Sort is a divide and conquer algorithm
- Divide the input array into two halves and we keep halving recursively until
they become too small that cannot be broken further
- Merge halves by sorting them
- [6, 4, 3, 7, 5, 1, 2]

#### Steps
- Divide the array once
  - `array_1 = [6, 4, 3, 7]`
  - `array_2 = [5, 1, 2]`
- Divide the arrays twice
  - `array_1 = [6, 4]`
  - `array_2 = [3, 7]`
  - `array_3 = [5, 1]`
  - `array_4 = [2]`
- Divide the arrays until there is only one element in each array
  - `array_1 = [6]`
  - `array_2 = [4]`
  - `array_3 = [3]`
  - `array_4 = [7]`
  - `array_5 = [5]`
  - `array_6 = [1]`
  - `array_7 = [2]`
- Merge two arrays and sort them once
  - `array_1 = [4, 6]`
  - `array_2 = [3, 7]`
  - `array_3 = [1, 5]`
  - `array_4 = [2]`
- Merge two arrays and sort them the second time
  - `array_1 = [3, 4, 6, 7]`
  - `array_2 = [1, 2, 5]`
- Merge two arrays and sort them until there is only one array left
  - `array_1 = [1, 2, 3, 4, 5, 6, 7]`

#### When to use Merge Sort?
- When you need stable sort
- When average expected time is O(NLogN)

#### When to avoid Merge Sort?
- Average space is an issue



### Quick Sort
- Use of a **pivot number**
- Compare the remaining elements to the pivot number
- Implementation of a swap operation

#### Steps:
- `unsorted_array = [3, 5, 0, 6, 2, 1, 4]`
- Use 3 as the **pivot number**, and use `|` for demo purpose
- If a number is greater than 3, then it is marked with **yellow** color
- If a number is less than 3, then it is marked with **blue** color
- 5 > 3, so 5 is **yellow**, and no swapping
  - `[3 | 5, 0, 6, 2, 1, 4]`
- 0 < 3, so 0 is **blue**, and 0 < 5: swap them
  - `[3 | 0, 5, 6, 2, 1, 4]`
- 6 > 3, so 6 is **yellow**, and no swapping
  - `[3 | 0, 5, 6, 2, 1, 4]`
- 2 < 3, so 2 is **blue**, and 2 < 5 (the first number greater than 3): swap them
  - `[3 | 0, 2, 6, 5, 1, 4]`
- 1 < 3, so 1 is **blue**, and 1 < 6 (the first number greater than 3): swap them
  - `[3 | 0, 2, 1, 5, 6, 4]`
- 4 > 3, so 4 is **yellow**, and no swapping
  - `[3 | 0, 2, 1, 5, 6, 4]`
- Swap the last small number, 1, with the pivot number 3, and 3 is now ordered
  - `[1, 0, 2 | 3 | 5, 6, 4]`
- Split the left and the right side of 3 into two arrays and repeat the steps
above for those two arrays
  - `[[1, 0, 2] | 3 | [5, 6, 4]]`
- For each subarray, repeat the same steps recursively until each array is sorted
  - `[[0, |1| 2] | 3 | [4, |5| 6]]`
- Recursively append each item in the arrays into the new array
  - `[0, 1, 2, 3, 4, 5, 6]`



### Heap Sort
- Step 1: Insert data into Binary Heap Tree
- Step 2: Extract data from Binary Heap
- It is best suited with array, and it doesn't work with Linked List

**Binary Heap** is a binary tree with special properties
- The value of any given node must be less or equal to its children (min heap)
- The value of any given node must be greater or equal to its children (max heap)
```
                    5
                 /    \  
              /         \  
           /               \  
         10                 20
        /  \               /  \ 
      /      \           /      \ 
    30        40       50        60
   /  \       
 70    80
```
#### Example: `[15, 10, 40, 20, 50, 10, 30, 45, 5]`

#### Step 1: Insert data into Binary Heap Tree
```
                   10
                 /    \  
              /         \  
           /               \  
         15                 10
        /  \               /  \ 
      /      \           /      \ 
    20        50       40        30
   /  \       
 45    5
```
```
                   10
                 /    \  
              /         \  
           /               \  
         15                 10
        /  \               /  \ 
      /      \           /      \ 
    5        50       40        30
   /  \       
 45    20
```
```
                   10
                 /    \  
              /         \  
           /               \  
         5                  10
        /  \               /  \ 
      /      \           /      \ 
    15        50       40        30
   /  \       
 45    20
```
```
                    5
                 /    \  
              /         \  
           /               \  
         10                 10
        /  \               /  \ 
      /      \           /      \ 
    15        50       40        30
   /  \       
 45    20
```

#### Step 2: Extract data from Binary Heap
- Extract 5 into array: `[5, ]`
- Move 45 to the root, then sort the left childe (smaller or equal)
```
                   10
                 /    \  
              /         \  
           /               \  
         15                 10
        /  \               /  \ 
      /      \           /      \ 
    20        50       40        30
   /         
 45    
```
- Extract 10 into array: `[5, 10]`
- Move 45 to the root, then sort the right child (smaller)
```
                   10
                 /    \  
              /         \  
           /               \  
         15                 30
        /  \               /  \ 
      /      \           /      \ 
    20        50       40        45
```
- Extract 10 into array: `[5, 10, 10]`
- Move 45 to the root, then sort the left child (smaller)
```
                   15
                 /    \  
              /         \  
           /               \  
         20                 30
        /  \               /  
      /      \           /    
    45        50       40     
```
- Extract 15 into array: `[5, 10, 10, 15]`
- Move 40 to the root, then sort the left child (smaller)
```
                   20
                 /    \  
              /         \  
           /               \  
         40                 30
        /  \               
      /      \           
    45        50
```
- Extract 20 into array: `[5, 10, 10, 15, 20]`
- Move 50 to the root, then sort the left child (smaller)
```
                   30
                 /    \  
              /         \  
           /               \  
         40                 50
        /                
      /                 
    45        
```
- Repeat the above steps to extra all data into the array
  - `[5, 10, 10, 15, 20, 30, 40, 45, 50]`


### Comparison of Sorting Algorithms
| **Name**       | **Time Complexity** | **Space Complexity** | **Stable** |
|----------------|---------------------|----------------------|------------|
| Bubble Sort    | O(N^2)              | O(1)                 | Yes        |
| Selection Sort | O(N^2)              | O(1)                 | No         |
| Insertion Sort | O(N^2)              | O(1)                 | Yes        |
| Bucket Sort    | O(N LogN)           | O(N)                 | Yes        |
| Merge Sort     | O(N LogN)           | O(N)                 | Yes        |
| Quick Sort     | O(N LogN)           | O(N)                 | No         |
| Heap Sort      | O(N LogN)           | O(1)                 | No         |
import array
import numpy as np

# Create an Array
my_array = array.array("i")
print(my_array)
my_array1 = array.array("i", [1, 2, 3, 4])  # O(N)
print(my_array1)

np_array = np.array([], dtype=int)
print(np_array)
np_array1 = np.array(
    [
        1,
        2,
        3,
        4,
    ]
)  # O(N)
print(np_array1)


# Insertion to Array
my_array1.insert(2, 6)
print(my_array1)
my_array1.insert(0, 6)
print(my_array1)


# Traversal Operation
def traverseArray(arr):
    for i in arr:
        print(i)


arr1 = array.array("i", [1, 2, 3, 4, 5, 6])
arr2 = array.array("d", [1.3, 1.5, 1.6])
traverseArray(arr1)
traverseArray(arr2)


# Accessing an element of Array
def accessElement(arr, index):
    if index > len(arr) - 1 or index < 0:
        print("there is no any element in this index")
        return
    print(arr[index])
    return arr[index]


accessElement(arr1, 6)
accessElement(arr1, 0)
accessElement(arr1, 1)
accessElement(arr1, 2)
accessElement(arr2, 1)
accessElement(arr2, 2)


# Searching for an element in Array
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"found {target} at index {i}")
            break
    print("Item not found")
    return


linear_search(arr1, 0)
linear_search(arr1, 1)
linear_search(arr1, 3)

# Deleting an element from Array

arr1.remove(1)
print(arr1)

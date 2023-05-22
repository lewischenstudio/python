"""
Merge Sort with Merge Function
Time complexity: O(NLogN)
Space complexity: O(N)
"""


def merge(customList, left, middle, right):
    """
    customList: input list to be sorted
    left: first index of the list
    middle: middle of the list
    right: length of the list
    """
    print("customList: ", customList)
    n1 = middle - left + 1  # length of first subarray
    n2 = right - middle  # length of second subarray

    left_list = [0] * (n1)  # left list
    right_list = [0] * (n2)  # right list

    for i in range(0, n1):
        left_list[i] = customList[left + i]

    for j in range(0, n2):
        right_list[j] = customList[middle + 1 + j]

    i = 0  # initial index of the first subarray
    j = 0  # initial index of the second subarray
    k = left  # initial index of the merged subarray

    # sort each element while merging them
    while i < n1 and j < n2:
        if left_list[i] <= right_list[j]:
            customList[k] = left_list[i]
            i += 1
        else:
            customList[k] = right_list[j]
            j += 1
        k += 1

    # copy the remaining element of the left subarray if there is any
    while i < n1:
        customList[k] = left_list[i]
        i += 1
        k += 1

    # copy the remaining element of the right subarray if there is any
    while j < n2:
        customList[k] = right_list[j]
        j += 1
        k += 1


def mergesort_helper(customList, left, right):
    """
    customList: input list to be sorted
    left: first index of the left subarray
    right: first index of the right subarray
    """
    if left < right:
        # divided by two and taking the floor of that number
        # split the initial array until each element is an entire array
        middle = (left + (right - 1)) // 2  # O(1)
        print("left: ", left)
        print("middle: ", middle)
        print("right: ", right)
        mergesort_helper(customList, left, middle)  # T(n/2)
        mergesort_helper(customList, middle + 1, right)  # T(n/2)

        # merge each subarray into a sorted array
        merge(customList, left, middle, right)  # O(n)
        print("\n")
    return customList


def mergeSort(customList, ascending: bool = True):
    sorted_list = mergesort_helper(customList, 0, len(customList) - 1)
    if not ascending:
        sorted_list.reverse()
    print(sorted_list)
    return sorted_list


custom_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
mergeSort(custom_list)
mergeSort(custom_list, False)

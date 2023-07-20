"""
Quick Sort
"""


def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


def pivot(my_list, pivot_index, end_index):
    """
    end_index: the new swap index
    """
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        # swap 0 with 5
        # swap 2 with 5
        # swap 6 with 1
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    # swap 3 with 1, so 3 is ordered in the middle
    swap(my_list, pivot_index, swap_index)
    # return the new swap index for the left and right side of 3
    return swap_index


def quicksort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        # recursively sort the left and the right array of the pivot number
        quicksort_helper(my_list, left, pivot_index - 1)
        quicksort_helper(my_list, pivot_index + 1, right)
    return my_list


def quickSort(my_list, ascending: bool = True):
    sorted_list = quicksort_helper(my_list, 0, len(my_list) - 1)
    if not ascending:
        sorted_list.reverse()
    return sorted_list


my_list = [3, 5, 0, 6, 2, 1, 4]
print(quickSort(my_list, False))

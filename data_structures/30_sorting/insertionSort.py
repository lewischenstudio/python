"""
Insertion Sort
"""


def insertionSort(customList: list, ascending: bool = True):
    for i in range(1, len(customList)):  # O(n)
        key = customList[i]
        j = i - 1
        if ascending:  # O(1)
            while j >= 0 and key < customList[j]:  # O(n)
                customList[j + 1] = customList[j]  # O(1)
                j -= 1
        else:
            while j >= 0 and key > customList[j]:  # O(n)
                customList[j + 1] = customList[j]  # O(1)
                j -= 1
        customList[j + 1] = key
    print(customList)
    return customList


custom_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
insertionSort(custom_list, False)

"""
Selection Sort
"""


def selectionSort(customList: list, ascending: bool = True):
    for i in range(len(customList)):  # O(n)
        min_index = i
        for j in range(i + 1, len(customList)):  # O(n)
            if ascending:
                if customList[min_index] > customList[j]:  # O(1)
                    min_index = j
            else:
                if customList[min_index] < customList[j]:  # O(1)
                    min_index = j
        customList[i], customList[min_index] = (
            customList[min_index],
            customList[i],
        )
    print(customList)
    return customList


custom_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
selectionSort(custom_list)

"""
Bubble Sort
"""


def bubbleSort(customList: list, ascending: bool = True):
    for i in range(len(customList) - 1):  # O(n)
        for j in range(len(customList) - i - 1):  # O(n)
            if ascending:
                if customList[j] > customList[j + 1]:  # O(1)
                    customList[j], customList[j + 1] = (
                        customList[j + 1],
                        customList[j],
                    )
            else:
                if customList[j] < customList[j + 1]:  # O(1)
                    customList[j + 1], customList[j] = (
                        customList[j],
                        customList[j + 1],
                    )
    print(customList)
    return customList


custom_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
bubbleSort(custom_list, False)

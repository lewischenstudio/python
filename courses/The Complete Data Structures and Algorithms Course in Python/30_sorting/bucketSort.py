"""
Bucket Sort with Insertion Sort
Time complexity: O(N^2)
Space complexity: O(N)
"""
import math


def insertionSort(customList: list, ascending: bool = True):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        if ascending:
            while j >= 0 and key < customList[j]:
                customList[j + 1] = customList[j]
                j -= 1
        else:
            while j >= 0 and key > customList[j]:
                customList[j + 1] = customList[j]
                j -= 1
        customList[j + 1] = key
    return customList


def bucketSort(customList: list, ascending: bool = True):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    # make the number of buckets
    for i in range(numberofBuckets):  # O(n)
        arr.append([])

    # append each element to its corresponding bucket
    for j in customList:  # O(n)
        index_b = math.ceil(j * numberofBuckets / maxValue)
        arr[index_b - 1].append(j)

    # use Insertion Sort to sort each bucket
    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i], ascending)  # O(n^2)

    k = 0
    for i in range(numberofBuckets):  # O(n)
        if not ascending:
            i = numberofBuckets - i - 1
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    print(customList)
    return customList


custom_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
bucketSort(custom_list, False)

custom_list = [91, 2, 93, 4, 95, 1]
bucketSort(custom_list)
bucketSort(custom_list, False)

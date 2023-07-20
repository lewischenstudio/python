"""
Heap Sort
Time complexity: O(NLogN)
Space complexity: O(1)
"""


def heapify(customList, n, i):
    """
    n: length of the custom list
    i: current index of the custom list
    """
    smallest = i
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2
    if leftChild < n and customList[leftChild] < customList[smallest]:
        smallest = leftChild

    if rightChild < n and customList[rightChild] < customList[smallest]:
        smallest = rightChild

    if smallest != i:
        customList[i], customList[smallest] = (
            customList[smallest],
            customList[i],
        )
        heapify(customList, n, smallest)


def heapSort(customList, ascending: bool = True):
    n = len(customList)
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(customList, n, i)

    for i in range(n - 1, 0, -1):
        customList[i], customList[0] = (
            customList[0],
            customList[i],
        )
        heapify(customList, i, 0)
    if ascending:
        customList.reverse()
    print(customList)
    return customList


custom_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
heapSort(custom_list)
heapSort(custom_list, False)

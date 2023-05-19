"""
Binary Heap
"""


class Heap:
    def __init__(self, size, heapType):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1
        self.heapType = heapType


def peekofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]


def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize


def levelOrderTraversal(rootNode):
    if not rootNode or rootNode.customList is None:
        return
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[i])


def heapifyTreeInsert(rootNode, index):
    parentIndex = int(index / 2)
    if index <= 1:
        return
    if rootNode.heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
    elif rootNode.heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
    heapifyTreeInsert(rootNode, parentIndex)  # O(logN)


def inserNode(rootNode, nodeValue):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is Full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize)
    return "The value has been successfully inserted"


def heapifyTreeExtract(rootNode, index):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return

    if rootNode.heapSize == leftIndex:
        if rootNode.heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if rootNode.heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:  # noqa
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:  # noqa
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyTreeExtract(rootNode, swapChild)


def extractNode(rootNode):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1)
        return extractedNode


def deleteEntireBP(rootNode):
    rootNode.customList = None


newHeap = Heap(5, "Max")
inserNode(newHeap, 4)
inserNode(newHeap, 5)
inserNode(newHeap, 2)
inserNode(newHeap, 1)
levelOrderTraversal(newHeap)
extractNode(newHeap)
levelOrderTraversal(newHeap)
deleteEntireBP(newHeap)

newHeap = Heap(5, "Min")
inserNode(newHeap, 50)
inserNode(newHeap, 20)
inserNode(newHeap, 30)
inserNode(newHeap, 10)
levelOrderTraversal(newHeap)
extractNode(newHeap)
levelOrderTraversal(newHeap)
deleteEntireBP(newHeap)
levelOrderTraversal(newHeap)

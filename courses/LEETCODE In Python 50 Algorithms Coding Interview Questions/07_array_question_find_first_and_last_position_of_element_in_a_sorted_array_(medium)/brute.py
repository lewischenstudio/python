def findFirst(input: [], target: int) -> int:
    for i in range(len(input)):
        if input[i] == target:
            return i
    return -1


def findLast(input: [], target: int) -> int:
    for i in range(len(input) - 1, 0, -1):
        if input[i] == target:
            return i
    return -1


def searchRange(input: [], target: int):
    first = findFirst(input, target)
    last = findLast(input, target)
    return [first, last]


if __name__ == "__main__":
    print(searchRange([5, 7, 7, 8, 8, 10], 8))
    print(searchRange([5, 7, 7, 8, 8, 10], 6))
    print(searchRange([11, 13, 13, 16, 13], 13))
    print(searchRange([11, 13, 15, 17, 18], 14))

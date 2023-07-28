def getLeftPosition(input: [], target: int):
    left = 0
    right = len(input) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if input[mid] == target:
            if mid == 0 or input[mid - 1] != target:
                return mid
            right = mid - 1
        elif input[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def getRightPosition(input: [], target: int):
    left = 0
    right = len(input) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if input[mid] == target:
            if mid == len(input) - 1 or input[mid + 1] != target:
                return mid
            left = mid + 1
        elif input[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def searchRange(input: [], target: int):
    left = getLeftPosition(input, target)  # O(log(n))
    right = getRightPosition(input, target)  # O(log(n))
    return [left, right]


if __name__ == "__main__":
    print(searchRange([5, 7, 7, 8, 8, 10], 8))
    print(searchRange([5, 7, 7, 8, 8, 10], 6))
    print(searchRange([11, 13, 13, 16, 13], 13))
    print(searchRange([11, 13, 15, 17, 18], 14))

def missingNumber(nums: []) -> int:
    for i in range(0, len(nums) + 1):
        if i not in nums:
            return i
    return -1


if __name__ == "__main__":
    print(missingNumber([3, 0, 1]))
    print(missingNumber([0, 1]))
    print(missingNumber([1, 2]))
    print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(missingNumber([9, 6, 4, 2, 3, 8, 7, 0, 1]))

def move_zeroes(nums: list) -> list:
    j = 0
    for item in nums:
        if item != 0:
            nums[j] = item
            j += 1
    for i in range(j, len(nums)):
        nums[i] = 0
    return nums


if __name__ == "__main__":
    print(move_zeroes([0, 1, 0, 3, 12]))
    print(move_zeroes([0, 2, 0, 0, 4, 0]))

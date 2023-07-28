def move_zeroes(nums: list) -> list:
    output = []
    for item in nums:
        if item != 0:
            output.append(item)
    for i in range(len(output), len(nums)):
        output.append(0)
    return output


if __name__ == "__main__":
    print(move_zeroes([0, 1, 0, 3, 12]))

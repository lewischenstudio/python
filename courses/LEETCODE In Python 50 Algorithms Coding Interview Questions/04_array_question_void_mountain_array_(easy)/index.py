def validMountainArray(arr: list) -> bool:
    i = 1
    while i < len(arr) and arr[i] > arr[i - 1]:
        i += 1
    if i == 1 or i == len(arr):
        return False
    while i < len(arr) and arr[i] < arr[i - 1]:
        i += 1
    return i == len(arr)


if __name__ == "__main__":
    print(validMountainArray([2, 1]))
    print(validMountainArray([3, 5, 5]))
    print(validMountainArray([0, 3, 2, 1]))

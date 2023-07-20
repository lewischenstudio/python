"""Coding Exercise 10: Pairs / Two Sum - LeetCode 1"""


def findPairs(list_, sum_):
    a = False
    b = False
    for i in range(len(list_)):
        for j in range(i + 1, len(list_)):
            if (list_[i] + list_[j]) == sum_:
                print(list_[i], list_[j])
                a = True
                b = True
    if not a and not b:
        print("Not Found")


findPairs([2, 6, 3, 9, 11], 9)
findPairs([2, 6, 3, 9, 11], 11)
findPairs([2, 6, 3, 9, 11], 6)


# LeetCode Solution


def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i


nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")

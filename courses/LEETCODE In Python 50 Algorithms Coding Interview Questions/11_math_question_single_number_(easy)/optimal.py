"""Single Number"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans


if __name__ == "__main__":
    print(Solution().singleNumber([1, 1, 3, 3, 4]))
    print(Solution().singleNumber([2, 1, 1, 2, 3]))
    print(Solution().singleNumber([5, 9, 0, 1, 9, 5, 0]))
    print(Solution().singleNumber([1, 1, 3, 3, 2]))

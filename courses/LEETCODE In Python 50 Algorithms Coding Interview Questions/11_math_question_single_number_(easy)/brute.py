"""Single Number"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        m = {}
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1
        for key in m.keys():
            if m[key] == 1:
                return key


if __name__ == "__main__":
    print(Solution().singleNumber([1, 1, 3, 3, 4]))
    print(Solution().singleNumber([2, 1, 1, 2, 3]))
    print(Solution().singleNumber([5, 9, 0, 1, 9, 5, 0]))
    print(Solution().singleNumber([1, 1, 3, 1, 3, 2]))

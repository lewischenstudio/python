class Solution:
    def __init__(self, bad_version) -> None:
        self.bad_version = bad_version

    def isBadVersion(self, num):
        return num >= self.bad_version

    def firstBadVersion(self, n):
        left = 1
        right = n
        while left < right:
            mid = int((left + right) / 2)
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        if self.bad_version > n:
            return -1
        return left


if __name__ == "__main__":
    print(Solution(3).firstBadVersion(5))
    print(Solution(5).firstBadVersion(10))
    print(Solution(6).firstBadVersion(5))

class Solution:
    def __init__(self, bad_version) -> None:
        self.bad_version = bad_version

    def isBadVersion(self, num):
        return num >= self.bad_version

    def firstBadVersion(self, n):
        for i in range(n):
            if self.isBadVersion(i):
                return i
        return -1


if __name__ == "__main__":
    print(Solution(3).firstBadVersion(5))
    print(Solution(6).firstBadVersion(10))
    print(Solution(6).firstBadVersion(5))

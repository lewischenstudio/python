"""Robot Return to Origin"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ""
        while i >= 0 or j >= 0 or carry == 1:
            sum_ = carry
            if i >= 0:
                sum_ += int(a[i])
                i -= 1
            if j >= 0:
                sum_ += int(b[j])
                j -= 1
            result = str(sum_ % 2) + result
            carry = sum_ // 2

        return result


if __name__ == "__main__":
    print(Solution().addBinary("1011", "1101"))
    print(Solution().addBinary("110", "010"))
    print(Solution().addBinary("1", "1"))
    print(Solution().addBinary("0", "0"))

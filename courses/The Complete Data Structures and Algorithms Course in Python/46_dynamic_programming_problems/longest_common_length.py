"""Longest Common Subsequence Length Problem"""


def LCSLength(S1, S2, lenS1, lenS2):
    if lenS1 == 0 or lenS2 == 0:
        return 0
    if S1[lenS1 - 1] == S2[lenS2 - 1]:
        return 1 + LCSLength(S1, S2, lenS1 - 1, lenS2 - 1)
    else:
        op1 = LCSLength(S1, S2, lenS1, lenS2 - 1)
        op2 = LCSLength(S1, S2, lenS1 - 1, lenS2)
        return max(op1, op2)


S1 = "ABCBDAB"
S2 = "BDCABA"
print(LCSLength(S1, S2, len(S1), len(S2)))

"""Longest Repeated Substring Length Problem"""


def LRSLength(s, index1, index2):
    """Algorithm fails most of the time"""
    # return if we have reached the end of either string
    if index1 == 0 or index2 == 0:
        return 0
    # if characters at index1 and index2 matches and they are different
    if s[index1 - 1] == s[index2 - 1] and index1 != index2:
        # if index1 < len(s) and s[index1] == s[index2 - 1]:
        #     return LRSLength(s, index1 - 1, index2 - 1)
        return 1 + LRSLength(s, index1 - 1, index2 - 1)
    # else if characters at index m and n don't match
    op1 = LRSLength(s, index1, index2 - 1)
    op2 = LRSLength(s, index1 - 1, index2)
    return max(op1, op2)


print(LRSLength("ATAKTKGGA", 9, 9))
print(LRSLength("ABCDEFEGA", 9, 9))
print(LRSLength("abbbbebba", 9, 9))

""" Number Factor Dynamic Programming"""


# Top Down Approach
def numberFactorTD(n, memo):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    elif n not in memo:
        sub1 = numberFactorTD(n - 1, memo)
        sub2 = numberFactorTD(n - 3, memo)
        sub3 = numberFactorTD(n - 4, memo)
        memo[n] = sub1 + sub2 + sub3
    return memo[n]


print(numberFactorTD(5, {}))


# Bottom Up Approach
def numberFactorBU(n):
    tb = [1, 1, 1, 2]
    for i in range(4, n + 1):
        tb.append(tb[i - 1] + tb[i - 3] + tb[i - 4])
    return tb[n]


print(numberFactorBU(5))

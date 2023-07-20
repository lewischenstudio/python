"""Fibonacci Series with Tabulation """


def fibonacciTab(n):
    tb = [0, 1]
    for i in range(2, n + 1):
        tb.append(tb[i - 1] + tb[i - 2])
    return tb[n - 1]


print(fibonacciTab(6))

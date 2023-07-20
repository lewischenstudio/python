"""Fibonacci Series with Memoization """


def fibonacciMemo(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        memo[n] = fibonacciMemo(n - 1, memo) + fibonacciMemo(n - 2, memo)
    return memo[n]


myDict = {}
print(fibonacciMemo(6, myDict))

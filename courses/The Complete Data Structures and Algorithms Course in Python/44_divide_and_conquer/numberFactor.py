"""Number Factor Problem  in Python"""


def numberFactor(n):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        subP1 = numberFactor(n - 1)
        subP2 = numberFactor(n - 3)
        subP3 = numberFactor(n - 4)
        return subP1 + subP2 + subP3


print(numberFactor(5))
print(numberFactor(7))


def numberFactor2(n, arr):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        subP1 = 0
        for i in arr:
            subP1 += numberFactor2(n - i, arr)
        return subP1


print(numberFactor2(5, [1, 3, 4]))
print(numberFactor2(7, [1, 3, 4]))

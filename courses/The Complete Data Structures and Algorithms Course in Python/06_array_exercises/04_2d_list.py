"""Coding Exercise 4: 2D Lists"""


def sumDiagonal(a):
    if len(a) == 1:
        n = len(a)
        return a[0][int(n / 2)]
    sum = 0
    for i in range(len(a)):
        row = a[i]
        m = int(len(row) / 2)
        sum += row[m]
    return sum


myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sumDiagonal(myList2D))

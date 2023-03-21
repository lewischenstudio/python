# Question 1 - Missing Number

def findMissing(arr, n):
    sum1 = n * (n + 1) / 2
    sum2 = sum(arr)
    print(sum1 - sum2)

myList = [i for i in range(1, 101, 1)]
myList.remove(73)
print('myList: ', myList)
findMissing(myList, 100)
def minimalHeaviestSetA(arr):
    # Write your code here
    arr.sort(reverse=True)
    setA = []
    for i in range(len(arr)):
        compare_A = sum(arr[:i+1])
        compare_B = sum(arr[i+1:])
        if compare_A < compare_B:
            setA.append(arr[i])
        if compare_A >= compare_B:
            setA.append(arr[i])
            break
    print('setA: ', setA)
    return setA

arr = [6,5,3,2,4,1,2]
# arr = [3,7,5,6,2]
minimalHeaviestSetA(arr)
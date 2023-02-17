
def quick_sort(arr):
    if len(arr) in [0, 1]:
        return arr
    for i in range(len(arr)-1):
        this = arr[i]
        for j in range(1, len(arr)):
            if this > arr[j]:
                new = arr[j]
                arr[j] = this
                arr[i] = new
                # this = arr[j]
                # arr[j] = new
        # if i == 0:
            # break
        # if this > arr[i]:
        #     new = arr[i]
        #     arr[i] = this
        #     arr[i - 1] = new
        # else:
        #     new = arr[i]
        #     this = arr[i]
            # arr[i] = this
            # this = new

    return arr

arr = [4,5,2,3,1]
print(quick_sort(arr))

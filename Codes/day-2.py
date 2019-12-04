def day2(arr):
    leftArr = [1]*len(arr)
    rightArr = [1]*len(arr)

    #Making the left array
    for i in range(1,len(arr)):
        leftArr[i] = leftArr[i-1]*arr[i-1]

    #Making the right array
    for i in range(len(arr)-2, -1, -1):
        rightArr[i] = rightArr[i+1]*arr[i+1]

    res = []

    for i in range(len(arr)):
        tmp = leftArr[i]*rightArr[i]
        res.append(tmp)

    return res

arr = [3,2,1]
print(day2(arr))    
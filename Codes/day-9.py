def largestSumNonAdj(arr):
    val1 = arr[0]
    if len(arr) == 1:
        return val1
    
    val2 = max(arr[0], arr[1])
    if len(arr) == 2:
        return val2
    
    max_val = 0
    for i in range(2, len(arr)):
        max_val = max(arr[i]+val1, val2)
        val1 = val2
        val2 = max_val
    
    return max_val


arr = [-5,1,-6,5]
print(largestSumNonAdj(arr))
def day4(A):
    m = max(A)

    if m < 1:
        return 1
    
    if len(A) == 1:
        return 2 if m == 1 else 1
    
    arr = [0]*m

    for i in range(len(A)):
        if A[i] > 0:
            arr[A[i]-1] = 1

    for i in range(len(arr)):
        if arr[i] != 1:
            return i+1

    return i+2

print(day4([1,2,0]))    
    
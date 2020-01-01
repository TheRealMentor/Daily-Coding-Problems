def trappedWater(arr):
    left_max, right_max = 0, 0
    res = 0
    left, right = 0, len(arr)-1

    while(left < right):
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                res += (left_max - arr[left])
            left+=1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                res += (right_max - arr[right])
            right-=1
    
    return res

print(trappedWater([3, 0, 1, 3, 0, 5]))

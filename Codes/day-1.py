arr = list(map(int, input().split()))
k = int(input())

n = len(arr)
hash_map = set()

def day1(arr, k):    
    for i in range(n):
        if k - arr[i] in hash_map:
            return True
        else:
            hash_map.add(arr[i])
    
    return False

print(day1(arr, k))
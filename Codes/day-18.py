print('Brute force solution:')
#This is O(n^2) solution
def maxValSubArr(arr, k):
    for i in range(len(arr)):
        if i+k <= len(arr):
            tmpSubArr = arr[i:i+k]
            print(max(tmpSubArr), end=' ')
        else:
            break
    return None

maxValSubArr([10,5,2,7,8,7], 3)

print('\nSolution using heapq:')

import heapq
#This is O(n) solution
def maxValSubArrK(arr, k):
    i = 0
    j = k-1

    heap = arr[i:j+1]
    heapq._heapify_max(heap)

    print(heap[0], end=' ')
    lastel = arr[i]
    i += 1
    j += 1
    nextel = arr[j]

    while j < len(arr):
        heap[heap.index(lastel)] = nextel
        heapq._heapify_max(heap)
        print(heap[0], end=' ')

        lastel = arr[i]
        i+=1
        j+=1
        if j < len(arr):
            nextel = arr[j]
    
maxValSubArrK([10,5,2,7,8,7], 3)

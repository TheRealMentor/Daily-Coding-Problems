#Time complexity - O(nlogn), Space complexity - O(n)
def minRooms(intervals):
    timeArr = []

    for i in range(len(intervals)):
        timeArr.append((intervals[i][0], 'S'))
        timeArr.append((intervals[i][1], 'E'))
    
    timeArr.sort()
    rooms = 0
    minRoom = 0

    for i in range(len(timeArr)):
        if timeArr[i][1] == 'S':
            rooms+=1
            minRoom = max(minRoom, rooms)
        else:
            rooms-=1
    
    return minRoom

print(minRooms([(30, 75), (0, 50), (60, 150)]))

#Time complexity - O(nlogn), Space complexity - O(1)
def minRoomsReq(intervals):
    intervals.sort()
    
    rooms_req = 1
    res = 1
    i = 1
    j = 0
    n = len(intervals)

    while i<n and j<n:
        if intervals[i][0] < intervals[j][1]:
            rooms_req += 1
            i+=1

            if rooms_req > res:
                res = rooms_req
        
        else:
            rooms_req-=1
            j+=1
    
    return res
    
print(minRoomsReq([(30, 75), (0, 50), (60, 150)]))
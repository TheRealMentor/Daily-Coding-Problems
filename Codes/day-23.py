R = 4
C = 4
matrix = [[1, 1, 1, 1],
          [0, 0, 1, 0],
          [1, 1, 1, 1],
          [1, 1, 1, 1]]

rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]


def isValid(row, col):
    return (row >= 0) and (row < R) and (col >= 0) and (col < C)

def pathFinder(matrix, src, dest):
    if not matrix[src[0]][src[1]] or not matrix[dest[0]][dest[1]]:
        return -1
    
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[src[0]][src[1]] = True

    q = []
    q.append([src, 0])

    while(len(q)!=0):
        curr = q.pop()
        currPt = curr[0]
        dist = curr[1]

        if (currPt[0] == dest[0]) and (currPt[1] == dest[1]):
            return dist
        
        for i in range(4):
            row = currPt[0] + rowNum[i]
            col = currPt[1] + colNum[i]

            if (isValid(row, col) and matrix[row][col] and not visited[row][col]):
                visited[row][col] = True
                nextPt = [row, col]
                q.append([nextPt, dist+1])

    return -1

print(pathFinder(matrix, [2,0], [0,0]))
def paintHouses(n, k, costs):
    cost = [[0 for _ in range(k)] for _ in range(n)]

    cost[0] = costs[0][:]

    for house in range(n):
        for color in range(k):
            pre = cost[house-1][:color] + cost[house-1][color+1:]
            cost[house][color] = costs[house][color] + min(pre)
    
    return min(cost[-1])

costs = [[4,0,3],[8,3,8],[4,5,0],[3,4,4],[8,8,0]]
print(paintHouses(5,3,costs))
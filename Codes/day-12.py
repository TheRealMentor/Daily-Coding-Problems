def num_of_ways(N):
    if N == 0 or N == 1:
        return 1
    numWays = [0]*(N+1)
    numWays[0] = 1 #Number of ways to climb 0 step stair
    numWays[1] = 1 #Number of ways to climb 1 step stair

    for i in range(2, N+1):
        numWays[i] = numWays[i-1] + numWays[i-2]
    
    return numWays[N]

print(num_of_ways(6))

#if there is a set of steps to take!
def num_of_ways_v2(N):
    if N == 0 or N == 1 or N == 2:
        return 1
    numWays = [0]*(N+1)
    numWays[0] = numWays[1] = numWays[2] = 1

    for i in range(3, N+1):
        numWays[i] = numWays[i-1] + numWays[i-3] + numWays[i-5]
    
    return numWays[N]

print(num_of_ways_v2(7))